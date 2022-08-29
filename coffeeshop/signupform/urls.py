from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup', views.Signup, name='signup'),
    path('thanks', views.Thanks, name='thanks')
]