/**
 * 删除运算符（§4.13.4）能删除对象中的属性。它的操作数应当是一个属性访问表达式。
 * 令人意外的是，delete 没有操作属性的值，而是操作属性的属性：
 */

let book = {
    "main title": "JavaScript",          // These property names include spaces,
    "sub-title": "The Definitive Guide", // and hyphens, so use string literals.
    for: "all audiences",                // for is reserved, but no quotes.
    author: {                            // The value of this property is
        firstname: "David",              // itself an object.
        surname: "Flanagan"
    }
};

delete book.author; // The book object now has no author property
delete book["main title"] // Now it doesn't have "main title",either
/**
 * delete 运算符只删除自有属性，不删除继承属性。
 * （想要删除一个继承属性，必须从定义这个属性的原型对象上删除它。这会影响所有继承这个原型的对象。）
 */
console.log(book)

let o = {x:1}; // o has own property x and inherits property toString
delete o.x; // => true: deletes property x
delete o.x; // => true: does nothing (x doesn't exist) but true anyway
delete o.toString(); // => true: does nothing (toString isn't an own property)
delete 1; // => true: nonsense, but true anyway

/**
 * delete 不能删除那些可配置性为 false 的属性。
 * 某些内置对象的属性是不可配置的，比如通过变量声明和函数声明创建的全局对象的属性。
 * 在严格模式中，删除一个不可配置属性会报一个类型错误。
 * 在非严格模式中，在这些情况下的 delete 操作会返回 false：
 */

// In strict mode , all these deletions throw TypeError instead of returning false
delete Object.prototype // => false: property is non-configurable
var x = 1; // Declare a global variable
delete globalThis.x // => false: can't delete this property
console.log(delete globalThis.x)
function f(){} // Declare a global function
delete globalThis.f // => false can't delete this property either

/**
 * 当在非严格模式中删除全局对象的可配值属性时，可以省略对全局对象的引用，
 * 直接在 delete 操作符后跟随要删除的属性名即可：
 */

globalThis.y = 1; // Create a configurable global property (no let or var)
console.log(delete y) // => true this property can be deleted

/**
 * 然而在严格模式中，delete 后跟随一个非法的操作数（比如 x），则会报一个语法错误，因此必须显式指定对象及其属性：
 */

console.log(delete z) // => true SyntaxError in strict mode
console.log(delete globalThis.z) // =>true  This works




