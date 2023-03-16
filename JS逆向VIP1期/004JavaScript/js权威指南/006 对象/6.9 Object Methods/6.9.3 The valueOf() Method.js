/**
 * valueOf() 方法和 toString() 方法非常类似，但往往当 JavaScript 需要将对象转换为某种原始值
 * 而非字符串的时候才会调用它，尤其是转换为数字的时候。如果在需要使用原始值的上下文中使用了对象，
 * JavaScript 就会自动调用这个方法。默认的 valueOf() 方法不足为奇，但有些内置类自定义了 valueOf() 方法.
 * Date 类定义 valueOf() 将日期转化成数值型，并且这允许 Date 对象使用 < 和 > 按时间先手顺序比较。
 * 可以对 point 对象做同样的事，定义一个 valueOf() 方法返回原点到点的距离：
 */

let point = {
    x : 3,
    y: 4,
    valueOf: function (){return Math.hypot(this.x,this.y)}
}

Number(point) // => 5: valueOf() is used for conversions to numbers  how to run ?

console.log(point > 4 )
console.log(point > 5 )
console.log(point < 6 )
