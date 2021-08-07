<?php
$filepath = "waitfor/" . $_POST["qq"] . ".txt";
$myfile = fopen($filepath, "w") or die("Unable to open file!");
$txt = $_POST["id"] . "\n";
fwrite($myfile, $txt);
$txt = $_POST["qq"];
fwrite($myfile, $txt);
fclose($myfile);
var_dump("已提交，将在3秒跳转至反馈页面");
$url= "index.html" ;?>
<html>
<head>
<meta   http-equiv = "refresh"   content ="3;
url = log.txt ">
</head>
?>