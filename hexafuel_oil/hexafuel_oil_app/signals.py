from django.dispatch import Signal #pragma: no cover


user_logged_in = Signal(providing_args=['instance', 'request']) #pragma: no cover