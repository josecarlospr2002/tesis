from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import EntradaDeReactivo, Reactivo

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

# @receiver(post_save, sender=EntradaDeReactivo)
# def actualizar_cantidad_reactivo_al_guardar(sender, instance, created, **kwargs):
#     """Actualiza la cantidad disponible cuando se crea o edita una entrada"""
#     reactivo = instance.reactivo
#     if created:  # Si es una nueva entrada
#         # Sumamos la nueva cantidad al disponible
#         reactivo.cantidad_de_disponible += instance.cantidad_de_reactivo
#         reactivo.save()
#     # No necesitamos else aquí porque las ediciones se manejan en pre_save

@receiver(post_delete, sender=EntradaDeReactivo)
def actualizar_cantidad_reactivo_al_borrar(sender, instance, **kwargs):
    """Actualiza la cantidad disponible cuando se elimina una entrada"""
    reactivo = instance.reactivo
    # Restamos la cantidad que se eliminó
    reactivo.cantidad_de_disponible -= instance.cantidad_de_reactivo
    reactivo.save()
