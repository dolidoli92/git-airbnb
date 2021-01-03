from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)

    # clean_<fieldname>()
    def clean(self):
        email = self.cleaned_data.get("email")
        passwd = self.cleaned_data.get("passwd")

        try:
            user = models.User.objects.get(email=email)

            if user.check_password(passwd):
                return self.cleaned_data
            else:
                self.add_error("passwd", forms.ValidationError("Password is error."))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist."))


class SignupForm(forms.Form):
    # basic information
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    passwd1 = forms.CharField(widget=forms.PasswordInput)
    passwd2 = forms.CharField(widget=forms.PasswordInput, label="Confirmed Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with email")
        except models.User.DoesNotExist:
            return email

    def clean_passwd2(self):
        passwd1 = self.cleaned_data.get("passwd1")
        passwd2 = self.cleaned_data.get("passwd2")

        if passwd1 != passwd2:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return passwd1

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        passwd1 = self.cleaned_data.get("passwd1")
        user = models.User.objects.create_user(email, email, passwd1)

        user.first_name = first_name
        user.last_name = last_name
        user.save()
