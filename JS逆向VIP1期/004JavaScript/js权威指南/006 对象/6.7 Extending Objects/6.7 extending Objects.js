/**
 * 在 JavaScript 代码中有一个很常见的操作，需要将一个对象中的属性拷贝到另外一个对象。以下面的代码很容易实现：
 */

let target = {x: 1}, source = {y: 2, z: 3}

for (let key of Object.keys(source)) {
    target[key] = source[key];
}

console.log(target) // target => {x:1,y:2,z:3}

/**
 * 但是因为这个是个常用的操作，各种 JavaScript 框架定义公用函数，经常将其命名为 extend()
 * 来执行这个拷贝操作。最后在 ES6 中，这个功能以 Object.assign() 的形式被添加到 JavaScript 核心语言中。
 *
 * Object.assign() 需要两个或多个对象作为其实参。它修改并返回第一个实参，即目标对象，
 * 但不会改变第二个或任何后续参数，这些参数是源对象。对于每个源对象，它将该对象的可枚举自有属性
 * （包括名称为 Symbol 的属性）复制到目标对象中。它按源对象在实参列表顺序中的顺序处理，
 * 所以第一个源对象中的属性会重写在目标对象中的同名属性，
 * 然后以第二个源对象中的同名属性（如果有第二个源对象）再次重写第一个源对象重写后的属性。
 *
 * Object.assign() 通过普通属性的 get 和 set 操作复制属性，
 * 因此，如果源对象具有 getter 方法或目标对象具有 setter 方法，
 * 则将在复制期间调用它们，但不会复制方法本身。
 */

defaults = {
    a: 1,
    b: 2,
    c: 'c',
    book: "my all"
}

o = {
    autor: "jack",
    book: "The magic world"
}


Object.assign(o, defaults)
console.log(o) // overwrites everything in o with defaults  {autor: 'jack', book: 'my all', a: 1, b: 2, c: 'c'}

o1 = {
    autor: "jack",
    book: "The magic world"
}

o2 = Object.assign({}, defaults, o1)
//o2 的属性重写defaults中的属性：
console.log(o2) // overwrites {a: 1, b: 2, c: 'c', book: 'The magic world', autor: 'jack'}

/**
 * 我们会在 §6.10.4 见到，可以用 ... 展开操作符如下操作这个对象拷贝并重写：
 */

a1 = {
    a: 1,
    b: 2,
    c: 3
}

a2 = {
    a: 4,
    b: 5,
    c: 6,
    d: 7,
}

a3 = {...a1, ...a2}
console.log(a3) // {a: 4, b: 5, c: 6, d: 7}

/**
 * 为了避免对象创建和复制的额外开销，我们还可以通过编写一个 Object.assign() 仅在缺少属性时复制属性：
 */

function merge(target, ...sources) {
    for (let source of sources) {
        for (let key of Object.keys(source)) {
            if (!(key in target)) {
                target[key] = source[key]
            }
        }
    }
    return target;
}

console.log(Object.assign({x: 1}, {x: 2, y: 2}, {y: 3, z: 4})) // => {x:2 , y:3 , z:4}
console.log(merge({x: 1}, {x: 2, y: 2}, {y: 3, z: 4})) // {x: 1, y: 2, z: 4}


