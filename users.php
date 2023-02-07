<?php
header("Content-Type: application/json");

$passcode = $_POST["passcode"];
$users = array(
  array("username" => "user1", "passcode" => "abc123"),
  array("username" => "user2", "passcode" => "def456"),
  array("username" => "user3", "passcode" => "ghi789"),
  // add more users as needed
);

$result = array("status" => "error");

foreach ($users as $user) {
  if ($user["passcode"] == $passcode) {
    $result["status"] = "success";
    $result["username"] = $user["username"];
    break;
  }
}

echo json_encode($result);