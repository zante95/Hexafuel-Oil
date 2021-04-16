//Query All input fields
var form_fields = document.getElementsByTagName('input')

form_fields[1].placeholder = 'Gallons';
// form_fields[2].placeholder = '1234 Fake Address';
form_fields[3].placeholder = 'Delivery Date';


for (var field in form_fields) {
  form_fields[field].className += ' form-control'
}

function validateForm() {
  var x = document.forms["fuel-form"]["gallons"].value;
  if (x !== parseInt(data, 10)) {
    alert("Please enter a whole number for gallons.");
    return false;
  }
  if (x.length < 1) {
    alert("Please enter a number for gallons.");
    return false;
  }
}