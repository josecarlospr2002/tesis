import json
from typing import List

from django.shortcuts import redirect
from django.urls import reverse

from ..models import *
from .util_email_reporte_d import custom_export_report_by_name




def generar_reporte_informe_laboratorio_pdf(modeladmin, request, queryset):
    entidades: List[Informe] = queryset
    lista = []
    for informe in entidades:
        soluciones=[]
        for solucion_preparada in informe.preparar_soluciones.all():
            soluciones_str="reactivos: "
            for reactivo in solucion_preparada.reactivo_consumido.all():
                soluciones_str+=f"{reactivo.reactivo.nombre_del_reactivo} | {reactivo.cantidad_de_reactivo_consumida} "

            soluciones_str += "soluciones: "
            for solucion in solucion_preparada.soluciones_preparadas_producidas.all():
                soluciones_str += f"{solucion.soluciones_preparadas.nombre_de_la_solucion_preparada} | {solucion.cantidad_de_soluciones_preparada_producidas} "

            soluciones.append(soluciones_str)
        hay_agua_vapor=informe.ensayo_aguavapor is not None

        hay_petroleo = informe.ensayo_del_combustible is not None
        data_licencia = {
            "nombre_del_informe": informe.titulo_del_informe,
            "fecha_y_hora": informe.fecha_del_informe,
            "trabajador": ",".join([trabajador.nombre_apellido for trabajador in informe.trabajador.all()]),
            "soluciones_preparadas": ",".join(soluciones),
            "hay_agua_vapor": hay_agua_vapor,
            "hay_petrole": hay_petroleo,
            "descripcion_del_informe": informe.descripicion_del_informe,
        }
        if hay_agua_vapor:
            data_licencia["nombre_ens_aguavapor"]= informe.ensayo_aguavapor.nombre_ensayo
            data_licencia["fecha_hora_de_aguavapor"] = informe.ensayo_aguavapor.fecha_del_ensayo
            data_licencia["descrip_ens_aguavapor"] = informe.ensayo_aguavapor.descripicion_del_ensayo

        if hay_petroleo:
            data_licencia["nombre_ens_combust"]= informe.ensayo_del_combustible.nombre_ensayo
            data_licencia["decha_del_combustible"]= informe.ensayo_del_combustible.fecha_del_ensayo
            data_licencia["result_viscos"]= informe.ensayo_del_combustible.result_determinacion_de_la_viscosidad
            data_licencia["result_temp_calent"]= informe.ensayo_del_combustible.result_determinacion_de_la_temperatura_de_calentamiento
            data_licencia["result_grav_especifica"]= informe.ensayo_del_combustible.result_determinacion_de_la_gravedad_especifica
            data_licencia["result_valor_calorico"]= informe.ensayo_del_combustible.result_determinacion_del_valor_calorico
            data_licencia["descrip_combustible"]= informe.ensayo_del_combustible.descripicion_del_resultado



        lista.append(data_licencia)

    data = {"lista": lista,}

    return custom_export_report_by_name(
        "Informe", data, file="reporte",
    )


generar_reporte_informe_laboratorio_pdf.short_description = (
    "Generar informe"
)
