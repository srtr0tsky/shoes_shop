from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django import forms
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView)
class RegisterUser(FormView):
    template_name='register_account.html'
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')

    def post(self, request, *args, **kwargs):
        form = super(RegisterUser, self).get_form(form_class=SignUpForm)
        if form.is_valid():
            form.save()
            return super(RegisterUser, self).form_valid(form)
        else:
            return super(RegisterUser, self).form_invalid(form)

