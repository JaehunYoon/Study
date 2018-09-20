var arr = [4, 15, 377, 395, 400, 1024, 3000];
var temp = arr.filter(function (n)
{
    return n % 5 == 0;
});

console.log(temp);