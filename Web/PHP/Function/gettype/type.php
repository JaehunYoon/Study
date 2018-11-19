<?php

class foo {
    function __construct()
    {
        echo "hello~~";
    }
}

$a = 3.14;
$b = "it is string";
$c = new foo();

echo gettype($a);
echo gettype($b);
echo gettype($c);