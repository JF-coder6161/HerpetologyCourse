// 属性的特性
/**
 *  除了包含名字和值之外，属性还包含一些标识它们可写、可枚举和可配置的特性。
 *  tips: 我们将存取器属性的getter和setter方法看成是属性的特性，按照这个逻辑，我们也可以
 *  把数据属性的值同样看做属性的特性。因此，可以认为一个属性包含一个名字和4个特性。
 *  1.数据属性的4个特性分别是它的值(value)、可写性(writable)、可枚举性(enumerable)和可配置性(configurable)
 *  2.存取器属性不具有值(value)特性和可写性，它们的可写性是由setter方法存在与否决定的。
 *  因此，存取器属性的4个特性是读取(get)、写入(set)、可枚举性和可配置性
 *  为了实现属性特性的查询和设置操作，ECMASeript 5中定义了一个名为“属性描述符”(property descriptor)的对象
 *  ,这个对象代表那4个特性。
 *  描述符对象的属性和它们所描述的属性特性是同名的。因此，
 *  数据属性的描述符对象的属性有value、writable、enumerable和configurable。
 *  存取器属性的描述符对象则用get属性和set属性代替value和writable。
 *  其中writable，enumerable和configurable都是布尔值，
 *  当然，get属性和set属性是函数值。
 *
 *  Object.defineProperty()
 *  Object.defineProperties()
 *  使用规则：
 *  如果对象是不可扩展的，则可以编辑已有的自有属性，但不能给它添加新属性。
 *  如果属性是不可配置的，则不能修改它的可配置性和可枚举性。
 *  如果存取器属性是不可配置的,则不能修改其getter和setter方法,也不能将它转换为数据属性。
 *  如果数据属性是不可配置的,则不能将它转换为存取器属性。
 *  如果数据属性是不可配置的,则不能将它的可写性从false修改为true,但可以从true修改为false。
 *  如果数据属性是不可配置且不可写的,则不能修改它的值。
 *  然而可配置但不可写属性的值是可以修改的(实际上是先将它标记为可写的,然后修改它的值,最后转换为不可写的）。
 */

//定义存取器属性


// var o = {
//     // 普通的数据属性
//     data_prop: value,
//     // 存取器属性
//     get accessor_prop() {
//     },
//     set accessor_prop(value) {
//     }
// }


var random1 = {
    get octet() {
        return Math.floor(Math.random() * 256)
    }
}

console.log(random1.octet)  // 196

// 数据属性的描述符对象的属性有value(get)、writable(set)、enumerable 和 configurable

Object.getOwnPropertyDescriptor({x: 1}, "x");

console.log(Object.getOwnPropertyDescriptor({x: 1}, "x"))
//{ value: 1, writable: true, enumerable: true, configurable: true }


console.log(Object.getOwnPropertyDescriptor(random1, "octet"))

// 对于继承属性和不存在的属性，返回undefined
console.log(Object.getOwnPropertyDescriptor({}, "x"))  // undefined 没有这个属性

console.log(Object.getOwnPropertyDescriptor({}, "toString")) // undefined 继承属性

// 设置属性的特性

var o = {}

// 添加一个不可枚举的数据属性 x，并赋值为 1
Object.defineProperty(o,"x",{
    value:1,
    writable:true,
    enumerable:false,
    configurable:true
})

// 属性是存在的，但不可枚举
console.log(o.x) // 1
console.log(Object.keys(o))  // []

Object.defineProperty(o,'x',{
    writable:false
})

o.x = 2;
console.log(o.x) // => 1

// 可以通过这种方法更改属性值（writable:false）
Object.defineProperty(o,'x',{value:2})

console.log(o.x) // => 2

// 将数据属性修改为存取器属性
Object.defineProperty(o,'x',{
    get:function (){
        return o
    }
})

console.log(o.x)









