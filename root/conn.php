<?php
$conn=mysql_connect("127.0.0.1:3306",'root','');
mysql_select_db("pscan",$conn);
session_start();

if(@$_GET['hash']){
$_SESSION['hash']=$_GET['hash'];
}
$hash=@$_SESSION['hash'];
if (strlen($hash) == 0) {
    $hash = 'cond0r';
}
?>