
function validatedNodes(nodeInfo) {
    var resultSet = document.evaluate(nodeInfo.query,
                                      document,
                                      null,
                                      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                      null);
    if (resultSet.snapshotLength === 0) {
        reportTestState("REPORT: ERROR: Failed to find any nodes for " + nodeInfo.name);
        return [];
    }

    var i, arrayized = [];
    for (i = 0; i < resultSet.snapshotLength; i++) {
        arrayized.push(resultSet.snapshotItem(i));
    }

    if (nodeInfo.validator === undefined) {
        return arrayized;
    }

    if (!nodeInfo.validator(arrayized)) {
        if (nodeInfo.fragment === undefined) {
            reportTestState("REPORT: ERROR: Failed to validate node " + nodeInfo.name);
            return null;
        }

        var testNode = document.createElement("div");
        testNode.innerHTML = nodeInfo.fragment;
        resultSet = document.evaluate(nodeInfo.query, testNode, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        var fragmentOk = resultSet.snapshotLength > 0 && nodeInfo.validator(resultSet.snapshotItem(0));
        reportTestState("REPORT: ERROR: Failed to validate node " + nodeInfo.name + " fragment check " + (fragmentOk ? "OK" : "failed"));
        return null;
    }

    return arrayized;
}

function validatedNode(nodeInfo) {
    var resultSet = document.evaluate(nodeInfo.query,
                                      document,
                                      null,
                                      XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,
                                      null);
    if (resultSet.snapshotLength === 0) {
        reportTestState("REPORT: ERROR: Failed to find any nodes for " + nodeInfo.name);
        return null;
    }

    var item = resultSet.snapshotItem(0);

    if (nodeInfo.validator === undefined) {
        return item;
    }

    if (!nodeInfo.validator(resultSet.snapshotItem(0))) {
        // Validation failed, check the fragment
        if (nodeInfo.fragment === undefined) {
            reportTestState("REPORT: ERROR: Failed to validate node " + nodeInfo.name);
            return null;
        }

        var testNode = document.createElement("div");
        testNode.innerHTML = nodeInfo.fragment;
        resultSet = document.evaluate(nodeInfo.query, testNode, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        var fragmentOk = resultSet.snapshotLength > 0 && nodeInfo.validator(resultSet.snapshotItem(0));
        reportTestState("REPORT: ERROR: Failed to validate node " + nodeInfo.name + " fragment check " + (fragmentOk ? "OK" : "failed"));
        return null;
    }

    return item;
}

function validatedNodeValue(nodeInfo, node) {
    if (nodeInfo.value === undefined) {
        throw new Error("Attempt to retrieve node value without a value probing function");
    }
    return nodeInfo.value(node === undefined ? validatedNode(nodeInfo) : node);
}

