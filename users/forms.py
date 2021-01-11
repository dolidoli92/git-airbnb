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


class SignupForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name")

    email = forms.EmailField()
    passwd1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    passwd2 = forms.CharField(widget=forms.PasswordInput, label="Confirmed Password")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            print("working?")
            raise forms.ValidationError("User already exists with that email")
        except models.User.DoesNotExist:
            return email

    def clean_passwd2(self):
        passwd1 = self.cleaned_data.get("passwd1")
        passwd2 = self.cleaned_data.get("passwd2")

        if passwd1 != passwd2:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return passwd1

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        passwd1 = self.cleaned_data.get("passwd1")
        user.email = email
        user.username = email
        user.set_password(passwd1)

        user.save()
