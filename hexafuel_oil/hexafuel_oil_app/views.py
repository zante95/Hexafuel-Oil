from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import re
from django.views.generic import TemplateView, CreateView, FormView, DetailView, View, UpdateView, RedirectView
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .mixins import NextUrlMixin, RequestFormAttachMixin
from .forms import LoginForm, RegisterForm
from .models import FuelQuote, ClientInformation
from django.contrib.auth.models import User


def calculatePrice(request):
      if request.method == 'GET':
        queryset = ClientInformation.objects.all()
        location = queryset.get(auth_user_id_id = request.user.id).state
        gallons = str(request.GET.get("gallons"))

        current_price_per_gallons = 1.50
        company_profit_factor = 0.1

        if location == 'TX':
          location_factor = 0.02
        else:
          location_factor = 0.04

        clients_queryset = ClientInformation.objects.all()
        client_id = clients_queryset.get(auth_user_id_id = request.user.id).id
        quotes_queryset = FuelQuote.objects.all()
        quotes = quotes_queryset.filter(client_id_id = client_id)
        
        if len(quotes) > 0:
          rate_history_factor = 0.01
        else:
          rate_history_factor = 0
        
        if int(gallons) >= 1000:
          gallons_requested_factor = 0.02
        else:
          gallons_requested_factor = 0.03

        margin = current_price_per_gallons * (location_factor - rate_history_factor + gallons_requested_factor + company_profit_factor)

        suggested_price_per_gallons = current_price_per_gallons + margin
        total_result = suggested_price_per_gallons * int(gallons)
        price_result = suggested_price_per_gallons
        args = {'price_result':price_result, 'total_result':total_result}
        return JsonResponse(args) # Sending an success response

      else:
        return HttpResponse("Request method is not a GET")


# ajax functionality was added to get the price quote before doing a form submission
class FuelQuoteFormView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "hexafuel_oil_app/fuel_quote.html"
    permission_required = ("auth.change_user")

    def calculatePrice(self, user_id, location, gallons):
          current_price_per_gallons = 1.50
          company_profit_factor = 0.1

          if location == 'TX':
            location_factor = 0.02
          else:
            location_factor = 0.04

          clients_queryset = ClientInformation.objects.all()
          client_id = clients_queryset.get(auth_user_id_id = user_id).id
          quotes_queryset = FuelQuote.objects.all()
          quotes = quotes_queryset.filter(client_id_id = client_id)
          
          if len(quotes) > 0:
            rate_history_factor = 0.01
          else:
            rate_history_factor = 0
          
          if int(gallons) >= 1000:
            gallons_requested_factor = 0.02
          else:
            gallons_requested_factor = 0.03

          margin = current_price_per_gallons * (location_factor - rate_history_factor + gallons_requested_factor + company_profit_factor)

          suggested_price_per_gallons = current_price_per_gallons + margin
          return suggested_price_per_gallons * int(gallons),suggested_price_per_gallons
    
    def get(self, request):
        try:
            clients_queryset = ClientInformation.objects.all()
            client = clients_queryset.get(auth_user_id_id = request.user.id)
            args = {'client' : client}
            return render(request, "hexafuel_oil_app/fuel_quote.html", args)
        except Exception as e:
            print('EXP', e)
            return render(request, "hexafuel_oil_app/fuel_quote.html")
    
    def post(self, request, *args, **kwargs):
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

            date_time_obj = datetime.datetime.strptime(delivery_date_str, "%Y-%m-%d")


            if date_time_obj < datetime.datetime.now():
                return JsonResponse({"ValidationError": "Choose a latter date."})

        try:
          queryset = ClientInformation.objects.all()
          client_id = queryset.get(auth_user_id_id = request.user.id).id
          delivery_address = queryset.get(auth_user_id_id = request.user.id).address1
          client = queryset.get(auth_user_id_id = request.user.id)
          
          total,cost_per_gallons = self.calculatePrice(request.user.id, queryset.get(auth_user_id_id = request.user.id).state, gallons)
          args = {'client' : client}
          quote = FuelQuote(
            gallons=gallons, 
            deliver_address=delivery_address, 
            delivery_date = delivery_date_str, 
            suggested_price_per_gallons = cost_per_gallons, 
            total_amount_due = total, 
            client_id_id = client_id
          )
          quote.save()

          return render(
              request,
              "hexafuel_oil_app/fuel_quote.html", args
          )
        except Exception as e:
          print('EXP', e)
          return JsonResponse({"AccessError": "Please fill out profile information."})
  

class HistoryView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    permission_required = ("auth.change_user")
    template_name = "hexafuel_oil_app/history.html"

    def get(self, request):
      try:
        clients_queryset = ClientInformation.objects.all()
        client_id = clients_queryset.get(auth_user_id_id = request.user.id).id
        quotes_queryset = FuelQuote.objects.all()
        quotes = quotes_queryset.filter(client_id_id = client_id)
        args = {'quotes' : quotes}
        return render(request, "hexafuel_oil_app/history.html", args)
      except Exception as e:
        print('EXP', e)
        return render(request, "hexafuel_oil_app/history.html")


class ProfileView(LoginRequiredMixin,PermissionRequiredMixin, TemplateView):
    template_name = "hexafuel_oil_app/account_settings.html"
    permission_required = ("auth.change_user")

    def get(self, request):
        try:
            clients_queryset = ClientInformation.objects.all()
            client = clients_queryset.get(auth_user_id_id = request.user.id)
            args = {'client' : client}
            return render(request, "hexafuel_oil_app/account_settings.html", args)
        except Exception as e:
            print('EXP', e)
            return render(request, "hexafuel_oil_app/account_settings.html")

    def post(self, request, *args, **kwargs):
    #    fullname, address1, address2, city, zipcode
        print("REQUEST", request.POST)
        fullname = str(request.POST.get('fullname'))
        add1 = str(request.POST.get('address1'))
        add2 = str(request.POST.get('address2'))
        state = str(request.POST.get('state'))
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
        auth_user_id = request.user.id
        obj, created = ClientInformation.objects.update_or_create(
            auth_user_id_id = auth_user_id,

            defaults = {  
            'auth_user_id_id' : auth_user_id,
            'fullname' : fullname,
            'address1' : add1,
            'address2' : add2,
            'city' : city,
            'state' : state,
            'zipcode' : zipcode
            }
        )
        args = {'messages' : 'Your Profile has been Updated successfully!'} 
        return render(request, 'hexafuel_oil_app/account_settings.html', args)


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


class LogoutView(LoginRequiredMixin, PermissionRequiredMixin, RedirectView):
    permission_required = ("auth.change_user")

    permanent = False
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)