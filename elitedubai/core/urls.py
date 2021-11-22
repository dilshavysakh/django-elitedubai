from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fleet',views.fleet,name='fleet'),
    path('contact',views.contact,name='contact'),
    path('services',views.services,name='services'),
]
