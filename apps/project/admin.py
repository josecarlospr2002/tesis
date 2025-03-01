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
        "cantidad_de_reactivo",
    )
    list_filter = (
        "cantidad_de_reactivo",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(EntradaDeReactivo)
class EntradaDeReactivoAdmin(admin.ModelAdmin):
    list_display = (
        "fecha_de_entrada_del_reactivo",
        "reactivo",
        "cantidad_de_reactivo",

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
            "nombre_del_trabajador",

        )
        search_fields = ("nombre_del_trabajador",)
        ordering = list(list_display).copy()
        list_display_links = list(list_display).copy()

@admin.register(LibroDeRegistroDeOperacione)
class LibroDeRegistroDeOperacioneAdmin(admin.ModelAdmin):
    list_display = (
        "tipo",
    )
    search_fields = ("tipo",)
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

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_del_cliente",

    )
    search_fields = ("nombre_del_cliente",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(Muestra)
class MuestraAdmin(admin.ModelAdmin):
    list_display = (
        "identificador_de_la_muestra",
        "nombre_de_la_muestra",
        "cantidad_de_la_muestra",
        "cliente",

    )
    list_filter = (
        "identificador_de_la_muestra",
        "cantidad_de_la_muestra",
        "cliente",

    )
    search_fields = ("nombre_de_la_muestrad",)
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDeLaGravedadEspecifica)
class DeterminacionDeLaGravedadEspecificaAdmin(admin.ModelAdmin):
    list_display = (
        "temperatura",
        "gravedad_especifica_resultante",
        "resultado_en_grado_API",

    )
    list_filter = (
        "temperatura",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDeLaTemperaturaDeCalentamiento)
class DeterminacionDeLaTemperaturaDeCalentamientoAdmin(admin.ModelAdmin):
    list_display = (
        "temperatura_resultante",
        "viscosidad_resultante",

    )
    list_filter = (
        "temperatura_resultante",
        "viscosidad_resultante",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDeLaViscosidad)
class DeterminacionDeLaViscosidadAdmin(admin.ModelAdmin):
    list_display = (
        "viscosidad",
        "tiempo_de_inicio",
        "tiempo_de_final",

    )
    list_filter = (
        "viscosidad",
        "tiempo_de_inicio",
        "tiempo_de_final",

    )
    date_hierarchy = "tiempo_de_inicio"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDelValorCaloricoSuperior_Calorimetro)
class DeterminacionDelValorCaloricoSuperior_CalorimetroAdmin(admin.ModelAdmin):
    list_display = (
        "temperatura_introducida",
        "valor_calorico_superior_resultante",

    )
    list_filter = (
        "temperatura_introducida",
        "valor_calorico_superior_resultante",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDelValorCaloricoSuperior_Algoritmo)
class DeterminacionDelValorCaloricoSuperior_AlgoritmoAdmin(admin.ModelAdmin):
    list_display = (
        "valor_calorico_superior_resultante",
        "gravedad_especifica_del_combustible",
        "porcentaje_de_agua",

    )
    list_filter = (
        "valor_calorico_superior_resultante",
        "gravedad_especifica_del_combustible",
        "porcentaje_de_agua",
    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()

@admin.register(DeterminacionDelValorCaloricoSuperior)
class DeterminacionDelValorCaloricoSuperiorAdmin(admin.ModelAdmin):
    list_display = (
        "esta_roto",
        "determinacion_del_valor_calorico_superior_Calorimetro",
        "determinacion_del_valor_calorico_superior_Calorimetro",

    )
    list_filter = (
        "esta_roto",

    )
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()


@admin.register(RegistroDeOperacion)
class RegistroDeOperacionAdmin(admin.ModelAdmin):
    list_display = (
        "identificador_del_registro_de_operacion",
        "fecha_de_registro_de_operacion",

    )
    list_filter = (
        "fecha_de_registro_de_operacion",

    )
    date_hierarchy = "fecha_de_registro_de_operacion"
    ordering = list(list_display).copy()
    list_display_links = list(list_display).copy()
    filter_horizontal = [
        "trabajador"
    ]




