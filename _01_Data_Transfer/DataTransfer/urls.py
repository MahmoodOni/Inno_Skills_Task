from django.contrib import admin
from django.urls import path
from .views import transfer_data



urlpatterns = [
    path('admin/', admin.site.urls),
    path('transfer/', transfer_data, name = 'transfer'),
]