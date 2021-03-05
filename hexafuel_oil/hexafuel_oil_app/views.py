from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import re

# Create your views here.

def home(request):

    print("REQUEST", request.POST)
    username = str(request.POST.get('username'))
    pwd = str(request.POST.get('password'))
    
    print(type(username)) #-> <class 'str'>
    print(type(pwd)) #-> <class 'str'>
    
    if (username == "") or (len(username) > 10):
        return JsonResponse({"ValidationError": "username cannot be empty or cannot exceed 10 chars."})

    if pwd == "":
        return JsonResponse({"ValidationError": "password cannot be empty."})

    return render(request, 'hexafuel_oil_app/login.html')

def form(request):
    return render(request, 'hexafuel_oil_app/fuel_quote.html')

def register(request):

    print("REQUEST", request.POST)
    username = str(request.POST.get('username'))
    email = str(request.POST.get('email'))
    pwd = str(request.POST.get('password1'))
    retypePwd = str(request.POST.get('password2'))

    isSubmitted = str(request.POST.get('isSubmitted'))
    
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

def history(request):
    return render(request, 'hexafuel_oil_app/history.html')

def profile(request):
    # fullname, address1, address2, city, zipcode 
    print("REQUEST", request.POST)
    fullname = str(request.POST.get('fullname'))
    add1 = str(request.POST.get('address1'))
    add2 = str(request.POST.get('address2'))
    city = str(request.POST.get('city'))
    zipcode = str(request.POST.get('zipcode'))
    is_Submitted = str(request.POST.get('is_Submitted'))

    if(is_Submitted == "true"):
            
        if (len(fullname)<1 or len(fullname) > 55):
            return JsonResponse({"ValidationError": "Name needs to be more than 1 and less than 55 charaters longs."})

        if (len(add1)<1 or len(add1) > 100):
            return JsonResponse({"ValidationError": "Address 1 needs to be more than 1 and less than 100 charaters longs."})

        if len(add2) > 100:
            return JsonResponse({"ValidationError": "Address 2 needs to be less than 100 charaters longs."})

        if (len(city)<1 or len(city)) > 100:
            return JsonResponse({"ValidationError": "City needs to be more than 1 and less than 100 charaters longs."})

        if len(zipcode) != 5:
            return JsonResponse({"ValidationError": "City needs to be 5 characters long."})

    return render(request, 'hexafuel_oil_app/account_settings.html')