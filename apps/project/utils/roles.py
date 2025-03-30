from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django_reportbroD.models import ReportDefinition, ReportRequest

from apps.project.models import (
    ROL_NAME_ADMIN,  
    ROL_NAME_DIRECT,
    ROL_NAME_TRABAJ,
    ROL_NAME_USER,
    EquipamientoDelLaboratorio,
    Reactivo,
    EntradaDeReactivo,
    SolucionesPreparadas,
    Trabajador,
    Reactivo_Consumido,
    Soluciones_Preparadas_Producidas,
    PrepararSoluciones,
    EnsayoAguaVapor,
    EnsayoDelCombustible,
    Informe
)

from config.utils.utils_permission import crear_rol

User = get_user_model()


def crear_roles_django_default():
    crear_rol(
        lista_modelos=[
            ReportDefinition,
            User,
            Group,
            Permission,
            ReportRequest
        ],
        lista_modelos_solo_update=[],
        lista_modelos_solo_create=[],
        lista_modelos_solo_view=[],
        nombre_rol=ROL_NAME_ADMIN,
    )
    crear_rol(
        lista_modelos=[
            EquipamientoDelLaboratorio,
            Reactivo,
            EntradaDeReactivo,
            SolucionesPreparadas,
            Reactivo_Consumido,
            Soluciones_Preparadas_Producidas,
            PrepararSoluciones,
            EnsayoAguaVapor,
            EnsayoDelCombustible,
            Informe

        ],
        lista_modelos_solo_view=[
            Trabajador,
        ],
        nombre_rol=ROL_NAME_TRABAJ,
    )
    crear_rol(
        nombre_rol=ROL_NAME_USER,
        lista_modelos_solo_view=[
            EquipamientoDelLaboratorio,
            Reactivo,
            EntradaDeReactivo,
            SolucionesPreparadas,
            Reactivo_Consumido,
            Soluciones_Preparadas_Producidas,
            PrepararSoluciones,
            EnsayoAguaVapor,
            EnsayoDelCombustible,
            Informe
        ],
    )
    crear_rol(
        lista_modelos=[
            Trabajador,
            EnsayoAguaVapor,
            EnsayoDelCombustible,
            Informe

        ],
        lista_modelos_solo_view=[
            EquipamientoDelLaboratorio,
            Reactivo,
            EntradaDeReactivo,
            SolucionesPreparadas,
            Reactivo_Consumido,
            Soluciones_Preparadas_Producidas,
            PrepararSoluciones,
        ],
        nombre_rol=ROL_NAME_DIRECT,
    )
