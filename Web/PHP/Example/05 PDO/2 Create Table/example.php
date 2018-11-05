<?php

$host = "localhost";
$db = "h4lo";
$user = "h4lo";
$pass = "h4lo";

try
{
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo-> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_SILENT);

    $isTable = $pdo-> exec("CREATE TABLE `test`
    (
        `id` INT UNSIGNED NOT NULL,
        `user_id` char(10) NOT NULL,
        `user_pass` char(30) NOT NULL,
        `comment` varchar(50),
        PRIMARY KEY (`id`)
    );");

    if ($isTable === false)
    {
        echo "\$isTable is False~~";
    }
    else
    {
        echo ":D";
    }
}

catch (PDOException $e) 
{
    echo "Database Error!" . $e-> getMessage();
}