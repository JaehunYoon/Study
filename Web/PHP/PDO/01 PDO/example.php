<?php

try
{
    // Create MySQL PDO object
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);

    // Print Error
    $pdo -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    /*
    [Error Mode]

    1. Do not print Error Message -> PDO::ERRMODE_SILENT
    2. Print only "Warning" -> PDO::ERRMODE_WARNING
    3. Print Error -> PDO::ERRMODE_EXCEPTION
    */
}

catch (Exception $e)
{
    echo $e -> getMessage();
}   