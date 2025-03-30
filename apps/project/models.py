from typing import Dict, List

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from rest_framework import serializers
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

User = get_user_model()

ROL_NAME_ADMIN = "admin"
ROL_NAME_DIRECT = "director"
ROL_NAME_TRABAJ = "trabajador"
ROL_NAME_USER = "ususario"


class EquipamientoDelLaboratorio (models.Model):
    identificador_del_equipo = models.CharField( max_length=255, verbose_name="Identidicador:",unique=True)
    nombre_del_equipo = models.CharField(
        max_length=255,
        verbose_name="Nombre: ",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_ ]+$',
                message='El nombre del equipo no puede contener carateres especiales'
            )
        ]
    )
    fabricante_del_equipo = models.CharField(max_length=255, verbose_name="Fabricante:")
    fecha_de_entrada_del_equipo_al_laboratorio = models.DateField(verbose_name="Fecha de entrada:")
    estado_del_equipo = models.CharField(max_length=255, choices=(("Roto","Roto"),("En uso","En uso")), verbose_name="Estado del equipo:")
    cantidad_actual = models.IntegerField(verbose_name="Cantidad actual:", validators=[MinValueValidator(0)],  blank=True, null=True)
    calibracion_del_equipo= models.FloatField(verbose_name= "Calibración:", validators=[MinValueValidator(0.0)])
    descripicion_del_equipo = models.TextField(verbose_name="Descripción del equipo:")

    class Meta:
        verbose_name= "Equipamiento del laboratorio"
        verbose_name_plural = "Equipamientos del laboratorio"

    def __str__(self):
        return f"{self.nombre_del_equipo} {self.identificador_del_equipo}"

class Reactivo (models.Model):
    nombre_del_reactivo = models.CharField(max_length=255, verbose_name="Nombre del reactivo:")
    cantidad_de_disponible = models.FloatField(verbose_name= "Cantidad de reactivo:", validators=[MinValueValidator(0.0)])
    fecha_entrada = models.DateField(verbose_name="Fecha")
    descripicion_del_reactivo = models.TextField(verbose_name="Descripción del reactivo:")


    class Meta:
        verbose_name = "Reactivo"
        verbose_name_plural = "Reactivos"

    def __str__(self):
        return f"{self.nombre_del_reactivo}"

class EntradaDeReactivo (models.Model):
    fecha_de_entrada_del_reactivo = models.DateField(verbose_name="Fecha de entrada:")
    cantidad_de_reactivo= models.FloatField(verbose_name= "Cantidad de reactivo:", validators=[MinValueValidator(0.0)])
    reactivo = models.ForeignKey(
        Reactivo,
        on_delete=models.CASCADE,
        verbose_name="Reactivo",
    )

    class Meta:
        verbose_name = "Entrada de reactivo"
        verbose_name_plural = "Entrada de reactivos"

    def __str__(self):
        return f"{self.reactivo}"


class SolucionesPreparadas(models.Model):
    identificador_de_la_solucion_preparada = models.CharField( max_length=255, verbose_name="Identidicador:")
    nombre_de_la_solucion_preparada = models.CharField(max_length=255, verbose_name="Nombre de la Sol. Prep:")
    cantidad_de_la_solucion_preparada= models.FloatField(verbose_name= "Cantidad de Sol. Prep:", validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = "Solución preparada"
        verbose_name_plural = "Soluciones preparadas"

    def __str__(self):
            return f"{self.nombre_de_la_solucion_preparada}{self.identificador_de_la_solucion_preparada}"

class Trabajador(models.Model):
    nombre_apellido = models.CharField(
        max_length=255,
        verbose_name="Nombre del trabajador:",
        validators=[
            RegexValidator(
                regex=r'^[A-Z][a-zñÑáéíóúÁÉÍÓÚ]*(?:\s[A-Z][a-zñÑáéíóúÁÉÍÓÚ]*)*$',
                message='El nombre y los apellidos deben comenzar con mayúscula, este campo solo puede contener letras'
            )
        ]
    )
    ci = models.CharField(
        max_length=11,
        verbose_name="Carné de identidad:",
        validators=[
            RegexValidator(
                regex=r'^\d{11}$',
                message='El carné de identidad debe contener exactamente 11 números y no contiene ningún carácter especial'
            )
        ]
    )
    rol_del_trabajador = models.CharField(
        max_length=255,
        verbose_name="Ocupación o cargo: ",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$',
                message='Este campo solo puede contener letras'
            )
        ]
    )


    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
            return f"{self.nombre_apellido}"



