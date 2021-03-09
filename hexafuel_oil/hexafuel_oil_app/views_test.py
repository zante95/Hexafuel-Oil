import uuid
from django.test import TestCase
from views import HomeView, RegisterView
from django.views.generic import TemplateView

#class HomeViewTest():
    #assert HomeView(TemplateView) == (request, 'hexafuel_oil_app/login.html')

class RegisterViewTest():
    
    def test_register_wrong_email(self):
        
        response = self.RegisterView.post.request(kwargs={
            'username': ['asd'], 
            'email': ['asd@email'], 
            'password1': ['123'], 
            'password2': ['123'],
            'isSubmitted': ['true']})
        # Manually check redirect (Can't use assertRedirect, because the redirect URL is unpredictable)
        
        self.assertEqual(response.status_code, 404)
        self.assertTrue(response.url.startswith('/register'))