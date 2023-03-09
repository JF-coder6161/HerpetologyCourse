/**
 * 原型对象
 * 每一个 JavaScript 对象都和另一个对象相关联。“另一个”对象就是我们熟知的原型，
 * 每一个对象都从原型继承属性。
 *
 * 所有通过对象字面量创建的对象都具有同一个原型对象，并可以通过 JavaScript 代码 Object.prototype
 * 获得对原型对象的引用。通过关键字 new 和构造函数调用创建的对象的原型就是构造函数的 prototype 属性的值。
 * 因此，同使用 {} 创建对象一样，通过 new Object() 创建的对象也继承自Object.prototype。
 * 同样，通过 new Array() 创建的对象的原型就是 Array.prototype，通过 new Date() 创建的对象的原型就是 Date.prototype。
 * 当第一次学习 JavaScript 时，这可能令人困惑。请记住：几乎所有对象都有原型，
 * 但只有相对较少的对象具有原型属性。正是这些具有原型属性的对象定义了所有其他对象的原型。
 *
 * 没有原型的对象为数不多，Object.prototype就是其中之一：它不继承任何属性。
 * 其他原型对象都是普通对象，普通对象都具有原型。
 * 大部分的内置构造函数（以及大部分自定义的构造函数）都具有一个继承自 Object.prototype 的原型。
 * 例如， Date.prototype 的属性继承自 Object.prototype，
 * 因此由 new Date() 创建的 Date 对象的属性同时继承自 Date.prototype 和 Object.prototype。
 * 这一系列链接的原型对象就是所谓 “原型链”（prototype chain）。
 *
 * §6.3.2 节讲述属性继承的工作机制。
 * 第 9 章将会更详细地讨论原型和构造函数：包括如何通过编写构造函数定义对象的“类”，
 * 以及给构造函数的 prototype 属性赋值可以让其“实例”直接使用这个原型上的属性和方法。
 * 并且在 §14.3 我们会学习如何查询（甚至改变）对象的原型。
 */


