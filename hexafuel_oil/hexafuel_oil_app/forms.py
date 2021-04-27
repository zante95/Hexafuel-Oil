from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.models import Permission
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        # print('LOGIN REQUEST', request.POST)
        self.user = user
        return data

class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    email = forms.EmailField(max_length=254, required=True, validators=[validate_email,])
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email') #'full_name',)

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         #raise forms.ValidationError("Passwords don't match")
    #         args = {'messages' : "Passwords don't match 2"}
    #         return render(request, 'hexafuel_oil_app/register2.html', args)
    #     return password2

    def save(self, commit=True):
        #check if passwords match each other
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2 or len(self.cleaned_data.get("username")) >= 10:
            args = {'messages' : 'Passwords do not match 2'}
            print('Passwords do not match or username exceeds 10 characters')
            return redirect('hexafuel_oil_app/register2.html', args)

        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        #user.active = True
        
        permission = Permission.objects.get(id='14')

        if commit:
            user.save()
            user.user_permissions.add(permission)
        
        return user