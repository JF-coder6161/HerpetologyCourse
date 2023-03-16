/**
 * Object.prototype 实际上没有定义 toJSON() 方法，但对于需要执行序列化的对象来说，
 * JSON.stringify() 方法（见 §6.8）会调用 toJSON() 方法。如果在待序列化的对象中存在这个方法
 * 则调用它，返回值即是序列化的结果，而不是原始的对象。Date 类（§11.4）定义了 toJSON() 方法
 * 返回日期的序列化字符串。我们可以这样对 point 对象做同样的事：
 */

let point = {
    x: 1,
    y: 2,
    toString: function () {
        return `(${this.x},${this.y})`;
    },
    toJson: function () {
        return this.toString();
    }
}

console.log(JSON.stringify([point]))

let point1 = [{
    x: 1,
    y: 2,
    z: "3"
}]

console.log(JSON.stringify(point1, function (k,v){
    if(typeof v === "string"){
        return undefined
    }
    return v
}))

