from django.urls import path
from .views import HomePageView,AboutPageView,ServicesPageView,ContactUsPageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('About/', AboutPageView.as_view(), name='about'),
    path('Services/', ServicesPageView.as_view(), name='services'),
    path('Contact Us/', ContactUsPageView.as_view(), name='contact us')
]