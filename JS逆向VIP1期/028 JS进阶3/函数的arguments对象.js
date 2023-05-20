

function foo(x,y,z){
    console.log(x,y)
}


add(1,2)

// arguments 可变参数
function add(){
    console.log("arguments:",arguments)

    var ret = 0;
    for(int i = 0 ; i < arguments.length();i++){
        console.log(arguments[i])
        ret += arguments[i]
    }
    return ret;
}





