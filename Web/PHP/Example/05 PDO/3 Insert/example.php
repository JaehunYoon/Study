<?php

$user_id = $_POST['id'];
$user_pass = $_POST['pw'];
$comment = $_POST['comment'];

$host = "localhost";
$db = "h4lo";
$user = "h4lo";
$pass = "h4lo";

try {
    $pdo = new PDO("mysql:host=$host; dbname=$db", $user, $pass);
    $pdo-> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_SILENT);

    $result = $pdo-> exec("INSERT INTO `test` (user_id, user_pass, comment) VALUES ('$user_id', '$user_pass', '$comment');");

    if($result === false) {
        $error = $pdo-> errorInfo();
        echo "데이터를 추가할 수 없습니다.\n";
        echo "SQL Error={$error[0]}, DB Error={$error[1]}, Message={$error[2]}";
    }
    else {
        echo ":D";
    }
}

catch (PDOException $e) {
    echo "Database Error :C.." . $e-> getMessage();
}