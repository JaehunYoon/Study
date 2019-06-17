import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.format.FormatStyle

fun main(args: Array<String>) {
    val current = LocalDateTime.now()
    val formatted = current.format(DateTimeFormatter.ofLocalizedDateTime(FormatStyle.MEDIUM))

    println("Current Date is $formatted")
}