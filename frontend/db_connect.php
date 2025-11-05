<?php
$host = "localhost";
$user = "root";  // your MySQL username
$pass = "root123";  // your MySQL password
$db = "certificate_verification";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
