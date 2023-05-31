/**
 * 给Object.prototype添加一个不可枚举的extend()方法这个方法继承自调用它的对象,
 * 将作为参数传入的对象的属性一一复制参数对象的所有自有对象(包括不可枚举的属性)也会一一复制。
 * 除了值之外,也复制属性的所有特性,除非在目标对象中存在同名的属性,
 */
Object.defineProperty(Object.prototype, 'extend', {
    writable: true,
    enumerable: false,
    configurable: true,
    value: function (o) {
        var names = Object.getOwnPropertyNames(o);
        for (var i = 0; i < names.length; i++) {
            // 如果属性已经存在，则跳过
            if (names[i] in this) continue;
            // 获得o中的属性的描述符
            var desc = Object.getOwnPropertyDescriptor(o, names[i]);
            // 用它给this创建一个属性
            Object.defineProperty(this, names[i], desc)
        }
    }
});

var a = {x:2}
var c = {x:1,y:3}

a.extend(c)

console.log(a)


