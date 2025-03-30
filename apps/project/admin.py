# Register your models here.
from django.contrib import admin

from apps.project.models import *
from apps.project.utils.utils_reportes_d import generar_reporte_informe_laboratorio_pdf
from django.utils.safestring import mark_safe


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
    def get_trabajadores(self, obj):
        trabajador = [trabajador.nombre_apellido for trabajador in obj.trabajador.all()]
        return mark_safe("<br>\n".join(trabajador))

    get_trabajadores.short_description = "Trabajador/res"
   
    list_display = (
        "nombre_ensayo",
        "fecha_del_ensayo",
        "get_trabajadores",
    )
    list_filter = (
        "nombre_ensayo",

    )
    date_hierarchy = "fecha_del_ensayo"
    ordering = (
        "nombre_ensayo",
        "fecha_del_ensayo",
       
    )
    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador",
        "preparar_soluciones",
    ]

# @admin.register(Cuadro)
# class CuadroAdmin(admin.ModelAdmin):
#     def get_cargos_sin_cubrir(self, obj):
#         cargos = [cargo.cargo for cargo in obj.cargosincubrir_set.all()]
#         return mark_safe("<br>\n".join(cargos))

#     get_cargos_sin_cubrir.short_description = "Cargos sin Cubrir"

#     list_display = ("empresa", "aprobada", "cubierta", "get_cargos_sin_cubrir")

@admin.register(EnsayoDelCombustible)
class EnsayoDelCombustibleAdmin(admin.ModelAdmin):

    def get_trabajadores(self, obj):
        trabajador = [trabajador.nombre_apellido for trabajador in obj.trabajador.all()]
        return mark_safe("<br>\n".join(trabajador))

    get_trabajadores.short_description = "Trabajador/res"        
    
    list_display = (
        "nombre_ensayo",
        "fecha_del_ensayo",
        "get_trabajadores",

    )
    list_filter = (
        "nombre_ensayo",
    )
    date_hierarchy = "fecha_del_ensayo"
    ordering = (
        "nombre_ensayo",
        "fecha_del_ensayo",
    )

    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador",
        "preparar_soluciones",
    ]


@admin.register(Informe)
class InformeAdmin(admin.ModelAdmin):

    def get_trabajadores(self, obj):
        trabajador = [trabajador.nombre_apellido for trabajador in obj.trabajador.all()]
        return mark_safe("<br>\n".join(trabajador))

    get_trabajadores.short_description = "Trabajador/res"        

    list_display = (
        "titulo_del_informe",
        "fecha_del_informe",
        "get_trabajadores",

    )
    list_filter = (
        "trabajador",
        "ensayo_aguavapor",
        "ensayo_del_combustible",
    )
    date_hierarchy = "fecha_del_informe"
    ordering = (
        "titulo_del_informe",
        "fecha_del_informe",

    )
    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador",
        "preparar_soluciones",
    ]
    actions = [generar_reporte_informe_laboratorio_pdf]





