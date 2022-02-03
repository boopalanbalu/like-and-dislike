from xml.etree.ElementInclude import include
from django.urls import path , include

urlpatterns = [
    path("", include('ajax_app.urls')), 
]
