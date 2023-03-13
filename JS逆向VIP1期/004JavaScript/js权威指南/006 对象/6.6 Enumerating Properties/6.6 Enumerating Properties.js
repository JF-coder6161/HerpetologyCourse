/**
 * 除了检测对象的属性是否存在，我们还会经常遍历对象的属性。有几种不同的方法可以做到这一点。
 * §5.4.5 讨论过 for/in 循环，其可以在循环体中遍历指定对象中所有可枚举的属性（包括自有属性和继承的属性），
 * 把属性名称赋值给循环变量。对象继承的内置方法不可枚举的，但在代码中给对象添加的属性都是可枚举的
 * （除非用下文中提到的一个方法将它们转换为不可枚举的）。
 */

let o = {
    x:1,
    y:2,
    z:3,
    f2 : function(){ }
}

o2 = Object.create(o)
o2.a = 4;
o2.b = 5;
o2.c = 6;
o2.fun1 = function (){ }
console.log(o.propertyIsEnumerable("toString")) // false
for (let p  in o2){ // Loop through the properties
    console.log(p) //  Prints a,b,c,x,y,z , but not toString
}

/**
 * 为了防止 for/in 枚举到继承属性，可以在循环中添加显示检查：
 */

for (const p in o2) {

    if(!o2.hasOwnProperty(p)) continue  // skip o2 inherits property
    if(typeof o2[p] === "function") continue // skip all methods
    console.log("o2 own property(except inherits) => ",p) // Prints a , b , c

}

/**
 * Object.keys() 返回对象的可枚举自有属性名称数组集合。
 * 数组内不包含不可枚举属性、继承属性或属性名称是 Symbol（见 §6.10.3）的属性
 */
console.log("Objects.keys() iterable =>",Object.keys(o2)) // ['a', 'b', 'c', 'fun1']

/**
 * Object.getOwnPropertyNames() 用起来和 Object.keys() 类似，
 * 但是它返回数组中也包含不可迭代的自有属性，只要它们的名称是字符串。
 */

console.log("Object.getOwnPropertyNames() iterable =>" ,Object.getOwnPropertyNames(o2)) // ['a', 'b', 'c', 'fun1']

/**
 * Object.getOwnPropertySymbols() 返回名称是 Symbol 的自有属性，无论它们是否可枚举。
 */


/**
 * Reflect.ownKeys() 返回所有的自由属性名称，包括可枚举和不可枚举类型，也包括字符串和 Symbol（见 §14.6）。
 */