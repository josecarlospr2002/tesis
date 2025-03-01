from django.http import JsonResponse
from django.utils import timezone
from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema,
    extend_schema_view,
    inline_serializer,
)
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from django.shortcuts import render
from config.utils.utils_view import (
    BaseGenericAPIView,
    BaseListAPIView,
    BaseModelAPIView,
    BaseModelViewSet,
)


def soluciones_view(request):
    return render(request, "admin/soluciones/soluciones.html")

def capilares_view(request):
    if request.method == "POST":
        numero = request.POST.get('numero', None)
        if numero is not None:
            return render(request, "admin/soluciones/capilares.html",{
            "numero":numero
        })

    return render(request, "admin/soluciones/capilares.html")