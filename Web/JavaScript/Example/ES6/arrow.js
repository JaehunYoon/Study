var temps = ['Apple', 'Banana', 'Carrot', 'Dragon'];

var tempsLength1 = temps.map(function(temp) {return temp.length;});

var tempsLength2 = temps.map((temp) => {return temp.length;})

var tempsLength3 = temps.map(temp => temp.length);

var tempsLength4 = temps.map(temp =>
{
    a = temp.length + 1;
    return a;
});

console.log(tempsLength1)
console.log(tempsLength2)
console.log(tempsLength3)
console.log(tempsLength4)