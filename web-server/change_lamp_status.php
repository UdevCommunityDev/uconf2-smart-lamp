<?php

$status = file_get_contents('lamp_status.txt');

if (intval($status) == 0)
    file_put_contents('lamp_status.txt', '1');
else file_put_contents('lamp_status.txt', '0');

?>