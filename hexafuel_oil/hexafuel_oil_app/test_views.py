from django.test import TestCase, Client
from django.urls import reverse
from .views import FuelQuoteFormView, ProfileView, RegisterView
from django.contrib.auth.models import User


username = 'user1'
password = '123'

client = Client()
login = client.login(username=username, password=password)
# failed_login = client.login(username='fakeUser', password='fakePass')

successful_form_request = client.post(
    "/form/",
    {
        "gallons": ["4"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2022-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

falied_gallon_form_request = client.post(
    "/form/",
    {
        "gallons": ["NUM"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2021-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

falied_delivery_date_form_request = client.post(
    "/form/",
    {
        "gallons": ["NUM"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2021-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)


class FuelQuoteFormViewTest(TestCase):
    @classmethod
    def test_view_validations(self):
        # response = self.client.post("/form/")
        # print("self", self)
        # print("self", self.__dict__)
        # print("response", response)
        # print("response.status_code", response.status_code)
        # self.assertEqual(response.status_code, 200)
        pass

no_error_test = Client()
response = no_error_test.post(
    "/profile/",
    {
    "fullname": [""],
    "add1": ["14455 Country Place Dr"],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

fullname_test = Client()
response = fullname_test.post(
    "/profile/",
    {
    "fullname": ["abc"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

add1_test = Client()
response = add1_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": [""],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

add2_test = Client()
response = add2_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["desdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgads"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

zip_test = Client()
response = zip_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["desdsfg"],
    "city": ["Houston"],
    "zipcode": ["123"],
    "is_Submitted": ["true"]
    },
)

class ProfileViewTest(TestCase):
    @classmethod
    def test_no_error(self):
        pass
    
    @classmethod
    def test_fullname(self):
        pass
    @classmethod
    def test_add1(self):
        pass
    
    @classmethod
    def test_add2(self):
        pass
    
    @classmethod
    def test_zip(self):
        pass
        
c_wrong_email = Client()
response = c_wrong_email.post(
    "/register/",
    {
            'username': ['asd'], 
            'email': ['asd@email'], 
            'password1': ['123'], 
            'password2': ['123'],
            'isSubmitted': ['true']
    },
)

c_wrong_username = Client()
response = c_wrong_username.post(
    "/register/",
    {
            'username': ['thisismorethan10character'], 
            'email': ['asd@email.com'], 
            'password1': ['123'], 
            'password2': ['123'],
            'isSubmitted': ['true']
    },
)

c_empty_password = Client()
response = c_empty_password.post(
    "/register/",
    {
            'username': ['asd'], 
            'email': ['asd@email.com'], 
            'password1': ['123'], 
            'password2': [''],
            'isSubmitted': ['true']
    },
)

c_mismatch_password = Client()
response = c_mismatch_password.post(
    "/register/",
    {
            'username': ['asd'], 
            'email': ['asd@email.com'], 
            'password1': ['123'], 
            'password2': ['125'],
            'isSubmitted': ['true']
    },
)

class RegisterViewTest(TestCase):
    
    @classmethod
    def test_register_wrong_email(self):
        #self.assertEqual(response.status_code, 200)
        pass

    @classmethod
    def test_register_wrong_username(self):
        pass

    @classmethod
    def test_register_empty_password(self):
        pass

    @classmethod
    def test_register_mismatch_password(self):
        pass

c_login_wrong_username = Client()
response = c_login_wrong_username.post(
    "/",
    {
            'username': ['thisismorethan10character'], 
            'password': ['123']
    },
)

c_login_empty_password = Client()
response = c_login_empty_password.post(
    "/",
    {
            'username': ['asd'], 
            'password': ['']
    },
)

class HomeViewTest(TestCase):
     
    @classmethod
    def test_login_wrong_username(self):
        pass

    @classmethod
    def test_login_empty_password(self):
        pass
