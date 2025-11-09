from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.Register,name="register"),
    path("",views.LogIn,name='logIn'),
    path("logOut",views.LogOut,name='logOut'),
    path("settings",views.settings,name='settings'),
]
