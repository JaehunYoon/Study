<?php

Example::name_string();  # Example 클래스의 static형 name_string() 이라는 메소드를 호출.

class Example
{
    static function name_string()  // 정적 메소드 name_string 선언
    {
        echo "test is good!";
    }
}