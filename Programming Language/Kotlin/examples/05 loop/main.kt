fun main(args: Array<String>) {
    val items = listOf("Apple", "Banana", "Carrot")
    var index: Int = 0

    for (i in items.indices) {
        println("item at $i is ${items[i]}")
        // 기본적인 foreach 루프가 아닌 인덱스를 사용한 루프를 돌기 위해서는 iterable 변수에 .indices 옵션을 준다.
    }

    while (index < items.size) {
        println("item at $index is ${items[index]}")
        index++
    }

    items.forEach {
        println("item is ${it}")
    }
}