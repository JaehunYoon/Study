<?php
    // 특수 비교 연산자

    $a = 3;
    $b = 5;

    echo "a = $a, b = $b". "\n";
    echo "[a <=> b]\n";
    echo $a <=> $b;
    echo "\n". "[b <=> a]\n";
    echo $b <=> $a;
    echo "\n". "[a <=> a]\n";
    echo $a <=> $a;

    // <=> 는 특수 비교 연산자로, a <=> b 를 예로 들었을 때,
    // a가 b보다 작으면 -1, 크면 1, 같으면 0을 결과값으로 반환한다.

    $temp1 = NULL;
    $temp2 = NULL;
    $temp3 = NULL;
    $temp4 = 1;

    // echo "temp1 ~ temp3 = NULL, temp4 = 1\n";
    // echo "temp1 ?? temp2 ?? temp3 = ";
    // var_dump(temp1 ?? temp2 ?? temp3);
    // echo "\n". "temp1 ?? temp2 ?? temp3 ?? temp4 = ";
    // var_dump(temp1 ?? temp2 ?? temp3 ?? temp4);

    // a??b??c?? 와 같은 식을로 되어 있을 때 우측으로 순서대로 값을 확인하여 NULL이 아닌 처음값을 반환.
    // a, b, c가 모두 NULL이면 반환값도 NULL이다.
    // Warning!! php cli 상에서 실행하면 정상적으로 출력이 되지 않는다!
?>