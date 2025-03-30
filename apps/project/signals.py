from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import EntradaDeReactivo, Reactivo, Reactivo_Consumido, Soluciones_Preparadas_Producidas, SolucionesPreparadas

@receiver(pre_save, sender=EntradaDeReactivo)
def manejar_edicion_entrada_reactivo(sender, instance, **kwargs):
    """Maneja el caso de edición de una entrada existente"""
    if instance.pk:  # Si es una edición (no una creación nueva)
        entrada_anterior = EntradaDeReactivo.objects.get(pk=instance.pk)
        # Si la nueva cantidad es menor que la anterior, actualizamos el disponible
        if instance.cantidad_de_reactivo < entrada_anterior.cantidad_de_reactivo:
            diferencia = entrada_anterior.cantidad_de_reactivo - instance.cantidad_de_reactivo
            instance.reactivo.cantidad_de_disponible -= diferencia
            instance.reactivo.save()
        else:
            # Si la nueva cantidad es mayor o igual, no hace nada
            if instance.cantidad_de_reactivo > entrada_anterior.cantidad_de_reactivo:
                diferencia = instance.cantidad_de_reactivo - entrada_anterior.cantidad_de_reactivo
                instance.reactivo.cantidad_de_disponible += diferencia
                instance.reactivo.save()
            
    else:
        # Sumamos la nueva cantidad al disponible
        instance.reactivo.cantidad_de_disponible += instance.cantidad_de_reactivo
        instance.reactivo.save()

@receiver(post_delete, sender=EntradaDeReactivo)
def actualizar_cantidad_reactivo_al_borrar(sender, instance, **kwargs):
    """Actualiza la cantidad disponible cuando se elimina una entrada"""
    reactivo = instance.reactivo
    # Restamos la cantidad que se eliminó
    reactivo.cantidad_de_disponible -= instance.cantidad_de_reactivo
    reactivo.save()

@receiver(pre_save, sender=Reactivo_Consumido)
def manejar_edicion_reactivo_consumido(sender, instance, **kwargs):
    """Maneja el caso de edición de un consumo existente"""
    if instance.pk:  # Si es una edición (no una creación nueva)
        consumo_anterior = Reactivo_Consumido.objects.get(pk=instance.pk)
        # Si la nueva cantidad es mayor que la anterior, restamos más del disponible
        if instance.cantidad_de_reactivo_consumida > consumo_anterior.cantidad_de_reactivo_consumida:
            diferencia = instance.cantidad_de_reactivo_consumida - consumo_anterior.cantidad_de_reactivo_consumida
            instance.reactivo.cantidad_de_disponible -= diferencia
            instance.reactivo.save()
        else:
            # Si la nueva cantidad es menor, devolvemos la diferencia al disponible
            if instance.cantidad_de_reactivo_consumida < consumo_anterior.cantidad_de_reactivo_consumida:
                diferencia = consumo_anterior.cantidad_de_reactivo_consumida - instance.cantidad_de_reactivo_consumida
                instance.reactivo.cantidad_de_disponible += diferencia
                instance.reactivo.save()
    else:
        # Es una nueva entrada, restamos del disponible
        instance.reactivo.cantidad_de_disponible -= instance.cantidad_de_reactivo_consumida
        instance.reactivo.save()

@receiver(post_delete, sender=Reactivo_Consumido)
def actualizar_reactivo_consumido_al_borrar(sender, instance, **kwargs):
    """Actualiza la cantidad disponible cuando se elimina un consumo"""
    reactivo = instance.reactivo
    # Al eliminar un consumo, devolvemos la cantidad al disponible
    reactivo.cantidad_de_disponible += instance.cantidad_de_reactivo_consumida
    reactivo.save()

@receiver(pre_save, sender=Soluciones_Preparadas_Producidas)
def manejar_edicion_solucion_producida(sender, instance, **kwargs):
    """Maneja el caso de edición de una solución producida"""
    if instance.pk:  # Si es una edición (no una creación nueva)
        produccion_anterior = Soluciones_Preparadas_Producidas.objects.get(pk=instance.pk)
        # Si la nueva cantidad es mayor que la anterior, sumamos la diferencia
        if instance.cantidad_de_soluciones_preparada_producidas > produccion_anterior.cantidad_de_soluciones_preparada_producidas:
            diferencia = instance.cantidad_de_soluciones_preparada_producidas - produccion_anterior.cantidad_de_soluciones_preparada_producidas
            instance.soluciones_preparadas.cantidad_de_la_solucion_preparada += diferencia
            instance.soluciones_preparadas.save()
        else:
            # Si la nueva cantidad es menor, restamos la diferencia
            if instance.cantidad_de_soluciones_preparada_producidas < produccion_anterior.cantidad_de_soluciones_preparada_producidas:
                diferencia = produccion_anterior.cantidad_de_soluciones_preparada_producidas - instance.cantidad_de_soluciones_preparada_producidas
                instance.soluciones_preparadas.cantidad_de_la_solucion_preparada -= diferencia
                instance.soluciones_preparadas.save()
    else:
        # Es una nueva entrada, sumamos al disponible
        instance.soluciones_preparadas.cantidad_de_la_solucion_preparada += instance.cantidad_de_soluciones_preparada_producidas
        instance.soluciones_preparadas.save()

@receiver(post_delete, sender=Soluciones_Preparadas_Producidas)
def actualizar_solucion_preparada_al_borrar(sender, instance, **kwargs):
    """Actualiza la cantidad cuando se elimina una producción"""
    solucion = instance.soluciones_preparadas
    # Al eliminar una producción, restamos la cantidad
    solucion.cantidad_de_la_solucion_preparada -= instance.cantidad_de_soluciones_preparada_producidas
    solucion.save()