// import java.lang.*

fun main(args: Array<String>) {
    val javaString: String = "String"
    val kotlinString: kotlin.String = "String"

    println("javaString's type is ${javaString.javaClass.name}")
    println("kotlinString's type is ${kotlinString.javaClass.name}")

    if (javaString === kotlinString) {
        println("Same!")
    } else {
        println("Different!")
    }
}