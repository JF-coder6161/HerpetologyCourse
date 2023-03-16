/**
 * toString() 方法没有实参，它将返回一个表示调用这个方法的对象值的字符串。在需要将对象转换为字符串的时候，
 * JavaScript 都会调用这个方法。比如，当使用 + 运算符连接一个字符串和一个对象时或者在希望使用字符串的方法中使用了对象时都会调用 toString()。
 *
 * 默认的 toString() 方法的返回值带有的信息量很少（尽管它在检测对象的类型时非常有用，参照 §14.4.3）
 * ，例如，下面这行代码的计算结果为字符串”[object Object]”：
 */

let s = {
    x: 1,
    y: 1
}.toString() // s == "[object object]"
console.log(s)

/**
 * 由于默认的 toString() 方法并不会输出很多有用的信息，因此很多类都带有自定义的 toString()。
 * 例如，当数组转换为字符串的时候，结果是一个数组元素列表，只是每个元素都转换成了字符串，
 * 再比如，当函数转换为字符串的时候，得到函数的源代码。可以像下面这样自定义 toString() 方法：
 */

let point = {
    x:1,
    y:2,
    toString:function (){ return `(${this.x},${this.y})`}
}

console.log(String(point))



