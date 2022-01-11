<?php 


$nu="a".$_REQUEST["num"];
$nu1=str_replace("a010","10",$nu);
$nu2=str_replace("a012","12",$nu1);
$nu3=str_replace("a015","15",$nu2);
$num=str_replace("a011","11",$nu3);
$command = escapeshellcmd('python code1.py '.$num);
$output = shell_exec($command);
echo $output;

?>
 
