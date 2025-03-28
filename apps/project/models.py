from typing import Dict, List

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from rest_framework import serializers
from django.core.validators import RegexValidator

User = get_user_model()

ROL_NAME_ADMIN = "admin"

class EquipamientoDelLaboratorio (models.Model):
    identificador_del_equipo = models.CharField( max_length=255, verbose_name="Identidicador:",unique=True)
    nombre_del_equipo = models.CharField(
        max_length=255,
        verbose_name="Nombre: ",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_]+$',
                message='El nombre del equipo no puede contener carateres especiales'
            )
        ]
    )
    fabricante_del_equipo = models.CharField(max_length=255, verbose_name="Fabricante:")
    descripicion_del_equipo = models.CharField(max_length=255, verbose_name="Descripción del equipo:")
    estado_del_equipo = models.CharField(max_length=255, choices=(("Roto","Roto"),("En uso","En uso")), verbose_name="Estado del equipo:")
    fecha_de_entrada_del_equipo_al_laboratorio = models.DateField(verbose_name="Fecha de entrada:")
    calibracion_del_equipo= models.FloatField(verbose_name= "Calibración:", validators=[MinValueValidator(0.0)])

    class Meta:
        verbose_name= "Equipamientos"
        verbose_name_plural = "Equipamientos"

    def __str__(self):
        return f"{self.nombre_del_equipo} {self.identificador_del_equipo}"

class Reactivo (models.Model):
    nombre_del_reactivo = models.CharField(max_length=255, verbose_name="Nombre del reactivo:")
    cantidad_de_disponible = models.FloatField(verbose_name= "Cantidad de reactivo:", validators=[MinValueValidator(0.0)])
    fecha_entrada = models.DateField(verbose_name="Fecha")
    descripicion = models.CharField(max_length=255, verbose_name="Descripción del reactivo")


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
    nombre_del_trabajador = models.CharField(max_length=255, verbose_name="Nombre del trabajador:")
    ci = models.CharField(max_length=255, verbose_name="Carné de indentidad: ")
    rol_del_trabajador = models.CharField(max_length=255, verbose_name="Rol del trabajador: ")



    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
            return f"{self.nombre_del_trabajador}"

class LibroDeInforme (models.Model):
    tipo = models.CharField(max_length=255, verbose_name="Tipo:")

    class Meta:
        verbose_name = "Libro de Informe"
        verbose_name_plural = "Libros de Informes"

    def __str__(self):
            return f"{self.tipo}"

class Reactivo_Consumido (models.Model):
    cantidad_de_reactivo_consumida = models.FloatField(verbose_name= "Cantidad de React. Consumida:", validators=[MinValueValidator(0.0)])

    reactivo = models.ForeignKey(
        Reactivo,
        on_delete=models.CASCADE,
        verbose_name="Reactivo",
    )
    class Meta:
        verbose_name = "Reactivo consumido"
        verbose_name_plural = "Reactivos consumidos"

    def __str__(self):
        return f"{self.reactivo}{self.cantidad_de_reactivo_consumida}"

class Soluciones_Preparadas_Producidas(models.Model):
    cantidad_de_soluciones_preparada_producidas = models.FloatField(verbose_name= "Cantidad Sol. Prep. Producida:", validators=[MinValueValidator(0.0)])

    soluciones_preparadas = models.ForeignKey(
        SolucionesPreparadas,
        on_delete=models.CASCADE,
        verbose_name="Soluciones preparadas",
    )
    class Meta:
        verbose_name = "Solución prep. producida"
        verbose_name_plural = "Soluciones preparadas producidas"

    def __str__(self):
            return f"{self.soluciones_preparadas}{self.cantidad_de_soluciones_preparada_producidas}"




class PrepararSoluciones(models.Model):
    fecha_de_preparacion_de_la_solucion = models.DateTimeField(verbose_name="Fecha de Prep. de la Sol.:")
    reactivo_consumido = models.ManyToManyField(Reactivo_Consumido, verbose_name="Preparar soluciones")
    soluciones_preparadas_producidas = models.ManyToManyField(Soluciones_Preparadas_Producidas, verbose_name="???")


    class Meta:
        verbose_name = "Preparar solución"
        verbose_name_plural = "Preparar soluciones"

    def __str__(self):
            return f"{self.fecha_de_preparacion_de_la_solucion}"




class EnsayoAguaVapor (models.Model):
    nombre_ensayo = models.CharField( max_length=255, verbose_name="Nombre del ensayo:")
    fecha_del_ensayo = models.DateTimeField(verbose_name="Fecha del ensayo:")
    descripicion_del_ensayo = models.TextField(verbose_name= "Descripción del ensayo")
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")

    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.CASCADE,
        verbose_name="Preparar soluciones",
    )


    class Meta:
        verbose_name = "Ensayo Agua-Vapor"
        verbose_name_plural = "Ensayos Agua-Vapor"

    def __str__(self):
        return f"{self.nombre_ensayo}"

class EnsayoDelCombustible (models.Model):
    nombre_ensayo = models.CharField( max_length=255, verbose_name="Nombre del ensayo:")
    result_determinacion_de_la_viscosidad = models.FloatField(verbose_name="Resultado de la viscosidad", validators=[MinValueValidator(0.0)])
    result_determinacion_de_la_temperatura_de_calentamiento = models.FloatField(verbose_name="Resultado de la Temp. de calentamiento", validators=[MinValueValidator(0.0)])
    result_determinacion_del_valor_calorico = models.FloatField(verbose_name="Resultado del valor calórico", validators=[MinValueValidator(0.0)])
    result_determinacion_de_la_gravedad_especifica = models.FloatField(verbose_name="Resultado de la gravedad específica", validators=[MinValueValidator(0.0)])
    fecha_del_ensayo = models.DateTimeField(verbose_name="Fecha del ensayo:")
    descripicion_del_resultado = models.TextField(verbose_name= "Descripción del resultado")
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")

    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.CASCADE,
        verbose_name="Preparar soluciones",
    )

    class Meta:
        verbose_name = "Ensayo del Combustible"
        verbose_name_plural = "Ensayos del Combustible"

    def __str__(self):
        return f"{self.nombre_ensayo}"


class Informe (models.Model):
    titulo_del_informe= models.CharField( max_length=255, verbose_name="Título del informe:")
    fecha_del_informe = models.DateTimeField(verbose_name="Fecha del informe:")
    descripicion_del_informe = models.TextField(verbose_name= "Descripción del informe")
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")

    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.SET_NULL,
        verbose_name="Preparar Soluciones",
        blank=True,
        null=True
    )

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
        verbose_name="Ensayoo del Combustible",
        blank=True,
        null=True
    )

    libroDeInforme = models.ForeignKey(
        LibroDeInforme,
        on_delete=models.CASCADE,
        verbose_name="Libro de Informe",
    )

    class Meta:
        verbose_name = "Informe"
        verbose_name_plural = "Informes"

    def __str__(self):
            return f"{self.titulo_del_informe}"