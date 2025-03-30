from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import EntradaDeReactivo, Reactivo, Reactivo_Consumido 

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