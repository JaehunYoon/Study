<?php

try
{
    // Create MySQL PDO object
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);

    // PDO 생성자에 첫 번째 인수로 전달된 문자열을 DSM(Data Source Name) 이라 한다.

    // Print Error
    $pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    /*
    [Error Mode]

    1. Do not print Error Message -> PDO::ERRMODE_SILENT
    2. Print only "Warning" -> PDO::ERRMODE_WARNING
    3. Print Error -> PDO::ERRMODE_EXCEPTION
    */
}

catch (PDOException $e)
{
    echo "Couldn't connect database.." . $e -> getMessage();
}   