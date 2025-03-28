# Register your models here.
from django.contrib import admin

from apps.project.models import *


@admin.register(EquipamientoDelLaboratorio)
class EquipamientoDelLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        "identificador_del_equipo",
        "nombre_del_equipo",
        "fecha_de_entrada_del_equipo_al_laboratorio",
        "estado_del_equipo",

    )
    list_filter = (
        "fecha_de_entrada_del_equipo_al_laboratorio",
        "estado_del_equipo",
        "fabricante_del_equipo",
        "calibracion_del_equipo",

    )
    search_fields = ("nombre_del_equipo",)
    date_hierarchy = "fecha_de_entrada_del_equipo_al_laboratorio"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(Reactivo)
class ReactivoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_del_reactivo",
        "cantidad_de_disponible",
        "fecha_entrada",
    )
    list_filter = (
        "cantidad_de_disponible",

    )
    date_hierarchy = "fecha_entrada"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(EntradaDeReactivo)
class EntradaDeReactivoAdmin(admin.ModelAdmin):
    list_display = (
        "reactivo",
        "cantidad_de_reactivo",
        "fecha_de_entrada_del_reactivo",

    )
    list_filter = (
        "fecha_de_entrada_del_reactivo",
        "cantidad_de_reactivo",
        "reactivo",

    )
    date_hierarchy = "fecha_de_entrada_del_reactivo"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(SolucionesPreparadas)
class SolucionesPreparadasAdmin(admin.ModelAdmin):
    list_display = (
        "identificador_de_la_solucion_preparada",
        "nombre_de_la_solucion_preparada",
        "cantidad_de_la_solucion_preparada",

    )
    list_filter = (
        "identificador_de_la_solucion_preparada",
        "cantidad_de_la_solucion_preparada",

    )
    search_fields = ("nombre_de_la_solucion_preparada",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
        list_display = (
            "nombre_apellido",
            "ci",
            "rol_del_trabajador",
        )
        list_filter = (
            "rol_del_trabajador",

        )
        search_fields = ("nombre_apellido",)
        ordering = list(list_display).copy()
        list_display_links = list(list_display).copy()


@admin.register(PrepararSoluciones)
class PrepararSolucionesAdmin(admin.ModelAdmin):
    list_display = (
        "fecha_de_preparacion_de_la_solucion",

    )
    list_filter = (
        "fecha_de_preparacion_de_la_solucion",

    )
    date_hierarchy = "fecha_de_preparacion_de_la_solucion"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    # filter_horizontal = [
    #     "reactivo_consumido","soluciones_preparadas_producidas"
    # ]
    

@admin.register(Soluciones_Preparadas_Producidas)
class Soluciones_Preparadas_ProducidasAdmin(admin.ModelAdmin):
    list_display = (
        "soluciones_preparadas",
        "cantidad_de_soluciones_preparada_producidas",

    )
    list_filter = (
        "soluciones_preparadas",
        "cantidad_de_soluciones_preparada_producidas",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(Reactivo_Consumido)
class Reactivo_ConsumidoAdmin(admin.ModelAdmin):
    list_display = (
        "reactivo",
        "cantidad_de_reactivo_consumida",

    )
    list_filter = (
        "reactivo",
        "cantidad_de_reactivo_consumida",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(EnsayoAguaVapor)
class EnsayoAguaVaporAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_ensayo",
        "fecha_del_ensayo",
    )
    list_filter = (
        "nombre_ensayo",

    )
    date_hierarchy = "fecha_del_ensayo"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador",
        "preparar_soluciones",
    ]


    @admin.register(EnsayoDelCombustible)
    class EnsayoDelCombustibleAdmin(admin.ModelAdmin):
        list_display = (
            "nombre_ensayo",
            "fecha_del_ensayo",

        )
        list_filter = (
            "nombre_ensayo",
        )
        date_hierarchy = "fecha_del_ensayo"
        ordering = list(list_display).copy()
        list_display_links = list(list_display).copy()
        filter_horizontal = [
            "trabajador",
            "preparar_soluciones",
        ]


@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):
    list_display = (
        "titulo_del_informe",
        "fecha_del_informe",

    )
    list_filter = (
        "trabajador",
        "ensayo_aguavapor",
        "ensayo_del_combustible",
    )
    date_hierarchy = "fecha_del_informe"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador",
        "preparar_soluciones",
    ]





