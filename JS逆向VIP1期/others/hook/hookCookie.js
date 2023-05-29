(function () {

    'use strict';

    var cookieTemp = "";

    Object.defineProperty(document, "cookie", {

        set: function (val) {
            console.log("Hook捕获的Cookie设置值->", val)
            debugger;
            cookieTemp = val;
            return val;
        },

        get: function (val) {

            return cookieTemp

        }

    })


})()