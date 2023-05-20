const CryptoJS = require('F:\\PyCharmProject\\HerpetologyCourse\\JS逆向VIP1期\\031 JS逆向案例1\\dependence\\node_modules\\crypto-js')

const d = "fanyideskweb"
    , u = "webfanyi"
    , m = "client,mysticTime,product"
    , p = "1.0.0"
    , b = "web"
    , f = "fanyi.web";

function g(e) {
    return r.a.createHash("md5").update(e).digest()
}

function v(e) {
    return CryptoJS.MD5(e).toString()
}

function h(e, t) {
    return v(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function getRquestParamForDecodeData(e) {
    const t = (new Date).getTime();
    return {
        sign: h(t, e),
        client: d,
        product: u,
        appVersion: p,
        vendor: b,
        pointParam: m,
        mysticTime: t,
        keyfrom: f
    }
}


// ret = getRquestParamForDecodeData('fsdsogkndfokasodnaso');
// console.log(ret)
// var rett = CryptoJS.MD5('1234').toString()
// console.log(rett)