from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
# Views 
class LoginUserTemplateView(TemplateView):
    template_name = 'users/login.html'