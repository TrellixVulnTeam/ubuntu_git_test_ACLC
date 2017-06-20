function doMainMenuIntegration(doc) {
    function evalInPageContext(func) {
        var script = document.createElement('script');
        script.appendChild(document.createTextNode('(' + func + ')();'));
        (document.body || document.head || document.documentElement).appendChild(script);
    }

    function makeRedirector(link) {
        return function () {
            evalInPageContext('function() {window.location = "' + link + '";}');
        };
    }
    var i, k;
    // explore main menu
    //document.getElementById('canvas_frame').contentDocument;
    var snapshot = doc.evaluate('//div[@id="gbz"]/ol[@class="gbtc"]/li',
                                doc, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);

    for (i = 0; i < snapshot.snapshotLength; i++) {
        var node = snapshot.snapshotItem(i);
        var link = node.firstChild.href;
        var text = node.firstChild.lastChild.textContent;

        Unity.addAction('/' + text, makeRedirector(link));
        console.log(text);
        //submenu
        var snapshot2 = doc.evaluate('div[@id="gbd"]/div/ol/li',
                                     node, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null);
        if (snapshot2) {
            for (k = 0; k < snapshot2.snapshotLength; k++) {
                var childNode = snapshot2.snapshotItem(k);
                if (childNode.textContent !== '') {
                    console.log(childNode.textContent);
                    Unity.addAction('/' + text + '/' + childNode.textContent, makeRedirector(childNode.firstChild.href));
                }
            }
        }
    }
}
