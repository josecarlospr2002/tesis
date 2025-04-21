from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from apps.project.models import (
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

fake = Faker('es_ES')

class Command(BaseCommand):
    help = 'Genera datos de prueba para el proyecto'

    def handle(self, *args, **kwargs):
        self.stdout.write('Generando datos de prueba...')
        
        # Generar equipamiento
        equipos = []
        for _ in range(10):
            equipo = EquipamientoDelLaboratorio.objects.create(
                identificador_del_equipo=fake.unique.bothify(text='EQ-####'),
                nombre_del_equipo=fake.random_element(elements=('Balanza', 'pH-metro', 'Espectrofotómetro', 'Horno', 'Centrífuga')),
                fabricante_del_equipo=fake.company(),
                fecha_de_entrada_del_equipo_al_laboratorio=fake.date_between(start_date='-5y', end_date='today'),
                estado_del_equipo=fake.random_element(elements=('Roto', 'En uso')),
                cantidad_actual=fake.random_int(min=1, max=5),
                calibracion_del_equipo=fake.random_number(digits=2, fix_len=True),
                descripicion_del_equipo=fake.text(max_nb_chars=200)
            )
            equipos.append(equipo)

        # Generar reactivos
        reactivos = []
        for _ in range(15):
            reactivo = Reactivo.objects.create(
                nombre_del_reactivo=fake.random_element(elements=('Ácido clorhídrico', 'Hidróxido de sodio', 'Sulfato de cobre', 'Nitrato de plata', 'Fenolftaleína')),
                cantidad_de_disponible=fake.random_number(digits=2, fix_len=True),
                fecha_entrada=fake.date_between(start_date='-1y', end_date='today'),
                descripicion_del_reactivo=fake.text(max_nb_chars=200)
            )
            reactivos.append(reactivo)

        # Generar entradas de reactivos
        for reactivo in reactivos:
            for _ in range(3):
                EntradaDeReactivo.objects.create(
                    fecha_de_entrada_del_reactivo=fake.date_between(start_date='-1y', end_date='today'),
                    cantidad_de_reactivo=fake.random_number(digits=2, fix_len=True),
                    reactivo=reactivo
                )

        # Generar soluciones preparadas
        soluciones = []
        for _ in range(8):
            solucion = SolucionesPreparadas.objects.create(
                identificador_de_la_solucion_preparada=fake.unique.bothify(text='SOL-####'),
                nombre_de_la_solucion_preparada=fake.random_element(elements=('Solución tampón pH 7', 'Solución de NaCl 0.9%', 'Solución de NaOH 1M')),
                cantidad_de_la_solucion_preparada=fake.random_number(digits=2, fix_len=True)
            )
            soluciones.append(solucion)

        # Generar trabajadores
        trabajadores = []
        for _ in range(5):
            trabajador = Trabajador.objects.create(
                nombre_apellido=fake.name(),
                ci=fake.unique.numerify(text='###########'),
                rol_del_trabajador=fake.random_element(elements=('Técnico de laboratorio', 'Químico', 'Investigador', 'Asistente'))
            )
            trabajadores.append(trabajador)

        # Generar reactivos consumidos
        reactivos_consumidos = []
        for reactivo in reactivos:
            for _ in range(2):
                rc = Reactivo_Consumido.objects.create(
                    reactivo=reactivo,
                    cantidad_de_reactivo_consumida=fake.random_number(digits=1, fix_len=True)
                )
                reactivos_consumidos.append(rc)

        # Generar soluciones preparadas producidas
        soluciones_producidas = []
        for solucion in soluciones:
            for _ in range(3):
                sp = Soluciones_Preparadas_Producidas.objects.create(
                    soluciones_preparadas=solucion,
                    cantidad_de_soluciones_preparada_producidas=fake.random_number(digits=2, fix_len=True)
                )
                soluciones_producidas.append(sp)

        # Generar preparaciones de soluciones
        preparaciones = []
        for _ in range(10):
            preparacion = PrepararSoluciones.objects.create(
                fecha_de_preparacion_de_la_solucion=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
            )
            # Asignar reactivos consumidos y soluciones producidas
            preparacion.reactivo_consumido.set(fake.random_elements(elements=reactivos_consumidos, length=3, unique=True))
            preparacion.soluciones_preparadas_producidas.set(fake.random_elements(elements=soluciones_producidas, length=2, unique=True))
            preparaciones.append(preparacion)

        # Generar ensayos de agua-vapor
        for _ in range(5):
            ensayo = EnsayoAguaVapor.objects.create(
                nombre_ensayo=fake.random_element(elements=('Análisis de pH', 'Determinación de cloruros', 'Análisis de dureza')),
                fecha_del_ensayo=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()),
                descripicion_del_ensayo=fake.text(max_nb_chars=500)
            )
            ensayo.trabajador.set(fake.random_elements(elements=trabajadores, length=2, unique=True))
            ensayo.preparar_soluciones.set(fake.random_elements(elements=preparaciones, length=3, unique=True))

        # Generar ensayos de combustible
        for _ in range(5):
            ensayo = EnsayoDelCombustible.objects.create(
                nombre_ensayo=fake.random_element(elements=('Análisis de viscosidad', 'Determinación de punto de inflamación', 'Análisis de azufre')),
                fecha_del_ensayo=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()),
                result_determinacion_de_la_viscosidad=fake.random_number(digits=2, fix_len=True),
                result_determinacion_de_la_temperatura_de_calentamiento=fake.random_number(digits=2, fix_len=True),
                result_determinacion_del_valor_calorico=fake.random_number(digits=4, fix_len=True),
                result_determinacion_de_la_gravedad_especifica=fake.random_number(digits=2, fix_len=True),
                descripicion_del_resultado=fake.text(max_nb_chars=500)
            )
            ensayo.trabajador.set(fake.random_elements(elements=trabajadores, length=2, unique=True))
            ensayo.preparar_soluciones.set(fake.random_elements(elements=preparaciones, length=3, unique=True))

        # Generar informes
        for _ in range(10):
            informe = Informe.objects.create(
                titulo_del_informe=fake.sentence(nb_words=6),
                fecha_del_informe=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()),
                descripicion_del_informe=fake.text(max_nb_chars=1000)
            )
            informe.trabajador.set(fake.random_elements(elements=trabajadores, length=2, unique=True))
            informe.preparar_soluciones.set(fake.random_elements(elements=preparaciones, length=3, unique=True))
            
            # Asignar ensayo de agua-vapor o combustible aleatoriamente
            if fake.boolean():
                informe.ensayo_aguavapor = EnsayoAguaVapor.objects.order_by('?').first()
            else:
                informe.ensayo_del_combustible = EnsayoDelCombustible.objects.order_by('?').first()
            informe.save()

        self.stdout.write(self.style.SUCCESS('Datos de prueba generados exitosamente!')) 