/**
 * JavaScript 对象可以看作属性的集合，
 * 我们经常会检测集合中成员的所属关系——判断某个属性是否存在于某个对象中。
 * 可以用 in 运算符、hasOwnPreperty() 和 propertyIsEnumerable() 方法来完成这个工作，
 * 甚至仅通过属性查询也可以做到这一点。
 * 这节的例子都是用字符串作为属性名称，但是也可以用 Symbol 作为属性名（§6.10.3）。
 */

let o = {x: 1}
console.log("x=>", "x" in o) //  => true: o has an own property "x"
console.log("y=>", "y" in o) // => false: o doesn't have a property "y"
console.log("toString=>", "toString" in o) // => true: o inherits a toString property

/**
 * 对象的 hasOwnProperty() 方法用来检测给定的名字是否是对象的自有属性。对于继承属性它将返回 false：
 */

console.log("o hasOwnProperty x =>", o.hasOwnProperty("x")) // => true
console.log("o hasOwnProperty y =>", o.hasOwnProperty("y")) // => false
console.log("o hasOwnProperty toString=>", o.hasOwnProperty("toString")) // false: toString is an inherits property

/**
 * propertyIsEnumerable() 是 hasOwnProperty() 的增强版。
 * 只有检测到是自有属性且这个属性的可枚举性为 true 时它才返回 true。
 * 某些内置属性是不可枚举的。
 * 通常由 JavaScript 代码创建的属性都是可枚举的，除非使用 §14.1 中介绍的技术来让它们不可枚举。
 */

console.log("o has an own enumerable property x => ", o.propertyIsEnumerable("x")) // true
console.log("o has an own enumerable property toString => ", o.propertyIsEnumerable("toString")) // false not an own property
console.log("Object have an own enumerable property =>", Object.propertyIsEnumerable("toString")) // false not enumerable


/**
 * 除了使用 in 运算符之外，另一种更简便的方法是使用 !== 判断一个属性是否是 undefined：
 * ！！但不能判断对象是否含有该属性
 */

let o1 = {x: 1} // Property is explicitly set to undefined
console.log("o1 has an own property x => ", o1.x !== undefined) // true
console.log("o1 has an own property y => ", o1.y !== undefined) // false
console.log("o1 inherits a toString property => ", o1.toString !== undefined) // true

/**
 * 然而有一种场景只能使用 in 运算符而不能使用上述属性访问的方式。
 * in 可以区分不存在的属性和存在但值为 undefined 的属性。例如下面的代码：
 */

let o2 = {x:undefined}
console.log("o2.x !== undefined",o2.x !== undefined) // false
console.log("o2.y !== undefined",o2.y !== undefined) // false
console.log(" 'x' in o2 ? ","x" in o2) // true
console.log(" 'y' in o2 ?" ,"y" in o2) // false
console.log("delete o2.x =>" ,delete o2.x) //true
console.log(" 'x' in o2",'x' in o2) // false


