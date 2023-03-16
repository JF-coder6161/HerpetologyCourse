/**
 * 对象序列化（serialization）是指将对象的状态转换为字符串，也可将字符串还原为对象。
 * 函数 JSON.stringify() 和 JSON.parse() 用来序列化和还原 JavaScript 对象。
 * 这些方法都使用 JSON 作为数据交换格式，JSON 的全称是“JavaScript Object Notation”
 * ——JavaScript 对象表示法，它的语法和 JavaScript 对象与数组字面量的语法非常相近：
 */

let o = {x: 1, y: {z: [false, null, ""]}} // Define a test object
let s = JSON.stringify(0) // 序列化
let p = JSON.parse(s)          // 反序列化

/**
 * JSON 的语法是 JavaScript 语法的子集，它并不能表示 JavaScript 里的所有值。
 * 支持对象、数组、字符串、无穷大数字、true、false 和 null，并且它们可以序列化和还原。
 * NaN、Infinity 和 -Infinity 序列化的结果是 null，日期对象序列化的结果是 ISO 格式的日期字符串（参照 Date.toJSON() 函数），
 * 但 JSON.parse() 依然保留它们的字符串形态，而不会将它们还原为原始日期对象。
 * 函数、RegExp、Error 对象和 undefined 值不能序列化和还原。
 * JSON.stringify() 只能序列化对象可枚举的自有属性。
 * 对于一个不能序列化的属性来说，在序列化后的输出字符串中会将这个属性省略掉。
 * JSON.stringify() 和 JSON.parse() 都可以接收第二个可选实参，
 * 通过传入需要序列化或还原的属性列表来定制自定义的序列化或还原操作。§11.6 有关于这些函数的详细文档。
 */

