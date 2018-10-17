<?php
/*
생성자 (Constructor)

void __construct ([mixed &args = ""[, $...]])

PHP5 이상의 버전을 사용하면, 클래스의 생성자 메소드를 선언할 수가 있다.
클래스는 새로이 생성된 오브젝트마다 자신의 생성자 메소드를 호출한다.
객체 초기화에 사용 가능.

[Note]
부모 생성자는 자식클래스가 생성자를 가지고 있을 경우 내부적으로 호출되지 않는다.
부모 생성자를 호출하기 위해서는 자식 생성자 내에서 parent::__construct() 호출이 필요하다.
자식이 생성자를 가지지 않는다면 다른 일반적인 클래스 메소드처럼 부모클래스의 생성자가 상속된다(private 메소드는 제외).
*/

class BaseClass 
{
    function __construct()
    {
        echo "In BaseClass Constructor<br>\n";
    }
}

class SubClass extends BaseClass // SubClass 는 자식 클래스이며 BaseClass를 부모 클래스로서 상속한다.
{
    function __construct()
    {
        parent::__construct(); // 부모 클래스인 BaseClass의 생성자를 호출한다.
        echo "In SubClass Constructor<br>\n";
    }
}

class OtherSubClass extends BaseClass
{
    // 부모 클래스인 BaseClass의 생성자 상속
}

$obj = new BaseClass(); // BaseClass 객체 생성
$obj = new SubClass(); // BaseClass를 상속하는 SubClass 객체 생성
$obj = new OtherSubClass(); // BaseClass를 상속하는 OTherSubClass 객체 생성