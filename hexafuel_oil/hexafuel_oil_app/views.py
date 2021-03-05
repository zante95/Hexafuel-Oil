from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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