
function Person(name,age){
this.name = name
this.age = age
}

Person.prototype.eat = function (){
console.log(this.name + " eating")}


p1 = new Person("yuan",22)


function eat(){
console.log(this.name + " is eating")}

eat.call(p1)  // p1赋值给eat的this
eat.apply(p1)

eat() // 普通函数的调用 内部的this指的是window对象

function add(a,b,c){
    console.log(this.name  + " is eating",a,b,c)

}

eat.call(p1,1,2,3)  // 按位置传参
eat.apply(p1,[1,2,3]) // 按数组传参

