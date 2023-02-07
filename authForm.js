$(document).ready(function() {
  $("#signup-form").submit(function(event) {
    event.preventDefault();
    var email = $("#signup-email").val();
    var username = $("#signup-username").val();
    var password = $("#signup-password").val();

    // Send sign-up data to server
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:5500/signup",
      data: JSON.stringify({
        email: email,
        username: username,
        password: password
      }),
      contentType: "application/json",
      success: function(data) {
        // Handle successful sign-up
        console.log("Sign-up successful");
      },
      error: function(data) {
        // Handle sign-up error
        console.log("Sign-up error");
      }
    });
  });

  $("#login-form").submit(function(event) {
    event.preventDefault();
    var email = $("#login-email").val();
    var password = $("#login-password").val();

    // Send login data to server
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:5500/login",
      data: JSON.stringify({
        email: email,
        password: password
      }),
      contentType: "application/json",
      success: function(data) {
        // Handle successful login
        console.log("Login successful");
      },
      error: function(data) {
        // Handle login error
        console.log("Login error");
      }
    });
  });
});