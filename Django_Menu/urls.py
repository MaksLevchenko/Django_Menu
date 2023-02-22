
from django.contrib import admin
from django.urls import path, include

from Menu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Menu.urls')),
]
