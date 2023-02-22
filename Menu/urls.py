from django.urls import path

from Menu.views import MenuIndexView


app_name = 'menu'

urlpatterns = [
    path('menu', MenuIndexView.as_view(), name='index')
]