class Reactivo_Consumido (models.Model):

    reactivo = models.ForeignKey(
        Reactivo,
        on_delete=models.CASCADE,
        verbose_name="Reactivo",
    ) 
    cantidad_de_reactivo_consumida = models.FloatField(verbose_name= "Cantidad de React. Consumida:", validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = "Reactivo consumido"
        verbose_name_plural = "Reactivos consumidos"

    def __str__(self):
        return f"{self.reactivo}{self.cantidad_de_reactivo_consumida}"

class Soluciones_Preparadas_Producidas(models.Model):

    soluciones_preparadas = models.ForeignKey(
        SolucionesPreparadas,
        on_delete=models.CASCADE,
        verbose_name="Soluciones preparadas",
    )
    cantidad_de_soluciones_preparada_producidas = models.FloatField(verbose_name= "Cantidad Sol. Prep. Producida:", validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name = "Solución preparada producida"
        verbose_name_plural = "Soluciones preparadas producidas"

    def __str__(self):
            return f"{self.soluciones_preparadas.nombre_de_la_solucion_preparada}{self.cantidad_de_soluciones_preparada_producidas}"




class PrepararSoluciones(models.Model):
    fecha_de_preparacion_de_la_solucion = models.DateTimeField(verbose_name="Fecha de Prep. de la Sol.:")
    reactivo_consumido = models.ManyToManyField(Reactivo_Consumido, verbose_name="Reactivo consumido")
    soluciones_preparadas_producidas = models.ManyToManyField(Soluciones_Preparadas_Producidas, verbose_name="Soluciones preparadas producidas")


    class Meta:
        verbose_name = "Preparar solución"
        verbose_name_plural = "Preparar soluciones"

    def __str__(self):
            soluciones=[
                f"{solucion.soluciones_preparadas.nombre_de_la_solucion_preparada}"
                for solucion in self.soluciones_preparadas_producidas.all()
                ]
            return f"{' : '.join(soluciones)}"


class EnsayoAguaVapor (models.Model):
    nombre_ensayo = models.CharField( max_length=255, verbose_name="Nombre del ensayo:")
    fecha_del_ensayo = models.DateTimeField(verbose_name="Fecha del ensayo:")
   
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")
    
    preparar_soluciones = models.ManyToManyField(PrepararSoluciones, verbose_name= "Soluciones preparadas para este ensaayo")
    descripicion_del_ensayo = models.TextField(verbose_name= "Descripción del ensayo", blank=True, null=True)

    class Meta:
        verbose_name = "Ensayo Agua-Vapor"
        verbose_name_plural = "Ensayos Agua-Vapor"

    def __str__(self):
        return f"{self.nombre_ensayo}"


class EnsayoDelCombustible (models.Model):
    nombre_ensayo = models.CharField( max_length=255, verbose_name="Nombre del ensayo:")
    fecha_del_ensayo = models.DateTimeField(verbose_name="Fecha del ensayo:")
    result_determinacion_de_la_viscosidad = models.FloatField(verbose_name="Resultado de la viscosidad", validators=[MinValueValidator(0.0)])
    result_determinacion_de_la_temperatura_de_calentamiento = models.FloatField(verbose_name="Resultado de la Temp. de calentamiento", validators=[MinValueValidator(0.0)])
    result_determinacion_del_valor_calorico = models.FloatField(verbose_name="Resultado del valor calórico", validators=[MinValueValidator(0.0)])
    result_determinacion_de_la_gravedad_especifica = models.FloatField(verbose_name="Resultado de la gravedad específica", validators=[MinValueValidator(0.0)])
   
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")
    preparar_soluciones = models.ManyToManyField(PrepararSoluciones, verbose_name= "Soluciones preparadas para este ensaayo")

    descripicion_del_resultado = models.TextField(verbose_name= "Descripción del resultado", blank=True, null=True)


    class Meta:
        verbose_name = "Ensayo del Combustible"
        verbose_name_plural = "Ensayos del Combustible"

    def __str__(self):
        return f"{self.nombre_ensayo}"


class Informe (models.Model):
    titulo_del_informe= models.CharField( max_length=255, verbose_name="Título del informe:")
    fecha_del_informe = models.DateTimeField(verbose_name="Fecha del informe:")
    
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")
    preparar_soluciones = models.ManyToManyField(PrepararSoluciones, verbose_name= "Soluciones preparadas para este ensaayo")

    ensayo_aguavapor = models.ForeignKey(
        EnsayoAguaVapor,
        on_delete=models.SET_NULL,
        verbose_name="Ensayo Agua-Vapor",
        blank=True,
        null=True
    )

    ensayo_del_combustible = models.ForeignKey(
        EnsayoDelCombustible,
        on_delete=models.SET_NULL,
        verbose_name="Ensayo del Combustible",
        blank=True,
        null=True
    )

    descripicion_del_informe = models.TextField(verbose_name= "Descripción del informe", blank=True, null=True)

    def clean(self):
        if not self.ensayo_aguavapor and not self.ensayo_del_combustible:
            raise ValidationError("Debe seleccionar al menos un tipo de ensayo (Agua-Vapor o Combustible)")
        return super().clean()

    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"

    def __str__(self):
            return f"{self.titulo_del_informe}"