// Login validation check
document.querySelector('#login_form').onsubmit = function() {
  if (!document.querySelector('#username_log').value){
      document.getElementById('login_err').style.display = "block";
      // alert("You must provide your first name")
      return false;
  } else if(!document.querySelector('#password_log').value)
  {
      document.getElementById('login_err').style.display = "block";
      // alert("You must provide your password")
      return false;
  }
  return true;
};


// Register validation check
document.querySelector('#register_form').onsubmit = function() {
  if (!document.querySelector('#username_regi').value){
      document.getElementById('regi-err').style.display = "block";
      // alert("You must provide your first name")
      return false;
  } else if(!document.querySelector('#password_regi').value)
  {
      document.getElementById('regi-err').style.display = "block";
      // alert("You must provide your password")
      return false;
  } else if(!document.querySelector('#confirm_pass_regi').value)
  {
      document.getElementById('regi-err').style.display = "block";
      // alert("You must provide your password")
      return false;
  } else if(!document.querySelector('#register_code').value)
  {
      document.getElementById('code-err').style.display = "block";
      // alert("Enter valid register code")
      return false;
  }
  return true;
};
