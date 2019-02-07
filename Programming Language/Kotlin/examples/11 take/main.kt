fun main() {
    val chars = ('a'..'z').toList()

    println(chars.take(3))
    println(chars.takeWhile {it < 'f'})
    println(chars.takeLast(2))
    println(chars.takeLastWhile {it > 'w'})
}