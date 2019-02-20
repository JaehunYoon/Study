fun main() {
    val lazySeq = sequence {
        println("START")
        for (i in 1..5) {
            yield(i)
            println("STEP")
        }
        println("END")
    }
    lazySeq.take(3).forEach { println(it)}
}Í