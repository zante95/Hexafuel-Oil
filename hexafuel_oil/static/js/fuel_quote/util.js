//Query All input fields
var form_fields = document.getElementsByTagName('input')
form_fields[0].placeholder='Gallons';
form_fields[1].placeholder='123 Fake Address';
form_fields[2].placeholder='Delivery Date';


for (var field in form_fields){	
form_fields[field].className += ' form-control'
}

function validateForm() {
      var x = document.forms["fuel-form"]["gallons"].value;
      if (isNaN(x)) {
        alert("Please enter a number for gallons.");
        return false;
      }
      if (x.length < 1) {
        alert("Please enter a number for gallons.");
        return false;
      }
    }