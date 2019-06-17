import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun main(args: Array<String>) {
    val current = LocalDateTime.now()
    val formatted = current.format(DateTimeFormatter.BASIC_ISO_DATE)

    println("current Date is $formatted")
}