/**
 * 除了基本的 toString() 方法之外，对象都包含 toLocaleString() 方法，
 * 这个方法返回一个表示这个对象的本地化字符串。Object 中默认的 toLocaleString() 方法并不做任何本地化自身的操作，
 * 它仅调用 toString() 方法并返回对应值。Date 和 Number 类对 toLocaleString() 方法做了定制，可以用它对数字、日期和时间做本地化的转换。
 * Array 类的 toLocaleString() 方法和 toString() 方法很像，唯一的不同是每个数组元素会调用 toLocaleString() 方法转换为字符串，
 * 而不是调用各自的 toString() 方法。可以像这样使用 point 对象做到同样的效果：
 */

let point ={
    x:1000,
    y:2000,
    toString:function (){return `(${this.x},${this.y})`;},
    toLocaleString:function (){
        return `(${this.x.toLocaleString()},${this.y.toLocaleString()})`
    }
}

console.log(point.toString())
console.log(point.toLocaleString())



