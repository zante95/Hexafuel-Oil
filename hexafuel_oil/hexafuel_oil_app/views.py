from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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
    return render(request, 'hexafuel_oil_app/register.html')

def history(request):
    return render(request, 'hexafuel_oil_app/history.html')

def profile(request):
    return render(request, 'hexafuel_oil_app/account_settings.html')