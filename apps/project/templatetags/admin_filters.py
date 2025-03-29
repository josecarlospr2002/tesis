from django import template

register = template.Library()

@register.filter(name='in_category')
def in_category(model, category):
    categories = {
        'ensayos': ['EnsayoAguaVapor', 'EnsayoDelCombustible', 'Informe'],
        'reactivos': ['Reactivo', 'EntradaDeReactivo', 'Reactivo_Consumido'],
        'soluciones': ['PrepararSoluciones', 'Soluciones_Preparadas_Producidas', 'SolucionesPreparadas'],
        'otros': ['EquipamientoDelLaboratorio', 'Trabajador']
    }
    return model.object_name in categories.get(category, [])

@register.filter(name='get_item')
def get_item(dictionary, key):
    """Get an item from a dictionary using a key."""
    return dictionary.get(key, '')
