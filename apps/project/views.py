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

from apps.project.utils.constante_del_viscosimetro import get_valor_bulbo
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
            try:
                # Intenta obtener el valor de bulbo para el número dado
                bulbo = get_valor_bulbo(int(numero))

                # Prepara los datos para mostrar en la plantilla
                datos = {
                    "numero": numero,
                    "bulbo": bulbo,
                }

                return render(request, "admin/soluciones/capilares.html", datos)
            except Exception as e:
                print(f"Error: {e}")
                return render(request, "admin/soluciones/capilares.html", {
                    "error": "No se encontraron datos para el número ingresado."
                })

    return render(request, "admin/soluciones/capilares.html")
