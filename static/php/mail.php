<?php
$name = $_POST['name'];
$email = $_POST['email']
$subjectt = $_POST['subjectt']
$message = $_POST['message']
$formcontent="From: $name \n Subject: $subjectt Message: $message";
$recipient = "niranjan27494@gmail.com";
$subject = "Contact Form";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
echo "Thank You!";
?>
