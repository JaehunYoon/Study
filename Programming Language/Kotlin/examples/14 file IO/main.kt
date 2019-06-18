import java.io.File

fun main(args: Array<String>) {
    File("./data.txt").forEachLine {
        println(it)
    }
}