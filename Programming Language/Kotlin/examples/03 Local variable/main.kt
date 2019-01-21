fun main(args: Array<String>) {
    val a: Int = 1 // 특시 할당
    val b = 2 // 'Int' 타입으로 추론
    val c: Int // 초기화를 하지 않으면 타입 필요
    c = 3 // 나중에 할당
    
    var x = 5
    x += 1
    
    // val = 수정 불가능한 final 변수
    // var = 읽기/쓰기가 가능한 일반 변수
    // let = var가 구려서 let을 쓴다!
    // const = 상수 개념 val이랑 비슷한가?
}