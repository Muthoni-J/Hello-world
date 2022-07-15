from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class HomePageView(TemplateView): template_name = 'Home.html'
class AboutPageView(TemplateView): template_name = 'About.html'
class ServicesPageView(TemplateView): template_name = 'Services.html'
class ContactUsPageView(TemplateView): template_name = 'Contact Us.html'
