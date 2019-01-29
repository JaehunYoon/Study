import kotlin.coroutines.experimental.buildSequence

fun main(args: Array<String>) {
    val fibonacciSeq = buildSequence {
        var a = 0
        var b = 1

        yield(1)

        while (true) {
            yield(a + b)

            val tmp = a + b
            a = b
            b = tmp
        }
    }

    println(fibonacciSeq.take(8).toList())
}