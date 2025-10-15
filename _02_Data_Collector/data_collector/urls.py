from django.urls import path
from . import views

urlpatterns = [
    path('', views.simple_form, name='home'),
    path('form/', views.simple_form, name='form'),
    path('data/', views.show_all_data, name='show_data'),
]