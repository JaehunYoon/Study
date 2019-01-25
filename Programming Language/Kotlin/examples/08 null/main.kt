fun main(args: Array<String>) {
    val tempData = HashMap<String, String>().apply {
        put("email", "goodasd123@gmail.com")
        put("author", "JaehunYoon (h4lo)")
    }

    val email = tempData["email"] ?: null
    val name = tempData["name"] ?: null

    println(email)
    println(name)
}