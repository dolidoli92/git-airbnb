from django.views import View
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        passwd = form.cleaned_data.get("passwd")
        user = authenticate(self.request, username=email, password=passwd)
        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


def log_out(request):
    logout(request)

    return redirect(reverse("core:home"))


class SignupView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("core:home")
    initial = {
        "first_name": "Yangwoo",
        "last_name": "Kim",
        "email": "dolidoli92@onhyang.co.kr",
    }

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
