from django.test import TestCase, Client
from django.urls import reverse
from .views import FuelQuoteFormView, ProfileView
from django.contrib.auth.models import User


username = 'user1'
password = '123'

client = Client()
newUser_noInfo = Client()
# newUser_noPreviousQuote = Client()

# login2 = newUser_noPreviousQuote.login(username = 'user22', password = '123')
logged_in = newUser_noInfo.login(username = 'user21', password = '123')
login = client.login(username = username, password = password)

test_successful_form_request = client.post(
    "/form/",
    {
        "gallons": ["4"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2022-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

test_failed_gallon_form_request = client.post(
    "/form/",
    {
        "gallons": ["NUM"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2021-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

test_failed_delivery_date_form_request = client.post(
    "/form/",
    {
        "gallons": ["150"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2021-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

test_failed_form_request = newUser_noInfo.post(
    "/form/",
    {
        "gallons": ["4"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2022-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

test_successful_form_request_greater_than_1000_gal = client.post(
    "/form/",
    {
        "gallons": ["2000"],
        "delivery-address": ["123 st"],
        "delivery-date": ["2022-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)

test_successful_get_address = client.get(
    "/form/",
    {

    },
)

test_failed_get_address = newUser_noInfo.get(
    "/form/",
    {

    },
)

class FuelQuoteFormViewTest(TestCase):
    
    @classmethod
    def test_successful_form_request(self): 
        pass

    @classmethod
    def test_failed_gallon_form_request(self): 
        pass

    @classmethod
    def test_failed_delivery_date_form_request(self): 
        pass
    
    @classmethod
    def test_failed_form_request(self): 
        pass

    @classmethod
    def test_successful_form_request_greater_than_1000_gal(self): 
        pass

    @classmethod
    def test_successful_get_address(self): 
        pass
    
    @classmethod
    def test_failed_get_address(self): 
        pass
    
test_successful_history_request = client.get(
    "/history/",
    {
       
    },
)

test_failed_history_request = newUser_noInfo.get(
    "/history/",
    {
        
    },
)

class HistoryViewTest(TestCase):
    
    @classmethod
    def test_successful_history_request(self): 
        pass

    @classmethod
    def test_failed_history_request(self): 
        pass


# no_error_test = Client()
# response = client.post(
#     "/profile/",
#     {
#     "fullname": [""],
#     "add1": ["14455 Country Place Dr"],
#     "add2": ["318"],
#     "city": ["Houston"],
#     "zipcode": ["77449"],
#     "is_Submitted": ["true"]
#     },
# )

# fullname_test = Client()
test_newUser_noInfo = newUser_noInfo.post(
    "/profile/",
    {
    "fullname": ["abc"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["318"],
    "city": ["Houston"],
    "state": ["TX"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

test_get_newUser_noInfo = newUser_noInfo.get(
    "/profile/",
    {

    },
)

class ProfileViewTest(TestCase):
    
    @classmethod
    def test_newUser_noInfo(self): 
        pass
    
    @classmethod
    def test_get_newUser_noInfo(self): 
        pass

test_calculate_not_get = client.post(
    "/calculate/",
    {
        "gallons": ["1500"],
        "delivery-date": ["2022-03-18"],
    },
)

test_calculate_successful_get_outside_TX = client.get(
    "/calculate/",
    {
        "gallons": ["1500"],
        "delivery-date": ["2022-03-18"],
    },
)

test_calculate_successful_get_in_TX = newUser_noInfo.get(
    "/calculate/",
    {
        "gallons": ["1500"],
        "delivery-date": ["2022-03-18"],
    },
)

test_calculate_successful_less_than_1000_gal = newUser_noInfo.get(
    "/calculate/",
    {
        "gallons": ["800"],
        "delivery-date": ["2022-03-18"],
    },
)

# test_calculate_successful_get_no_previous_quotes = newUser_noPreviousQuote.get(
#     "/calculate/",
#     {
#         "gallons": ["1500"],
#         "delivery-date": ["2022-03-18"],
#     },
# )

class CalculatePriceTest(TestCase):
    
    @classmethod
    def test_calculate_not_get(self): 
        pass

    @classmethod
    def test_calculate_successful_get_outside_TX(self): 
        pass

    @classmethod
    def test_calculate_successful_get_in_TX(self): 
        pass
    
    @classmethod
    def test_calculate_successful_less_than_1000_gal(self): 
        pass
    
    # @classmethod
    # def test_calculate_successful_get_no_previous_quotes(self): 
    #     pass

test_logout = newUser_noInfo.get(
    "/logout/",
    {

    },
)

class LogoutViewTest(TestCase):
    
    @classmethod
    def test_logout(self): 
        pass
# add1_test = Client()
# response = add1_test.post(
#     "/profile/",
#     {
#     "fullname": ["Carlos Suarez"],
#     "add1": [""],
#     "add2": ["318"],
#     "city": ["Houston"],
#     "zipcode": ["77449"],
#     "is_Submitted": ["true"]
#     },
# )

# add2_test = Client()
# response = add2_test.post(
#     "/profile/",
#     {
#     "fullname": ["Carlos Suarez"],
#     "add1": ["14455 Country Place Dr"],
#     "add2": ["desdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadsdesdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgads"],
#     "city": ["Houston"],
#     "zipcode": ["77449"],
#     "is_Submitted": ["true"]
#     },
# )

# zip_test = Client()
# response = zip_test.post(
#     "/profile/",
#     {
#     "fullname": ["Carlos Suarez"],
#     "add1": ["14455 Country Place Dr"],
#     "add2": ["desdsfg"],
#     "city": ["Houston"],
#     "zipcode": ["123"],
#     "is_Submitted": ["true"]
#     },
# )

# class ProfileViewTest(TestCase):
#     @classmethod
#     def test_no_error(self):
#         pass
    
#     @classmethod
#     def test_fullname(self):
#         pass
#     @classmethod
#     def test_add1(self):
#         pass
    
#     @classmethod
#     def test_add2(self):
#         pass
    
#     @classmethod
#     def test_zip(self):
#         pass

# c_wrong_email = Client()
# response = c_wrong_email.post(
#     "/register/",
#     {
#             'username': ['asd'], 
#             'email': ['asd@email'], 
#             'password1': ['123'], 
#             'password2': ['123'],
#             'isSubmitted': ['true']
#     },
# )

# c_wrong_username = Client()
# response = c_wrong_username.post(
#     "/register/",
#     {
#             'username': ['thisismorethan10character'], 
#             'email': ['asd@email.com'], 
#             'password1': ['123'], 
#             'password2': ['123'],
#             'isSubmitted': ['true']
#     },
# )

# c_empty_password = Client()
# response = c_empty_password.post(
#     "/register/",
#     {
#             'username': ['asd'], 
#             'email': ['asd@email.com'], 
#             'password1': ['123'], 
#             'password2': [''],
#             'isSubmitted': ['true']
#     },
# )


# c_mismatch_password = Client()
# response = c_mismatch_password.post(
#     "/register/",
#     {
#             'username': ['asd'], 
#             'email': ['asd@email.com'], 
#             'password1': ['123'], 
#             'password2': ['125'],
#             'isSubmitted': ['true']
#     },
# )

# class RegisterViewTest(TestCase):
    
#     @classmethod
#     def test_register_wrong_email(self):
#         #self.assertEqual(response.status_code, 200)
#         pass

#     @classmethod
#     def test_register_wrong_username(self):
#         pass

#     @classmethod
#     def test_register_empty_password(self):
#         pass

#     @classmethod
#     def test_register_mismatch_password(self):
#         pass

# c_login_wrong_username = Client()
# response = c_login_wrong_username.post(
#     "/",
#     {
#             'username': ['thisismorethan10character'], 
#             'password': ['123']
#     },
# )

# c_login_empty_password = Client()
# response = client.post(
#     "/",
#     {
#             'username': ['asd'], 
#             'password': ['']
#     },
# )

# class HomeViewTest(TestCase):
     
#     @classmethod
#     def test_login_wrong_username(self):
#         pass

#     @classmethod
#     def test_login_empty_password(self):
#         pass