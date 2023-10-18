from django.urls import path
from . import views

urlpatterns = [
    path("login" , views.index , name = "index"),
    path("register" , views.register , name = "register"),
    path("add" , views.add , name = "add"), 
    path("view" , views.view ,name = "view")
]