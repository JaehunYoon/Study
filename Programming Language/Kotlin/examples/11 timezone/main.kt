fun main(args: Array<String>) {
    val temp = DateTimeFormatter.ISO_INSTANT.format(Instant.now())
        .ofPattern("yyyy-MM-dd HH:mm:ss.SSSSSS")
        .withZone(ZoneOffset.UTC)
        .format(Instant.now())

    println(temp)
}