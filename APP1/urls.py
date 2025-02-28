from django.urls import path
from . import  views

urlpatterns=[
    path('',views.home,name="home"),
    path('application',views.application,name="application"),
    path('contact/', views.contact_view, name='contact'),
]