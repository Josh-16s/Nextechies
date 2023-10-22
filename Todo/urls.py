from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("" , views.index , name = "index"), 
    path("login" , views.index , name = "index"),
    path("register" , views.register , name = "register"),
    path("add" , views.add , name = "add"), 
    path("view" , views.view ,name = "view")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)