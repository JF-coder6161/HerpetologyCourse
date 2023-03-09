// Object.create() 创建一个新对象，用第一个实参作为它的原型
let o1 = Object.create({ // o1 inherits properties x and y
    x: 1,
    y: 2,
})

o1.x + o1.y  // => 3

console.log(o1)

/**
 * 可以通过传入参数 null 来创建一个没有原型的新对象，但通过这种方式创建的对象不会继承任何东西，
 * 甚至不包括基础方法，比如 toString()，也就是说，它将不能和“+”运算符一起正常工作：
 */

let o2 = Object.create(null) // o2 inherits no props or methods

console.log(o2)

/**
 * 如果想创建一个普通的空对象（像通过 {} 或 new Object() 创建的对象），需要传入 Object.prototype：
 */

let o3 = new Object(Object.prototype); // o3 is like {} or new Object()

console.log(o3)

/**
 * 可以通过任意原型创建新对象，这是一个强大的特性，并且本章我们会在很多地方使用 Object.create()。
 * （Object.create() 也可以传入第二个可选实参来描述这个新的对象的属性。第二个实参是一个高级特性，在 §14.1 再进行描述。）
 *
 * Object.create() 其中一个用途是预防对象无意间（非恶意地）被无法支配的库函数篡改。
 * 可以创建一个继承它的对象来传递给函数，而不是将其直接传递给函数。当函数读取继承对象的属性时，实际上读取的是继承来的值。如果给继承对象的属性赋值，则这些属性只会影响这个继承对象自身，而不是原始对象：
 */

let o = {x: "don't change this value"};
let o4 = Object.create(o);
o4.x = "change value"
p(o4); // Guard against accidental modifications
console.log(o)
function p(x) {
    console.log(x)
}
