<?php

$status = file_get_contents('lamp_status.txt');
print intval($status);

?>