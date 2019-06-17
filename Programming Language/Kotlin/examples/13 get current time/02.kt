import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun main(args: Array<String>) {
    val current = LocalDateTime.now()
    val formatted = current.format(DateTimeFormatter.ofPattern("YYYY-MM-dd"))

    println("Current Date is $formatted")
}