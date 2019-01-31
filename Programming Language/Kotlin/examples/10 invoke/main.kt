object Foo {
    operator fun invoke() = "Hello World!"
    operator fun invoke(message: String) = "Hello $message"
}

fun main(args: Array<String>) {
    println(Foo())
    println(Foo("World"))
}