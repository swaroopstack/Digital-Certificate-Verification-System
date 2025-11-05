<?php
include('db_connect.php');

$cert_id = $_POST['certificate_id'];

$sql = "SELECT c.Certificate_ID, c.Certificate_Type, c.Status, c.Expiry_Date,
               h.Name AS Holder_Name, i.Institution_Name AS Issuer_Name
        FROM Certificate c
        JOIN Holder h ON c.Holder_ID = h.Holder_ID
        JOIN Issuer i ON c.Issuer_ID = i.Issuer_ID
        WHERE c.Certificate_ID = $cert_id";

$result = $conn->query($sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Verification Result</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
  <h1>🔍 Verification Result</h1>
  <?php
  if ($result->num_rows > 0) {
      $row = $result->fetch_assoc();
      $statusColor = ($row['Status'] == 'Valid') ? 'green' : 'red';
      echo "<h3>Certificate ID: " . $row['Certificate_ID'] . "</h3>";
      echo "<p><b>Holder:</b> " . $row['Holder_Name'] . "</p>";
      echo "<p><b>Issuer:</b> " . $row['Issuer_Name'] . "</p>";
      echo "<p><b>Type:</b> " . $row['Certificate_Type'] . "</p>";
      echo "<p><b>Expiry Date:</b> " . $row['Expiry_Date'] . "</p>";
      echo "<p><b>Status:</b> <span style='color:$statusColor; font-weight:bold;'>" . $row['Status'] . "</span></p>";
  } else {
      echo "<p style='color:red;'>❌ No certificate found with ID $cert_id</p>";
  }
  $conn->close();
  ?>
  <br>
  <a href="index.html"><button>Verify Another</button></a>
</div>
</body>
</html>
