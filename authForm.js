$(document).ready(function() {

  $("#login-form").submit(function(event) {
    event.preventDefault();
    var passcode = $("#login-passcode").val();

    // Send login data to server
    $.ajax({
      type: "POST",
      url: "/login",
      data: JSON.stringify({
        passcode: passcode
      }),
      contentType: "application/json",
      success: function(data) {
        // Handle successful login
        console.log("Login successful");
        window.location.href = "mypicks.html";
      },
      error: function(data) {
        // Handle login error
        console.log("Login error");
        window.location.href = "leaderboard.html";
      }
    });
  });
});