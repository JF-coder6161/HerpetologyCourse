/**
 * 每一个对象都有与之相关的
 * 1.原型(prototype)
 * 2.类 (class)
 * 3.可扩展性 (extensible attribute)
 *
 */

// 检测一个对象是否是另一个对象的原型(或处于原型链中)

var p = {x: 1}
var o = Object.create(p);

console.log(p.isPrototypeOf(o)) // true
Object.prototype.isPrototypeOf(o) // true

/**
 * 类属性： 是一个字符串,用以表示对象的类型信息
 * 默认的toString方法可以查询它，（Object.prototype）
 * 未提供设置这个属性的方法
 */

// classof()函数可以返回传递给它的任意对象类
function classof(o) {
    if (o === null) return "Null";
    if (o === undefined) return "Undefined";
    return Object.prototype.toString.call(o).slice(8, -1)
}

console.log(classof(o)) // =>Object
console.log(classof(1)) // => Number


