<?php
    // 암묵적 형변환
    
    echo "1각김밥" + "2각김밥";
    // PHP에서 암묵적 형변환이 빈번하게 발생한다는 소리가 있어서 실험해보고자 함.
    // 숫자가 들어간 문자열을 병합하면, 위의 형변환에 따르면 출력결과가 "3각김밥" 이 되어야 함.
    //
    // [Result]
    // PHP Notice:  A non well formed numeric value encountered in [파일경로] Notice:  A non well formed numeric value encountered in [파일경로]
    // -> 자동 형변환은 PHP Notice를 출력한 후, 결과값은 정상적으로 출력시키지 못하였다.
?>