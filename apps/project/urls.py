from django.urls import include, path
from .views import *

urlpatterns = [
    path("admin/soluciones/", soluciones_view,name="soluciones"),
]
