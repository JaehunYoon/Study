fun main(args: Array<String>) {
    val temp = "bearer abcdefghijklmnopqrstuvwxyz1234567890"
    val token = HashMap<String, String>().apply {
        put("token", temp)
    }
    println(token.getValue("token"))
    token.getValue("token").let {
        it.split(" ").toTypedArray().also {
            println(it[0])
            println(it[1])
        }
    }
}