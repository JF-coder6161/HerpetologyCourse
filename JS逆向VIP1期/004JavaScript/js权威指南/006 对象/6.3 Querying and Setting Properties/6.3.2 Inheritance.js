/**
 * JavaScript 对象中有一组“自有属性”，也有一组属性是继承自它的原型对象。
 *
 * 假设要查询对象 o 的属性 x。如果 o 中不存在 x 名称的自由属性，那么将会继续在 o 的原型对象中查询属性 x。
 * 如果原型对象中也没有 x，但这个原型对象也有原型，那么继续在这个原型对象的原型上执行查询，
 * 直到找到 x 或者查找到一个原型是 null 的对象为止。
 * 可以看到，对象的原型属性构成了一个“链”，通过这个“链”可以实现属性的继承。
 */


let o = {}; // o inherits object methods from Object.prototype
o.x = 1;   // and it now has an own property x.
let p = Object.create(o) // p inherits properties from o and Object.prototype
p.y = 2; // and has an own properties y
let q = Object.create(p); // q inherits properties from p and o  and Object.prototype
q.z = 3; // ... Object.prototype and has an own property z.
let f = q.toString(); // toString is inherited from Object.prototype
q.x + q.y // ==> 3 ; x and y are inherited from o and p

/**
 * 现在假设给对象 o 的属性 x 赋值，如果 o 中已经有属性 x（这个属性不是继承来的），
 * 那么这个赋值操作只改变这个已有属性 x 的值。否则，赋值操作给 o 添加一个新属性 x。
 * 如果之前 o 继承自属性 x，那么这个继承的属性就被新创建的同名属性覆盖了。
 */

/**
 * 属性赋值操作检查原型链只是判断是否允许赋值操作。
 * 例如，如果 o 继承自一个只读属性 x，那么赋值操作是不允许的（§6.3.3 将对此进行详细讨论）。
 * 如果允许属性赋值操作，它也总是在原始对象上创建属性或对已有的属性赋值，而不会去修改原型链。
 * 在 JavaScript 中，只有在查询属性时才会体会到继承的存在，而设置属性则和继承无关，
 * 这是 JavaScript 的一个重要特性，该特性让程序员可以有选择地重写继承的属性。
 */

let unitcircle = {r: 1};      // An object to inherit from
let c = Object.create(unitcircle); // c inherits the property r
c.x = 1; c.y =1;            // c defines two properties of its own
c.r = 2                     // c overrides its inherited property
console.log("c.r = ",c.r)  // ==> 2
console.log("unitcircle_value",unitcircle.r) // => 1: the prototype is not affected

/**
 *
 *
 */




