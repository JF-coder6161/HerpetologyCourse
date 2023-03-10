/**
 * JavaScript 对象都是关联数组
 *
 * 对象在程序中可以创建任意数量的属性。当使用 . 运算符访问对象的属性时，属性名用一个标识符来表示。
 * 标识符必须直接出现在 JavaScript 程序中，它们不是数据类型，所以无法在程序中修改。
 *
 * JavaScript 对象通常用作关联数组，理解其工作原理非常重要。
 * 但是，在 ES6 之后使用 Map 类常常是一个更好的选择，我们将在 §11.1.2 中进行描述。
 */

console.log(Object.prototype)
console.log(Object["property"]) // 标识符无法在程序中修改

customer = {
    "address0": "China",
    "address1": "America",
    "address2": "Spanish"
}

let addr = "";
for (let i = 0; i < 3; i++) {
    addr += customer[`address${i}`] + "\n"
}
console.log("addr",addr)


function addstock(portfolio,stockname,shares){
    portfolio[stockname] = shares; // 字符串值是动态的，可以在运行时候更改
}

/**
 * 当使用 for/in 循环遍历关联数组时，就可以清晰地体会到 for/in 的强大之处。
 * @param portfolio
 * @returns {number}
 */

function computeValue(portfolio){
    let total = 0.0;
    for (const stock in portfolio) {   // For each stock in the portfolio
        let shares = portfolio[stock] // get the number of shares
        let price =  getQuote(stock); // look up share price
        total += shares * price;      // add stock value to total value
    }
    return total;                   // Return total value.
}

portfolio = {
    "IBM":50,
    "Apple":60,
    "AWS":50,
    "HuaWei":40
}





