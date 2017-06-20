// ==UserScript==
// @include        http://www.amazon.*/*
// @require        utils.js
// ==/UserScript==

window.Unity = external.getUnityObject(1);

function unityLoaded() {
    function addAction(name, uri) {
        var fullUri = 'http://' + window.location.hostname + '/' + uri;

        Unity.Launcher.addAction(name, makeRedirector(fullUri));
    }
    addAction(_("Basket"), 'gp/cart/view.html');
    addAction(_("Wishlist"), 'gp/registry/wishlist/');
    addAction(_("Orders"), 'gp/css/history/orders/view.html');
    addAction(_("Manage your Kindle"), 'gp/digital/fiona/manage');

    var buyButton = document.getElementById('buyButton');
    if (buyButton) {
        Unity.addAction('/1-Action order', function () { click(buyButton); });
    }

    var addToWishList = document.evaluate('//input[@name="submit.add-to-registry.wishlist"]', document, null, XPathResult.ANY_UNORDERED_NODE_TYPE, null).singleNodeValue;
    if (addToWishList) {
        Unity.addAction('/Add to Wish List', function () { click(addToWishList); });
    }

    var showSimilar = document.evaluate('//div[@id="vtpsims"]/div/b/a', document, null, XPathResult.ANY_UNORDERED_NODE_TYPE, null).singleNodeValue;
    if (showSimilar) {
        Unity.addAction('/Show similar', function () { click(showSimilar); });
    }
}

Unity.init({ name: "Amazon",
	     domains: [ ['amazon.com', 'http://www.amazon.com/'],
			['amazon.co.uk', 'http://www.amazon.co.uk/'],
			['amazon.co.jp', 'http://www.amazon.co.jp/'],
			['amazon.com.mx', 'http://www.amazon.com.mx/'],
			['amazon.ca', 'http://www.amazon.ca/'],
			['amazon.cn', 'http://www.amazon.cn/'],
			['amazon.fr', 'http://www.amazon.fr/'],
			['amazon.es', 'http://www.amazon.es/'],
			['amazon.it', 'http://www.amazon.it/'],
			['amazon.de', 'http://www.amazon.de/'] ],
             iconUrl: "icon://amazon-store",
             onInit: wrapCallback(unityLoaded) });

