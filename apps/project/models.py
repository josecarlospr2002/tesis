from typing import Dict, List

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from rest_framework import serializers


User = get_user_model()

ROL_NAME_ADMIN = "admin"

class EquipamientoDelLaboratorio (models.Model):
    identificador_del_equipo = models.CharField( max_length=255, verbose_name="Identidicador:")
    nombre_del_equipo = models.CharField(max_length=255, verbose_name="Nombre: ")
    fabricante_del_equipo = models.CharField(max_length=255, verbose_name="Fabricante:")
    descripicion_del_equipo = models.CharField(max_length=255, verbose_name="Descripción del equipo:")
    estado_del_equipo = models.CharField(max_length=255, choices=(("Roto","Roto"),("En uso","En uso")), verbose_name="Estado del equipo:")
    fecha_de_entrada_del_equipo_al_laboratorio = models.DateField(verbose_name="Fecha de entrada:")
    calibracion_del_equipo= models.FloatField(verbose_name= "Calibración:")

    class Meta:
        verbose_name= "Equipamientos"
        verbose_name_plural = "Equipamientos"

    def __str__(self):
        return f"{self.nombre_del_equipo} {self.identificador_del_equipo}"

class Reactivo (models.Model):
    nombre_del_reactivo = models.CharField(max_length=255, verbose_name="Nombre del reactivo:")
    cantidad_de_reactivo = models.FloatField(verbose_name= "Cantidad de reactivo:")

    class Meta:
        verbose_name = "Reactivo"
        verbose_name_plural = "Reactivos"

    def __str__(self):
        return f"{self.nombre_del_reactivo}"

class EntradaDeReactivo (models.Model):
    fecha_de_entrada_del_reactivo = models.DateField(verbose_name="Fecha de entrada:")
    cantidad_de_reactivo= models.FloatField(verbose_name= "Cantidad de reactivo:")
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
    cantidad_de_la_solucion_preparada= models.FloatField(verbose_name= "Cantidad de Sol. Prep:")

    class Meta:
        verbose_name = "Solución preparada"
        verbose_name_plural = "Soluciones preparadas"

    def __str__(self):
            return f"{self.nombre_de_la_solucion_preparada}{self.identificador_de_la_solucion_preparada}"

class Trabajador(models.Model):
    nombre_del_trabajador = models.CharField(max_length=255, verbose_name="Nombre del trabajador:")

    class Meta:
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"

    def __str__(self):
            return f"{self.nombre_del_trabajador}"

class LibroDeRegistroDeOperacione (models.Model):
    tipo = models.CharField(max_length=255, verbose_name="Tipo:")

    class Meta:
        verbose_name = "Libro Registro Operaciones"
        verbose_name_plural = "Libros Registros Operaciones"

    def __str__(self):
            return f"{self.tipo}"


class PrepararSoluciones(models.Model):
    fecha_de_preparacion_de_la_solucion = models.DateField(verbose_name="Fecha de Prep. de la Sol.:")

    class Meta:
        verbose_name = "Preparar solución"
        verbose_name_plural = "Preparar soluciones"

    def __str__(self):
            return f"{self.registro_de_operacion}"


class Soluciones_Preparadas_Producidas(models.Model):
    cantidad_de_soluciones_preparada_producidas = models.FloatField(verbose_name= "Cantidad Sol. Prep. Producida:")
    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.CASCADE,
        verbose_name="Preparar soluciones",
    )
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


class Reactivo_Consumido (models.Model):
    cantidad_de_reactivo_consumida = models.FloatField(verbose_name= "Cantidad de React. Consumida:")
    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.CASCADE,
        verbose_name="Preparar soluciones",
    )
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


class Cliente(models.Model):
    nombre_del_cliente = models.CharField(max_length=255, verbose_name="Nombre del cliente: ")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.nombre_del_cliente}"

class Muestra(models.Model):
    identificador_de_la_muestra = models.CharField( max_length=255, verbose_name="Identidicador de la muestra: ")
    nombre_de_la_muestra = models.CharField(max_length=255, verbose_name="Nombre de la muestra: ")
    cantidad_de_la_muestra = models.FloatField(verbose_name= "Cantidad de muestra: ")
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name="Cliente",
    )

    class Meta:
        verbose_name = "Muestra"
        verbose_name_plural = "Muestras"

    def __str__(self):
        return f"{self.nombre_de_la_muestra}{self.identificador_de_la_muestra}"


class DeterminacionDeLaGravedadEspecifica (models.Model):
    temperatura = models.FloatField(verbose_name= "Temperatura:")
    gravedad_especifica_resultante = models.FloatField(verbose_name= "Grav. Específica Result:")
    resultado_en_grado_API   = models.FloatField(verbose_name= "Gado API:")

    class Meta:
        verbose_name = "Det. Gravedad Especifica"
        verbose_name_plural = "Det. Gravedades Especificas"

    def __str__(self):
        return f"{self.gravedad_especifica_resultante}{self.temperatura}"

class DeterminacionDeLaTemperaturaDeCalentamiento (models.Model):
    temperatura_resultante = models.FloatField(verbose_name= "Temperatura Result:")
    viscosidad_resultante = models.FloatField(verbose_name= "Viscosidad Result:")

    class Meta:
        verbose_name = "Det. Temp de Calentamiento"
        verbose_name_plural = "Det. Temps de Calentamiento"

    def __str__(self):
        return f"{self.temperatura_resultante}{self.viscosidad_resultante}"


