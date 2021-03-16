from django.test import TestCase
from .views import FormView
from django.test import Client

c = Client()
request = c.post(
    "/form/",
    {
        "gallons": ["4"],
        "delivery-address": [""],
        "delivery-date": ["2021-03-18"],
        "Calculate Cost": ["Calculate Cost"],
    },
)


class FormViewTest(TestCase):
    @classmethod
    def test_view_validations(self):
        # response = self.client.post("/form/")
        # print("self", self)
        # print("self", self.__dict__)
        # print("response", response)
        # print("response.status_code", response.status_code)
        # self.assertEqual(response.status_code, 200)
        pass
