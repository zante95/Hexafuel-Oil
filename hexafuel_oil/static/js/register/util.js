//Query All input fields
var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}

// for avoiding email regex backend validation in views.py in register views function being triggered automatically (otherwise it will not grant tester access to the register page)  
function backendValidateForm() {
    document.forms["register-form"]["isSubmitted"].value = "true";
}