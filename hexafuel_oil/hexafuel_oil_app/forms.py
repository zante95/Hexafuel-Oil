from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#from django.utils.safestring import mark_safe
#from .models import EmailActivation, GuestEmail
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        username  = data.get("username")
        password  = data.get("password")
        # qs = User.objects.filter(username=username)
        # if qs.exists():
        #     # user email is registered, check active/
        #     not_active = qs.filter(is_active=False)
        #     if not_active.exists():
        #         ## not active, check email activation
        #         link = reverse("account:resend-activation")
        #         reconfirm_msg = """Go to <a href='{resend_link}'>
        #         resend confirmation email</a>.
        #         """.format(resend_link = link)
        #         confirm_email = EmailActivation.objects.filter(email=email)
        #         is_confirmable = confirm_email.confirmable().exists()
        #         if is_confirmable:
        #             msg1 = "Please check your email to confirm your account or " + reconfirm_msg.lower()
        #             raise forms.ValidationError(mark_safe(msg1))
        #         email_confirm_exists = EmailActivation.objects.email_exists(email).exists()
        #         if email_confirm_exists:
        #             msg2 = "Email not confirmed. " + reconfirm_msg
        #             raise forms.ValidationError(mark_safe(msg2))
        #         if not is_confirmable and not email_confirm_exists:
        #             raise forms.ValidationError("This user is inactive.")
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data

class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    # for custom validator: (be sure to assign the function on the validators attribute of the related field)
    # def custom_validate_email(value):
    #     if <custom_check>:
    #         raise ValidationError('Email format is incorrect')

    email = forms.EmailField(max_length=254, required=True, validators=[validate_email,])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email') #'full_name',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        # obj = EmailActivation.objects.create(user=user)
        # obj.send_activation_email()
        if commit:
            user.save()
        return user