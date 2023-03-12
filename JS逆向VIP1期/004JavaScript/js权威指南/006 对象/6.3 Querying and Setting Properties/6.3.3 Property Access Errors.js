/**
 * 属性访问表达式并不总是返回或设置一个值。本节讲述查询或设置属性时的一些出错情况。
 *
 */

let book = {
    "main title": "JavaScript",          // These property names include spaces,
    "sub-title": "The Definitive Guide", // and hyphens, so use string literals.
    for: "all audiences",                // for is reserved, but no quotes.
    author: {                            // The value of this property is
        firstname: "David",              // itself an object.
        surname1: "Flanagan"
    }
};

/**
 * 查询一个不存在的属性并不会报错，如果在对象 o 自身的属性或继承的属性中均未找到属性 x，
 * 属性访问表达式 o.x 返回 undefined。
 * 回想一下我们的 book 对象有属性“sub-title”，而没有属性“subtitle”：
 */

book.subtitle // => undefined: property doesn't exist

/**
 * 但是，如果对象不存在，那么试图查询这个不存在的对象的属性就会报错。
 * null 和 undefined 值都没有属性，因此查询这些值的属性会报错，接上例：
 */

//book.subtitle.length; // !TypeError: undefined doesn't have length

/**
 * 如果 . 的左边是 null 或 undefined 时，其属性表达式会失败。
 * 所以当写一个像 book.author.surname 一样的表达式时，
 * 如果你不确定 book 和 book.author 确实被定义就要小心了。下面提供了两种避免出错的方法：
 */

// A verbose and explicit technique
let surname = undefined
if(book){
    if(book.author){
        surname = book.author.surname;
    }
}

// A concise and idiomatic alternative to get surname or null or undefined
surname = book && book.author && book.author.surname
console.log(surname)

// ES2020 支持用 ？. 条件属性访问 可以重写上面的表达式
surname = book?.author?.surname;

/**
 * 当然，给 null 和 undefined 设置属性也会报类型错误。
 * 给其他值设置属性也不总是成功，有一些属性是只读的，不能重新赋值，有一些对象不允许新增属性。
 * 在严格模式下（§5.6.3），属性设定失败时会抛出 TypeError 异常。
 * 在非严格模式下，这些失败的处理经常没有任何反应。
 */

/**
 * 尽管属性赋值成功或失败的规律看起来很简单，但要描述清楚并不容易。在这些场景下给对象 o 设置属性 p 会失败：
 *
 * 1.o 中的属性 p 是只读的：不能给只读属性重新赋值。
 * 2.o 中的属性 p 是继承属性，且它是只读的：不能通过同名自有属性覆盖只读的继承属性。
 * 3.o 中不存在自有属性 p;
 *   o 没有使用 setter 方法继承属性 p，并且o的可扩展性是（见 §14.2）false。
 *   如果 o 中不存在 p，而且没有 setter 方法可供调用，则 p 一定会添加至 o 中。
 *   但如果 o 不是可扩展的，那么在 o 中不能定义新属性。
 */

