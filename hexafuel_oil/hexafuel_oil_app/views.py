from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import re
from django.views.generic import TemplateView, CreateView, FormView, DetailView, View, UpdateView
from django.contrib.auth import authenticate, login, logout, get_user_model
#from rest_framework import permissions

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .mixins import NextUrlMixin, RequestFormAttachMixin
from .forms import LoginForm, RegisterForm #, GuestForm, ReactivateEmailForm, UserDetailChangeForm
#from .signals import user_logged_in

# Create your views here.

class HomeView(TemplateView):
    template_name = "hexafuel_oil_app/login.html"
    #permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):

        print("REQUEST", request.POST)
        username = str(request.POST.get('username'))
        pwd = str(request.POST.get('password'))
        
        self.object = []

        print(type(username)) #-> <class 'str'>
        print(type(pwd)) #-> <class 'str'>
        
        if (username == "") or (len(username) > 10):
            return JsonResponse({"ValidationError": "username cannot be empty or cannot exceed 10 chars."})

        if pwd == "":
            return JsonResponse({"ValidationError": "password cannot be empty."})

        return render(request, 'hexafuel_oil_app/login.html')

#@method_decorator(login_required, name='dispatch')
#class FuelQuoteFormView(TemplateView):
class FuelQuoteFormView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "hexafuel_oil_app/fuel_quote.html"
    permission_required = ("auth.change_user")

    def post(self, request, *args, **kwargs):
        # def post(request, format=None, *args, **kwargs):
        print("REQUEST", request.POST)
        # print("BOOL", bool(request.POST))
        # print("REQUEST", request.POST)
        # data = request.POST.copy()

        self.object = []

        if bool(request.POST):
            data = request.POST.dict()

            gallons = data["gallons"]
            delivery_date_str = data["delivery-date"]
            delivery_address = data["delivery-address"]

            if not gallons.isnumeric():
                return JsonResponse(
                    {"ValidationError": "Gallons must be a whole number."}
                )

            # if not True:
            #     return JsonResponse({"ValidationError": "Delivery address does not match"})

            date_time_obj = datetime.datetime.strptime(delivery_date_str, "%Y-%m-%d")

            if date_time_obj < datetime.datetime.now():
                return JsonResponse({"ValidationError": "Choose a latter date."})

        return render(
            request,
            "hexafuel_oil_app/fuel_quote.html",
        )

class RegisterView(TemplateView):
    template_name = "hexafuel_oil_app/register.html"
    #permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):

        print("REQUEST", request.POST)
        username = str(request.POST.get('username'))
        email = str(request.POST.get('email'))
        pwd = str(request.POST.get('password1'))
        retypePwd = str(request.POST.get('password2'))

        isSubmitted = str(request.POST.get('isSubmitted'))
        
        self.object = []

        print(type(username)) #-> <class 'str'>
        print(type(email)) #-> <class 'str'>
        print(type(pwd)) #-> <class 'str'>
        print(type(retypePwd)) #-> <class 'str'>
        print(type(isSubmitted)) #-> <class 'str'>
        
        email_regex = re.compile(r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|'(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*')@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")

        if (isSubmitted == "true"):

            if (username == "") or (len(username) > 10):
                return JsonResponse({"ValidationError": "username cannot be empty or cannot exceed 10 chars."})

            if (pwd == "") or (retypePwd == ""):
                return JsonResponse({"ValidationError": "password or retype-password field cannot be empty."})
            
            if (pwd != retypePwd):
                return JsonResponse({"ValidationError": "please make sure password and retype-password field match."})
            
            if (not(email_regex.match(email))):
                return JsonResponse({"ValidationError": "email is not valid."})

        return render(request, 'hexafuel_oil_app/register.html')

#use login_required for function based view OR use LoginRequiredMixin for class-based view
def history(request): # pragma: no cover
    return render(request, 'hexafuel_oil_app/history.html')

#@method_decorator(login_required, name='dispatch')
#class ProfileView(TemplateView):
class ProfileView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
   template_name = "hexafuel_oil_app/account_settings.html"
   permission_required = ("auth.change_user")

   def post(self, request, *args, **kwargs):
    #    fullname, address1, address2, city, zipcode
        print("REQUEST", request.POST)
        fullname = str(request.POST.get('fullname'))
        add1 = str(request.POST.get('address1'))
        add2 = str(request.POST.get('address2'))
        city = str(request.POST.get('city'))
        zipcode = str(request.POST.get('zipcode'))
        is_Submitted = str(request.POST.get('is_Submitted'))
 
        self.object = []
 
        if(is_Submitted == "true"):
              
            if (len(fullname)<1) or (len(fullname) > 50):
                return JsonResponse({"ValidationError": "Name needs to be more than 1 and less than 55 charaters longs."})
 
            if (len(add1)<1) or (len(add1) > 100):
                return JsonResponse({"ValidationError": "Address 1 needs to be more than 1 and less than 100 charaters longs."})
 
            if len(add2) > 100:
                return JsonResponse({"ValidationError": "Address 2 needs to be less than 100 charaters longs."})
 
            if (len(city)<1) or (len(city)) > 100:
                return JsonResponse({"ValidationError": "City needs to be more than 1 and less than 100 charaters longs."})
 
            if len(zipcode) != 5:
                return JsonResponse({"ValidationError": "City needs to be 5 characters long."})
 
        return render(request, 'hexafuel_oil_app/account_settings.html')

class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/form'
    template_name = 'hexafuel_oil_app/login.html'
    default_next = '/home'

    def form_valid(self, form):
        next_path = self.get_next_url()
        print(next_path)

        return redirect('/form')

class RegisterView2(CreateView):
    form_class = RegisterForm
    template_name = 'hexafuel_oil_app/register2.html'
    success_url = '/home'