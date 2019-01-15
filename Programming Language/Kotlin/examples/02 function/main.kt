fun sum1(a: Int, b: Int): Int {
    return a + b
} 

fun sum2(a: Int, b: Int) = a + b

fun sum3(a: Int, b: Int): Unit {
    println("sum3 = ${a + b}")
}

fun main() {
    println("sum1 = ${sum1(3, 4)}")
    println("sum2 = ${sum2(3, 4)}")
    sum3(3, 4)
}