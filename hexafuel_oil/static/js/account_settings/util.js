//Query All input fields
var form_fields = document.getElementsByTagName('input');
form_fields[1].placeholder='Full Name..';
form_fields[2].placeholder='Address 1..';
form_fields[3].placeholder='Address 2..';
form_fields[4].placeholder='City..';
form_fields[5].placeholder='ZIP code..';

for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}

function validateForm(){
    var fullnameIsValid = document.forms["profile-form"]["fullname"].value;
    var address1IsValid = document.forms["profile-form"]["address1"].value;
    var address2IsValid = document.forms["profile-form"]["address2"].value;
    var cityIsValid = document.forms["profile-form"]["city"].value;
    var zipcodeIsValid = document.forms["profile-form"]["zipcode"].value;

    if (fullnameIsValid.length < 1 || fullnameIsValid.length > 50) {
        alert("Please enter your full name and make sure it does not exceed beyond 50 characters.");
        return false;
    }

    if (address1IsValid.length < 1 || address1IsValid.length > 100) {
        alert("Please enter your address line 1 and make sure it does not exceed beyond 100 characters.");
        return false;
    }

    if (address2IsValid.length > 100) {
        alert("Please make sure your address line 2 does not exceed beyond 100 characters.");
        return false;
    }

    if (cityIsValid.length < 1 || cityIsValid.length > 100) {
        alert("Please enter your city and make sure it does not exceed beyond 100 characters.");
        return false;
    }
    
    if (zipcodeIsValid.length != 5) {
        alert("Please enter your zip code and make sure it has 5 characters.");
        return false;
    } 

    document.forms['profile-form']['is_Submitted'].value="true"
}