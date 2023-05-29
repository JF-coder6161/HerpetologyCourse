
let code = function(){
var open = window.XMLHttpRequest.prototype.open;
window.XMLHttpRequest.prototype.open = function (method, url, async){
    console.log("Hook获取的RequestUrl::" , url)
    if (url.indexOf("customized")>-1){
        debugger;
    }
    return open.apply(this, arguments);
};
}
let script = document.createElement('script');
script.textContent = '(' + code + ')()';
(document.head||document.documentElement).appendChild(script);
script.parentNode.removeChild(script);
