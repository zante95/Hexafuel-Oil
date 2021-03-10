from django.test import RequestFactory, TestCase, Client
from .views import RegisterView
from django.views.generic import TemplateView

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