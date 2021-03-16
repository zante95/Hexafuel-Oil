from django.test import RequestFactory, TestCase, Client
from django.urls import reverse

from .views import ProfileView

no_error_test = Client()
response = no_error_test.post(
    "/profile/",
    {
    "fullname": [""],
    "add1": ["14455 Country Place Dr"],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

fullname_test = Client()
response = fullname_test.post(
    "/profile/",
    {
    "fullname": [""],
    "add1": ["14455 Country Place Dr"],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

add1_test = Client()
response = add1_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": [""],
    "add2": ["318"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

zip_test = Client()
response = zip_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["desdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgads"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

add1_test = Client()
response = add1_test.post(
    "/profile/",
    {
    "fullname": ["Carlos Suarez"],
    "add1": ["14455 Country Place Dr"],
    "add2": ["desdsfgdsfdsfhrdshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgadshfgdfdfagdfgads"],
    "city": ["Houston"],
    "zipcode": ["77449"],
    "is_Submitted": ["true"]
    },
)

class ProfileViewTest(TestCase):
    @classmethod
    def test_no_error(self):
        pass
    def test_fullname(self):
        pass
    def test_add1(self):
        pass
    def test_add2(self):
        pass
    def test_zip(self):
        pass