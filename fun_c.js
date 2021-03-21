
function test_func(name) {
    console.log(name)
    return name
}

function tihs_test(name) {
    console.log('这是另一个函数的输出:' + name)
    return name
}


module.exports = {
    test_func,
    tihs_test
}