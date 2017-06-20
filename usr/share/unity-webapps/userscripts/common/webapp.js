
function WebApp(appInfo, callbacks) {
    this._init(appInfo, callbacks);
}

WebApp.match = { FIRST: 0, ANY: 1, ALL: 2 };
WebApp.prototype = {
    _init: function (appInfo, callbacks) {
        this._appInfo = appInfo;
        this._totalWeight = 0.0;
        this._validItems = [];
        this._callbacks = callbacks;
        this._retries = 0;
    },

    _unityLoaded: function () {
        try {
            var i, nodeFunction = function () {
                return document.evaluate("(" + this.node + ")[" + this.index + "]",
                                         document,
                                         null,
                                         XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                         null).snapshotItem(0);
            };

            for (i = 0; i < this._validItems.length; i++) {
                var item = this._validItems[i];
                if (item.install !== undefined) {
                    item.install(nodeFunction.bind(item));
                }
            }
        } catch (e) {
            console.log("Exception attempting item install = " + e);
        }

        var indicatorsController = new Indicators(function () {
                return this._unityCallback();
            }.bind(this));

        if (this._callbacks.loaded !== undefined) {
            this._reportInfo("calling loaded callback");
            this._callbacks.loaded(indicatorsController);
        }
    },

    setupPage: function () {
        function nodeValue(node) {
            if (typeof node === 'string') {
                var resultSet = document.evaluate(node,
                                                  document,
                                                  null,
                                                  XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                                  null);
                var i, arrayized = [];
                for (i = 0; i < resultSet.snapshotLength; i++) {
                    arrayized.push(resultSet.snapshotItem(i));
                }
                return arrayized;
            } else if (typeof node === 'function') {
                return node();
            }

            return [];
        }

        // Can we skip?
        if (this._totalWeight > 0.0) {
            if (this._appInfo.validator(this._totalWeight)) {
                return true;
            }
            this._totalWeight = 0.0;
        }

        var pageData = {};

        var i = 0, j = 0, k = 0;

        // Try and find login
        // Always collect login if available
        if (this._appInfo.login !== undefined) {
            var loginTests = this._appInfo.login;
            for (i = 0; i < loginTests.nodes.length; i++) {
                var nodeTest = {
                    name: loginTests.name,
                    query: loginTests.nodes[i],
                    validator: loginTests.validator,
                    fragment: loginTests.fragment,
                    value: loginTests.value
                };

                var loginNode = validatedNode(nodeTest);
                if (loginNode !== null) {
                    this._login = validatedNodeValue(nodeTest, loginNode);
                }
            }
            if (this._login === undefined) {
                if (this._shouldRetry()) {
                    this._reportWarning("Failed to find login will retry");
                    return false;
                } else {
                    this._reportError("Unable to obtain login information");
                    return true;
                }
            } else {
                this._reportInfo("Found login: " + this._login);
            }
        }

        // Check all items
        var itemsTests = this._appInfo.items;
        var valueFunction = function () {
                var result = document.evaluate("(" + this.node + ")[" + this.index + "]",
                                                 document,
                                                 null,
                                                 XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null).snapshotItem(0);

                return this.nativeValue(result);
            };

        for (i = 0; i < itemsTests.length; i++) {
            var found = false;
            var item = itemsTests[i];

            for (j = 0; j < item.nodes.length; j++) {
                var nodeSet = nodeValue(item.nodes[j]);

                for (k = 0; k < nodeSet.length; k++) {
                    var node = nodeSet[k];

                    if (item.validator(node)) {
                        if (item.weight) {
                            this._totalWeight += item.weight;
                        }

                        var itemData = {
                            name: item.name,
                            node: item.nodes[j],
                            index: k + 1
                        };

                        if (item.value !== undefined) {
                            itemData.nativeValue = item.value;
                            itemData.value = valueFunction;
                        }

                        if (item.install !== undefined) {
                            itemData.install = item.install;
                        }

                        // Save the node 
                        this._validItems.push(itemData);
                        this._reportInfo("Found item - " + item.name);
                        found = true;

                        if (item.match === WebApp.match.FIRST || item.match === WebApp.match.ANY) {
                            break;
                        }
                    }
                }
                if (found) {
                    break;
                }
            }

            if (!found) {
                if (item.fragment !== undefined) {
                    var fragmentOk, resultSet, testNode = document.createElement("div");
                    testNode.innerHTML = item.fragment;
                    resultSet = document.evaluate(item.nodes[0], testNode, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
                    fragmentOk = resultSet.snapshotLength > 0 && item.validator(resultSet.snapshotItem(0));
                    this._reportWarning("Item not found " + item.name + " fragment check " + (fragmentOk ? "OK" : "failed"));
                } else {
                    this._reportWarning("Item not found: " + item.name);
                }
            }
        }

        // Should we continue?
        if (!this._appInfo.validator(this._totalWeight)) {
            if (this._shouldRetry()) {
                this._reportWarning("Did not retrieve enough information to instantiate app, will retry");
                return false;
            } else {
                this._reportFailure(this._totalWeght);
                return true;
            }
        }

        // Build Pagedata for Unity.init()
        pageData.name = this._valueFromField(this._appInfo.name);
        pageData.iconUrl = this._valueFromField(this._appInfo.iconUrl);
        pageData.homepage = this._valueFromField(this._appInfo.homepage);
        pageData.domain = this._valueFromField(this._appInfo.domain);
        pageData.login = this._login;
        pageData.onInit = function () { this._unityLoaded(); }.bind(this);

        if (this._callbacks.success !== undefined) {
            this._reportInfo("calling success callback");
            this._callbacks.success(pageData);
        }

        return true;
    },

    _unityCallback: function () {
        // Collect all values
        var indicators = [];
        var i = 0;

        for (i = 0; i < this._validItems.length; i++) {
            var item = this._validItems[i];

            if (item.value !== undefined) {
                indicators.push(item.value());
            }
        }

        return indicators;
    },

    _valueFromField: function (value) {
        // Field can either be a value or a function to compute the value
        if (typeof value === 'function') {
            return value();
        }
        return value;
    },

    _reportInfo: function (msg) {
        if (this._callbacks.report) {
            this._callbacks.report("REPORT: INFO: " + msg);
        }
    },

    _reportWarning: function (msg) {
        if (this._callbacks.report) {
            this._callbacks.report("REPORT: WARNING: " + msg);
        }
    },

    _reportError: function (msg) {
        if (this._callbacks.report) {
            this._callbacks.report("REPORT: ERROR: " + msg);
        }
    },

    _reportFailure: function (weight) {
        if (this._callbacks.report) {
            this._callbacks.report("REPORT: ERROR: Failed to pass sufficient tests to continue " + weight);
        }
    },

    _shouldRetry: function () {
        if (this._appInfo.maxRetries !== undefined) {
            return this._retries++ < this._appInfo.maxRetries;
        }
        return true;
    }
};



