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
