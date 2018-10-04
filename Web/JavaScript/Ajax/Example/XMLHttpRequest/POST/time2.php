<?php
$dl = new Datetime;
$dl -> setTimezone(new DataTimezone($_POST['timezome']));

echo $dl -> format($_POST['format']);