class DeterminacionDeLaViscosidad(models.Model):
    viscosidad = models.FloatField(verbose_name="Viscosidad Result:")
    tiempo_de_inicio = models.DateField (verbose_name= "Tiempo Inicio:")
    tiempo_de_final = models.DateField (verbose_name= "Tiempo Final:")

    class Meta:
        verbose_name = "Det. Viscosidad"
        verbose_name_plural = "Det. Viscosidades"

    def __str__(self):
        return f"{self.viscosidad}"

class DeterminacionDelValorCaloricoSuperior_Calorimetro (models.Model):
    temperatura_introducida = models.FloatField(verbose_name="Temp. Introducida:")
    valor_calorico_superior_resultante = models.FloatField(verbose_name="Valor Calórico Result:")
    porciento_de_asufre_resultante = models.FloatField(verbose_name="% de Asufre Result:")
    porciento_de_hidrogeno_resultante = models.FloatField(verbose_name="% de Hidrógeno Result:")
    porciento_de_carbono_resultante = models.FloatField(verbose_name="% de Carbono Result:")

    class Meta:
        verbose_name = "Det. Valor Calórico Sup Calorím"
        verbose_name_plural = "Det. Valores Calóricos Sup Calorím"

    def __str__(self):
        return f"{self.temperatura_introducida}{self.valor_calorico_superior_resultante}"


class DeterminacionDelValorCaloricoSuperior_Algoritmo(models.Model):

    valor_calorico_superior_resultante = models.FloatField(verbose_name="Valor Calórico Result:")
    gravedad_especifica_del_combustible = models.FloatField(verbose_name="Gravedad Específica:")
    porcentaje_de_agua = models.FloatField(verbose_name="Porcentaje de Agua:")

    class Meta:
        verbose_name = "Det. Valor Calórico Sup. Algor"
        verbose_name_plural = "Det. Valores Calóricos Sup Algor"

    def __str__(self):
        return f"{self.valor_calorico_superior_resultante}"

class DeterminacionDelValorCaloricoSuperior(models.Model):

    esta_roto = models.BooleanField (verbose_name="Está Roto el Calorímetro", default=False)

    determinacion_del_valor_calorico_superior_Calorimetro = models.ForeignKey(
        DeterminacionDelValorCaloricoSuperior_Calorimetro,
        on_delete=models.SET_NULL,
        verbose_name="Valor Calórico Sup. en el Calorímetro",
        blank=True,
        null=True
    )
    determinacion_del_valor_calorico_superior_Algoritmo = models.ForeignKey(
        DeterminacionDelValorCaloricoSuperior_Algoritmo,
        on_delete=models.SET_NULL,
        verbose_name="Valor Calórico Sup. Medeiante el Algorítmo",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Det. Valor Calórico Sup"
        verbose_name_plural = "Det. Valores Calóricos Sup"

    def __str__(self):
        return f"{self.esta_roto}"


class RegistroDeOperacion (models.Model):
    identificador_del_registro_de_operacion= models.CharField( max_length=255, verbose_name="Identidicador:")
    fecha_de_registro_de_operacion = models.DateField(verbose_name="Fecha del registro:")
    descripicion_del_registro_de_operacion = models.CharField(max_length=255, verbose_name="Descripción del registro:")
    trabajador = models.ManyToManyField(Trabajador, verbose_name="Trabajador")

    preparar_soluciones = models.ForeignKey(
        PrepararSoluciones,
        on_delete=models.SET_NULL,
        verbose_name="Preparar Soluciones",
        blank=True,
        null=True
    )

    determinacion_de_la_gravedad_especifica = models.ForeignKey(
        DeterminacionDeLaGravedadEspecifica,
        on_delete=models.SET_NULL,
        verbose_name="Det. Gravedad Especifica:",
        blank=True,
        null=True
    )

    determinacion_de_la_temperatura_de_calentamiento = models.ForeignKey(
        DeterminacionDeLaTemperaturaDeCalentamiento,
        on_delete=models.SET_NULL,
        verbose_name="Det. Temp de Calentamiento:",
        blank=True,
        null=True
    )

    determinacion_de_la_viscosidad = models.ForeignKey(
        DeterminacionDeLaViscosidad,
        on_delete=models.SET_NULL,
        verbose_name="Det. Viscosidad:",
        blank=True,
        null=True
    )

    determinacion_del_valor_calorico_superior = models.ForeignKey(
        DeterminacionDelValorCaloricoSuperior,
        on_delete=models.SET_NULL,
        verbose_name="Det. Valor Calórico Sup:",
        blank=True,
        null=True
    )

    muestra = models.ForeignKey(
        Muestra,
        on_delete=models.SET_NULL,
        verbose_name="Muestra",
        blank=True,
        null=True
    )

    libroDeRegistroDeOperacione = models.ForeignKey(
        LibroDeRegistroDeOperacione,
        on_delete=models.CASCADE,
        verbose_name="Libro de Registro de Operacione",
    )

    class Meta:
        verbose_name = "Registro de operación"
        verbose_name_plural = "Registro de operaciones"

    def __str__(self):
            return f"{self.identificador_del_registro_de_operacion}"