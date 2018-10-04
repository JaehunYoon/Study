<?php
$dl = new DateTime;
$dl -> setTimezone(new DateTimezone("asia/seoul"));

echo $dl -> format('H:i:s');