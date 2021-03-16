from django.test import RequestFactory, TestCase
from .views import FormView


# class FormViewTest(TestCase):
#     def test_environment_set_in_context(self):
#         request = RequestFactory().get("/")
#         view = FormView()
#         view.setup(request)

#         context = view.get_context_data()
#         self.assertIn("environment", context)
#         # https://docs.djangoproject.com/en/3.1/topics/testing/overview/
