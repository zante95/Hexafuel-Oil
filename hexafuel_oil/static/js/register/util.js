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
    //document.forms["register-form"]["isSubmitted"].value = "true";
    //console.log(document.forms["register-form"]["password1"].value)
    //console.log(document.forms["register-form"]["password2"].value)
    if((document.forms["register-form"]["password1"].value != document.forms["register-form"]["password2"].value)){
      $('.alert').removeAttr('hidden')
      $('.alert-message').text('Passwords do not match or username exceeds 10 characters')
      console.log('Passwords do not match or username exceeds 10 characters')
    }
}

function uiUpdate() {

    let button = document.querySelector("button");
    let classes = button.classList;
    classes.add("login_btn");
    
    let x = document.getElementById("id_username");
    let classes_x = x.classList;
    classes_x.add("form-control");

    let x2 = document.getElementById("id_email");
    let classes_x2 = x2.classList;
    classes_x2.add("form-control");

    let y = document.getElementById("id_password1");
    let classes_y = y.classList;
    classes_y.add("form-control");

    let z = document.getElementById("id_password2");
    let classes_z = z.classList;
    classes_z.add("form-control");

    var hasCheckedClass = $('body').find('span').hasClass('helptext');

        if (hasCheckedClass) {
          //add br after that elements
          $('.helptext').text('Required. 10 characters or fewer. Letters, digits and @/./+/-/_ only.')
          $('.helptext').after("<br/><br/>")
        } else {
          //do nothing
        }

}

$(document).ready(function() {
    uiUpdate();
});