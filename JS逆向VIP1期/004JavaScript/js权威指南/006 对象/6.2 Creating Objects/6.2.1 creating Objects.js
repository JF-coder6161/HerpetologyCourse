/*
1.对象可以用对象字面量创建，也可以用 new 关键字和 Object.create() 函数来创建。接下来的几部分对这些技术一一讲述。
*/

// --------------------

let empty = {}; // An object with no properties
let point = {   // Two numeric properties
    x: 0,
    y: 0
}
let p2 = {
    x: point.x,
    y: point.y,
}

let book = {
    "main title" : "Java Script",         // These property names include spaces,
    "sub-title" : "The Definitive Guide", // and hyphens, so use string literals
    for : "all audiences",              // for is reserved, but no quotes
    author : {                          // The value of this property is
        firstname : "David",            // itself an object
        surname : "Flanagan",
    }
}

console.log(book["for"]) // all audiences
console.log(book.for) // all audiences
console.log(book.author.firstname) // David

