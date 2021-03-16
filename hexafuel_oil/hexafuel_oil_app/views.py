from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from django.views.generic import TemplateView

# Create your views here.
def home(request):
    return render(request, "hexafuel_oil_app/login.html")


class FormView(TemplateView):
    template_name = "hexafuel_oil_app/fuel_quote.html"

    def post(self, request, *args, **kwargs):
        # def post(request, format=None, *args, **kwargs):
        # print("REQUEST", request.POST)
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


def register(request):

    return render(request, "hexafuel_oil_app/register.html")


def history(request):
    return render(request, "hexafuel_oil_app/history.html")


def profile(request):
    return render(request, "hexafuel_oil_app/account_settings.html")


# def myPrint1(my_str):
#     print(my_str)
#     return 1


# def myPrint2(my_str):
#     print(my_str)
#     return 1


# myPrint1("HERE")
# myPrint2("HERE")

# my_dict = {
#     "gallons": ["3"],
#     "delivery-address": [""],
#     "delivery-date": ["2021-02-25"],
#     "Calculate Cost": ["Calculate Cost"],
# }
# q_dict = QueryDict("", mutable=True)
# q_dict.update(my_dict)

# form(q_dict)