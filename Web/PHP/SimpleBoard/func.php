<?php

function check_null($arg)
{
    if (is_null($arg))
    {
        $arg = "";
        return $arg;
    }
}

?>