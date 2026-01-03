// ==UserScript==
// @name         URLSearchParams tracker
// @description  tracks URLSearchParams usage
// @version      2025-12-11
// @author       ptrstr
// @include      *
// @grant        none
// @run-at       document-start
// ==/UserScript==

(function () {
    "use strict";

    if (window.__urlHooked) {
        return;
    }

    window.__urlHooked = true;

    const origGet = URLSearchParams.prototype.get;
    URLSearchParams.prototype.get = function (key) {
        const error = new Error();
        console.log(`URLSearchParams.get('${key}')`, error);
        return origGet.call(this, key);
    };

    const origHas = URLSearchParams.prototype.has;
    URLSearchParams.prototype.get = function (key) {
        const error = new Error();
        console.log(`URLSearchParams.has('${key}')`, error);
        return origHas.call(this, key);
    };

    console.log("Tracking URLSearchParams");
})();
