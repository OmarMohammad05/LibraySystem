from django.urls import path
from . import views
from Users import views as uViews
urlpatterns = [
    path("",views.Home,name='Home'),
    path("View/",views.ViewBooks,name='View'),
    path("Borrow/",views.BorrowBook,name="Borrow"),
    path("Return/",views.ReturnBook,name='Return'),
    path('settings',uViews.settings, name="settings")
]
