<?php
    $conn = @mysqli_connect("localhost", "user_name", "password", "db_name");
//  mysql에서 @는 오류 발생 시 오류메시지를 무시하고 넘어가라는 의미로 사용된다.

//  if (mysqli_connect_errno($conn)) echo "Database Connect Error";
//  위의 코드는 db 연결에 실패했을 때의 처리를 위해 사용된다.
?>