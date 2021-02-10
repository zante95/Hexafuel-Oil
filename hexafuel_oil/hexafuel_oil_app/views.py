from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'hexafuel_oil_app/login.html')

def form(request):
    return render(request, 'hexafuel_oil_app/fuel_quote.html')

def register(request):
    return render(request, 'hexafuel_oil_app/register.html')

def history(request):
    return render(request, 'hexafuel_oil_app/history.html')

def profile(request):
    return render(request, 'hexafuel_oil_app/account_settings.html')