// ==UserScript==
// @name         innerHTML tracker
// @description  tracks innerHTML changes
// @version      2025-12-11
// @author       ptrstr
// @include      *
// @grant        none
// ==/UserScript==

(function() {
    "use strict";

    if (window.onInnerHTMLChange) {
        return;
    }

    const token = "<TOKEN>";

    const descriptor = Object.getOwnPropertyDescriptor(
        Element.prototype,
        "innerHTML"
    );

    Object.defineProperty(Element.prototype, "innerHTML", {
        get: function () {
            return descriptor.get.call(this);
        },
        set: function (value) {
            descriptor.set.call(this, value);

            window.onInnerHTMLChange(this, value);
        },
        enumerable: true,
        configurable: true,
    });

    window.onInnerHTMLChange = (element, newValue) => {
        const error = new Error();

        element.style.outline = 'dashed red 12px';
        if (newValue.toLowerCase().includes(token.toLowerCase())) {
            console.warn("innerHTML changed with token", element, newValue, error);
        } else {
            console.log("innerHTML changed", element, newValue, error);
        }
    };

    console.log("Tracking innerHTML changes with token", token);
})();