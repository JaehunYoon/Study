fun getStringLength(obj: Any): Int? {
    if (obj is String) {
        return obj.length
    }

    return null
}

fun main(args: Array<String>) {
    var len = getStringLength("안녕하세요~~")
    println(len)
}