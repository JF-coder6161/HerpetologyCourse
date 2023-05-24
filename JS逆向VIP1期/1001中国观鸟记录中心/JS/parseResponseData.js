CryptoJS = require("./node_modules/crypto-js/crypto-js")


var f = function () {
    this.url = 'www.birdreport.cn';
    this.key = '3583ec0257e2f4c8195eec7410ff1619';
    this.iv = 'd93c0d5ec6352f20'
};
f.prototype.aes_encode = function (a) {
    if (e.location.href.indexOf(this.url) != -1) {
        var b = CryptoJS.enc.Utf8.parse(this.key);
        var c = CryptoJS.enc.Utf8.parse(this.iv);
        var a = CryptoJS.AES.encrypt(a, b, {
            iv: c,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return a
    } else {
        return ''
    }
}
;
f.prototype.aes_decode = function (a) {
    if (e.location.href.indexOf(this.url) != -1) {
        var b = CryptoJS.enc.Utf8.parse(this.key);
        var c = CryptoJS.enc.Utf8.parse(this.iv);
        var d = CryptoJS.AES.decrypt(a, b, {
            iv: c,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return d.toString(CryptoJS.enc.Utf8)
    } else {
        return ''
    }
}
;
f.prototype.decode = function (a) {
    var b = CryptoJS.enc.Utf8.parse(this.key);
    var c = CryptoJS.enc.Utf8.parse(this.iv);
    var d = CryptoJS.AES.decrypt(a, b, {
        iv: c,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return d.toString(CryptoJS.enc.Utf8)
}
;


function getParseData(data){
    var parse = new f()
    return JSON.stringify(parse.decode(data))
}
