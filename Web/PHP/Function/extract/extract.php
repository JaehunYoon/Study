<?php

$arr = array();

$arr["extract1"] = "one";
$arr["extract2"] = "two";
$arr["extract3"] = "three";

extract($arr);

echo $extract1;
echo $extract2;
echo $extract3;