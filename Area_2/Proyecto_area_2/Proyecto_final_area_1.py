
from IPython.display import display # Importamos el siguiente componente del módulo display para poder representar correctamente el mapa dentro del menú creado.
import folium                       # Importamos la librería folium para representar un mapa de las comisarías y los delitos cometidos.
from datetime import datetime       # Importamos el módulo datetime de la librería datetime.
from pyproj import Transformer      # Importamos la clase Transformer de la librería pyproj.
import numpy as np                  # Importamos la librería numpy.
import math                         # Importamos la librería math.
import webbrowser
import os
from dotenv import load_dotenv
import pymongo
import mysql.connector
import mysql_insertar_datos
import mysql_consultas_datos
import mongodb_delincuencia


# Vvariables para el menú que controla los procesos.
proceso_delitos = 1
proceso_criminal = 2
proceso_comisarias = 3
proceso_hospitales = 4
proceso_areas_comunitarias = 5
proceso_mapa = 6
proceso_coordenadas = 7
proceso_agregar_areas_con_delitos = 8
proceso_indice_criminalidad = 9
proceso_ordenar_delitos = 10
proceso_tiempo_entre_delitos = 11
proceso_comisaria_entre_delitos = 12
proceso_cerrar_app = 13

delitos = []                                # Lista de los delitos cometidos.
comisarias = []                             # Lista de las comisarias.
delitos_areas = []                          # Lista de los delitos según áreas.

sistema_referencia_origen = "EPSG:4326"     # Sistema geográfico.
sistema_referencia_destino = "EPSG:26916"   # Sistema proyectado.
transformer = Transformer.from_crs(sistema_referencia_origen, sistema_referencia_destino)   # Definimos la variable transformer para crear el objeto transformador.


# ------------------------------------- MENÚ Y CONTROLADOR DE PROCESOS DEL PROGRAMA -----------------------------
def controlador(par_proceso):
    proceso = par_proceso
    
    if proceso == proceso_delitos:
        opcion_orden = int(input("¿Eliga una opción?\n\
- 1) Buscar delitos.\n\
- 2) Mostrar todos los delitos.\n\
- 3) Agregar delito.\n\
- 4) Editar delito.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            mysql_consultas_datos.buscar_delitos_por_valor()
        elif opcion_orden == 2:
            mysql_consultas_datos.mostrar_todos_los_delitos()
        elif opcion_orden == 3:
            mysql_insertar_datos.agregar_delito()
        elif opcion_orden == 4:
            mysql_consultas_datos.editar_delito()
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")

    elif proceso == proceso_criminal:
        opcion_orden = int(input("¿Eliga una opción?\n\
- 1) Buscar criminales entre fehcas de nacimiento.\n\
- 2) Buscar Por delito.\n\
- 3) Buscar por estatura y peso.\n\
- 4) Mostrar lista con todos los criminales.\n\
- 5) Agregar un criminal.\n\
- 6) Editar un criminal.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            mongodb_delincuencia.buscar_por_fecha()
        elif opcion_orden == 2:
            mongodb_delincuencia.buscar_por_delito()
        elif opcion_orden == 3:
            mongodb_delincuencia.buscar_por_estatura_peso()
        elif opcion_orden == 4:
            mongodb_delincuencia.mostrar_todos_los_criminales()
        elif opcion_orden == 5:
            mongodb_delincuencia.buscar_por_estatura_peso()#falta
        elif opcion_orden == 6:
            mongodb_delincuencia.buscar_por_estatura_peso()#falta
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")

    elif proceso == proceso_comisarias:
        opcion_orden = int(input("\n¿Eliga una opción?\n\
- 1) Mostrar todas las comisarias.\n\
- 2) Agregar una comisaria.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            mysql_consultas_datos.mostrar_todas_las_comisarias()            
        elif opcion_orden == 2:
            mysql_insertar_datos.agregar_comisaria()            
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")     

    elif proceso == proceso_hospitales:
        opcion_orden = int(input("\n¿Eliga una opción?\n\
- 1) Mostrar todos los Hospitales.\n\
- 2) Agregar un Hospital.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            mysql_consultas_datos.mostrar_todos_los_hospitales()            
        elif opcion_orden == 2:
            mysql_insertar_datos.agregar_hospital()       
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")

    elif proceso == proceso_areas_comunitarias:
        opcion_orden = int(input("\n¿Eliga una opción?\n\
- 1) Mostrar todas las Áreas Comunitarias Hospitales.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            mysql_consultas_datos.mostrar_areas_comunitarias()    
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")    

    elif proceso == proceso_mapa:
        ver_mapa()
    elif proceso == proceso_agregar_areas_con_delitos:
        nuevo_delitos_area = agregar_delitos_area()
    elif proceso == proceso_indice_criminalidad:
        mostrar_indice_criminalidad()
    elif proceso == proceso_ordenar_delitos:
        opcion_orden = int(input("¿Cómo quieres ordenar los delitos?\n\
- 1) De más antiguo a más reciente.\n\
- 2) De más reciente a más antiguo.\n\
Introduce el número que corresponda con la opción escogida: "))
        if opcion_orden == 1:
            ordenar_delitos_ascendente(delitos)
        elif opcion_orden == 2:
            ordenar_delitos_descendente(delitos)
        else:
            opcion_orden = input("Elige una opción válida. Introduce el número que corresponda con la opción escogida: ")
    elif proceso == proceso_tiempo_entre_delitos:
        calcular_tiempo_entre_delitos(delitos)
    elif proceso == proceso_comisaria_entre_delitos:
        encontrar_comisaria_mas_cercana()
    else:
        cerrar_sesion()

# Función para el menú.
def main():
    # Mediante la siguiente función precargamos el histórico de delitos, de comisarías y de áreas delictivas.
    cargar_historico_delitos()
    cargar_historico_comisarias()
    cargar_historico_delitos_areas()

    continuar = True
    while continuar:
        proceso = int(input("\n¡Hola Agente! ¿Con que información desea trabajar?\n\
\n1) Delitos.\n\
2) Criminales.\n\
3) Comisarias.\n\
4) Hospitales.\n\
5) Áreas comunitarias.\n\
6) Ver mapa de delitos y comisarias.\n\
8) Agregar datos sobre delitos en áreas comunitarias.\n\
9) Ver el índice de criminalidad por áreas.\n\
10) Mostrar y ordenar los delitos existentes.\n\
11) Calcular el tiempo entre delitos.\n\
12) Comprobar cuál es la comisaría más cercana a cada delito.\n\
13) Cerrar sesión.\n\
\nIntroduce el número que corresponda con la opción escogida: "))
        controlador(proceso)

        if proceso == 13:
            continuar = False
        else:
            respuesta = input("¿Desea hacer algo más? (SI/NO): ").strip().lower()
            if respuesta != 'si':
                continuar = False

    print("\n¡Hasta pronto! ¡Qué tenga un buen día!")

# Función para cerrar la sesión del programa.
def cerrar_sesion():
    print("Ha cerrado la sesión correctamente.")

# ------------------------------------------ EJERCICIO 1 DEL RETO -------------------------------------------
# Función para agregar delito.
def agregar_delito(par_num_caso = None, par_descripcion = None, par_arrestado = None, par_num_area_comunitaria = None,
                   par_cuadra = None, par_fecha = None, par_latitud_delito = None, par_longitud_delito = None):
    if par_num_caso is None:
        num_caso = input("Núm. caso: ")
    else:
        num_caso = par_num_caso

    if par_descripcion is None:
        descripcion = input("Descripción: ")
    else:
        descripcion = par_descripcion

    if par_arrestado is None:
        arrestado = input("Arrestado (True/False): ").strip().lower() == 'true'
    else:
        arrestado = par_arrestado

    if par_num_area_comunitaria is None:
        num_area_comunitaria = int(input("Núm. área comunitaria: "))
    else:
        num_area_comunitaria = par_num_area_comunitaria

    if par_cuadra is None:
        cuadra = input("Cuadra: ")
    else:
        cuadra = par_cuadra

    if par_fecha is None:
        fecha = input("Fecha (YYYY-MM-DD HH:MM:SS): ")
    else:
        fecha = par_fecha

    if par_latitud_delito is None:
        latitud_delito = float(input("Latitud: "))
    else:
        latitud_delito = par_latitud_delito

    if par_longitud_delito is None:
        longitud_delito = float(input("Longitud: "))
    else:
        longitud_delito = par_longitud_delito

    # Declaramos la variable nuevo_delito como un diccionario que pueda almacenar los nuevos datos introducidos por el usuario.
    nuevo_delito = {
        "Núm. caso": num_caso,
        "Descripción": descripcion,
        "Arrestado": arrestado,
        "Núm. área comunitaria": num_area_comunitaria,
        "Cuadra": cuadra,
        "Fecha": fecha,
        "Coordenadas": {
            "Latitud": latitud_delito,
            "Longitud": longitud_delito
        }
    }

    # Agregamos los datos del nuevo delito a la lista de delitos existente mediante el método append().
    delitos.append(nuevo_delito)
    return nuevo_delito

# Función para cargar el histórico de los delitos registrados.
def cargar_historico_delitos():
    agregar_delito("HY411648", "Maltrato doméstico", False, 61, "043XX S WOOD ST", "2015-09-05 13:30:00", 41.937406, -87.670000)
    agregar_delito("HY411595", "Tráfico de drogas", True, 21, "035XX W BARRY AVE", "2015-09-05 12:45:00", 41.815117, -87.716650)
    agregar_delito("HY411435", "Robo en casa", False, 71, "082XX S LOOMIS BLVD", "2015-09-05 10:55:00", 41.744379, -87.658431)

# Función para consultar los datos de un delito.
def consultar_delito():
    if not delitos:
        print("No hay delitos registrados.")
    else:
        num_caso = input("Por favor, introduce Núm. caso del delito que desees consultar: ")
        for delito in delitos:
            if delito["Núm. caso"] == num_caso:
                print("Aquí tienes el delito solicitado: ")
                imprimir_delito(delito)
                return

# Función para imprimir un delito.
def imprimir_delito(delito):
    print(f"Núm. caso: {delito['Núm. caso']}")
    print(f"Descripción: {delito['Descripción']}")
    print(f"Arrestado: {'Sí' if delito['Arrestado'] else 'No'}")
    print(f"Núm. área comunitaria: {delito['Núm. área comunitaria']}")
    print(f"Cuadra: {delito['Cuadra']}")
    print(f"Fecha: {delito['Fecha']}")
    print(f"Latitud: {delito['Coordenadas']['Latitud']}")
    print(f"Longitud: {delito['Coordenadas']['Longitud']}\n")

# Función para actualizar los datos de un delito.
def modificar_delito():
    num_caso = input("Introduce el Núm. caso del delito que quieres modificar: ")
    for delito in delitos:
        if delito["Núm. caso"] == num_caso:
            dato_modificar = int(input("¿Qué dato te gustaría modificar?: \n\
1) Descripción.\n\
2) Arrestado.\n\
3) Núm. area comunitaria.\n\
4) Cuadra.\n\
5) Fecha.\n\
6) Latitud.\n\
7) Longitud.\n\
Introduce el número que corresponda con la opción escogida: "))

            if dato_modificar == 1:
                delito["Descripción"] = input("Introduce la nueva descripción del caso: ")
            elif dato_modificar == 2:
                delito["Arrestado"] = input("Introduce el nuevo estado de Arrestado (True/False): ").lower() == 'true'
            elif dato_modificar == 3:
                delito["Núm. área comunitaria"] = int(input("Introduce el nuevo Núm. área comunitaria: "))
            elif dato_modificar == 4:
                delito["Cuadra"] = input("Introduce la nueva Cuadra: ")
            elif dato_modificar == 5:
                delito["Fecha"] = input("Introduce la nueva Fecha (YYYY-MM-DD HH:MM:SS): ")
            elif dato_modificar == 6:
                delito["Coordenadas"]["Latitud"] = float(input("Introduce la nueva Latitud: "))
            elif dato_modificar == 7:
                delito["Coordenadas"]["Longitud"] = float(input("Introduce la nueva Longitud: "))
            else:
                dato_modificar = ("¡Ups! Ha habido un error. Introduzca una opción: ")
            print("¡Los datos se han modificado con éxito!")
            imprimir_delito(delito)
            break
        else:
            num_caso = input("¡Ups! Algún dato es erróneo. Por favor, inténtelo de nuevo: ")

# ---------------------------------------- EJERCICIO 2 DEL RETO -------------------------------------------
# Función para agregar comisarías.
def agregar_comisaria(par_nombre_comisaria = None, par_latitud_comisaria = None, par_longitud_comisaria = None):
    if par_nombre_comisaria is None:
        nombre_comisaria = input("Nombre del Distrito: ")
    else:
        nombre_comisaria = par_nombre_comisaria

    if par_latitud_comisaria is None:
        latitud_comisaria = float(input("Latitud: "))
    else:
        latitud_comisaria = par_latitud_comisaria

    if par_longitud_comisaria is None:
        longitud_comisaria = float(input("Longitud: "))
    else:
        longitud_comisaria = par_longitud_comisaria

    # Declaramos la variable nueva_comisaria como un diccionario que pueda almacenar los nuevos datos introducidos por el usuario.
    nueva_comisaria = {
        "Nombre del Distrito": nombre_comisaria,
        "Coordenadas": {
            "Latitud": latitud_comisaria,
            "Longitud": longitud_comisaria
        }
    }

    # Agregamos los datos de la nueva comisaria a la lista de comisarias existente mediante el método append().
    comisarias.append(nueva_comisaria)
    return nueva_comisaria

# Función para cargar datos del histórico de las comisarías.
def cargar_historico_comisarias():
    agregar_comisaria("Near North", 41.903242, -87.643352)
    agregar_comisaria("Town Hall", 41.947400, -87.651512)
    agregar_comisaria("Lincoln", 41.979550, -87.692845)
    agregar_comisaria("Morgan Park", 41.691435, -87.668520)
    agregar_comisaria("Rogers Park", 41.999763, -87.671324)

# Función para establecer las coordenadas para el mapa.
def ver_mapa():
    # Creamos un mapa centrado en una ubicación por defecto
    mapa = folium.Map()

    # Obtenemos las ubicaciones de las comisarías desde la base de datos.
    ubicaciones_comisarias = mysql_consultas_datos.coordenadas_comisarias()

    # Obtenemos las ubicaciones de los delitos desde la base de datos.
    ubicaciones_delitos = mysql_consultas_datos.coordenadas_delitos()

    # Llamamos a la función para agregar marcadores de comisarías al mapa.
    marcador_comisarias(mapa, ubicaciones_comisarias)

    # Llamamos a la función para agregar marcadores de delitos al mapa.
    marcador_delitos(mapa, ubicaciones_delitos)

    # Creamos un mapa centrado en todas las ubicaciones.
    todas_ubicaciones = ubicaciones_comisarias + ubicaciones_delitos
    if todas_ubicaciones:
        mapa.fit_bounds([ubicacion[:2] for ubicacion in todas_ubicaciones])

    # Guardamos el mapa como un archivo HTML
    mapa_html = "mapa_delitos_comisarias.html"
    mapa.save(mapa_html)

    # Abrir automáticamente el archivo en el navegador web predeterminado
    print("Aquí tienes el mapa con las comisarías y delitos existentes: ")
    webbrowser.open(os.path.abspath(mapa_html))

    print("Mira la página que se abrió en tu navegador")

def marcador_comisarias(mapa, ubicaciones):
    for ubicacion in ubicaciones:
        lat, lon, nombre = ubicacion
        folium.Marker(
            location=[lat, lon],
            popup=nombre,
            icon=folium.Icon(color='blue')
        ).add_to(mapa)

def marcador_delitos(mapa, ubicaciones):
    for ubicacion in ubicaciones:
        lat, lon, texto = ubicacion
        folium.Marker(
            location=[lat, lon],
            popup=texto,
            icon=folium.Icon(color='red')
        ).add_to(mapa)

# Función para cargar las coordenadas ya existentes.
def consultar_mapa_registrado():
    establecer_coordenadas_mapa()


# ---------------------------------------- EJERCICIO 3 DEL RETO -------------------------------------------
# Función para agregar delitos por áreas.
def agregar_delitos_area(par_area = None, par_numero_delitos = None, par_poblacion = None):
    if par_area is None:
        area = input("Introduce el área correspondiente: ")
    else:
        area = par_area

    if par_numero_delitos is None:
        numero_delitos = int(input("Introduce el número de delitos: "))
    else:
        numero_delitos = par_numero_delitos

    if par_poblacion is None:
        poblacion = int(input("Introduce el número de población: "))
    else:
        poblacion = par_poblacion

    # Declaramos la variable nuevo_delitos_áreas como un diccionario que pueda almacenar los nuevos datos introducidos por el usuario.
    nuevo_delitos_area = {
        "Área correspondiente": area,
        "Número de delitos": numero_delitos,
        "Población": poblacion
    }

    # Agregamos los datos de la nueva comisaria a la lista de comisarias existente mediante el método append().
    delitos_areas.append(nuevo_delitos_area)
    return nuevo_delitos_area

# Función para cargar el histórico de delitos por áreas.
def cargar_historico_delitos_areas():
    agregar_delitos_area("Área 1", 289, 54991)
    agregar_delitos_area("Área 2", 228, 71942)
    agregar_delitos_area("Área 3", 319, 56362)
    agregar_delitos_area("Área 4", 141, 39493)
    agregar_delitos_area("Área 5", 5, 0)

# Función para calcular el índice de criminalidad.
def calcular_indice_criminalidad(delitos_areas):
    indices_criminalidad = []
    for i in delitos_areas:
        numero_delitos = i["Número de delitos"]
        poblacion = i["Población"]
        if poblacion == 0:
            continue
        calculo_indice = (numero_delitos / poblacion) * 100000
        indices_criminalidad.append(round(calculo_indice, 2))
        print(f"El índice de criminalidad del {i['Área correspondiente']} es de {round(calculo_indice, 2)} delitos.")
    return indices_criminalidad

# Función para mostrar el índice de criminalidad calculado.
def mostrar_indice_criminalidad():
    print("A continuación, se muestra el Índice de Criminalidad por cada 100.000 habitantes: ")
    indices_criminalidad = calcular_indice_criminalidad(delitos_areas)

    # Calcular el valor máximo, el valor mínimo y la media de los resultados.
    maximo_criminalidad = max(indices_criminalidad)
    minimo_criminalidad = min(indices_criminalidad)
    media_criminalidad = sum(indices_criminalidad) / len(indices_criminalidad)

    # Mostrar los resultados obtenidos.
    print(f"El mayor resultado del Índice de Criminalidad es de {maximo_criminalidad} delitos.")
    print(f"El menor resultado del Índice de Criminalidad es de {minimo_criminalidad} delitos.")
    print(f"La media del Índice de Criminalidad es de {round(media_criminalidad, 2)} delitos.")

# (Función para ordenar los delitos por fecha ascendente.
def ordenar_delitos_ascendente(delitos):
    for delito in delitos:
        if type(delito["Fecha"]) is str:
            delito["Fecha"] = datetime.strptime(delito["Fecha"], "%Y-%m-%d %H:%M:%S")

    orden_por_fecha = sorted(delitos, key = lambda x: x["Fecha"])

    for orden in orden_por_fecha:
        imprimir_delito(orden)

# Función para ordenar los delitos por fecha descendente.
def ordenar_delitos_descendente(delitos):
    for delito in delitos:
        if type(delito["Fecha"]) is str:
            delito["Fecha"] = datetime.strptime(delito["Fecha"], "%Y-%m-%d %H:%M:%S")

    orden_por_fecha = sorted(delitos, key = lambda x: x["Fecha"], reverse = True)

    for orden in orden_por_fecha:
        imprimir_delito(orden)

# Función para calcular el tiempo entre delitos.
def calcular_tiempo_entre_delitos(delitos):
    # Ordenar los delitos por fecha de forma ascendente.
    delitos_ordenados = sorted(delitos, key=lambda x: x["Fecha"])

    # Guardar la primera fecha para determinar si es str o datetime.
    primera_fecha = delitos_ordenados[0]["Fecha"]

    # Calcular la diferencia de tiempo entre delitos consecutivos.
    print("Tiempo entre delitos consecutivos: \n")
    for i in range(1, len(delitos_ordenados)):
        if type(primera_fecha) is str:
            # Si las fechas son cadenas, convertirlas a objetos datetime.
            fecha_actual = datetime.strptime(delitos_ordenados[i]["Fecha"], "%Y-%m-%d %H:%M:%S")
            fecha_anterior = datetime.strptime(delitos_ordenados[i - 1]["Fecha"], "%Y-%m-%d %H:%M:%S")
        else:
            # Si las fechas ya son objetos datetime, usarlas directamente.
            fecha_actual = delitos_ordenados[i]["Fecha"]
            fecha_anterior = delitos_ordenados[i - 1]["Fecha"]

        # Calcular la diferencia de tiempo entre las fechas.
        diferencia = fecha_actual - fecha_anterior
        tiempo_en_minutos = diferencia.total_seconds() / 60
        num_caso_actual = delitos_ordenados[i]["Núm. caso"]
        num_caso_anterior = delitos_ordenados[i - 1]["Núm. caso"]
        print(f"El tiempo entre el caso número {num_caso_anterior} y el caso número {num_caso_actual} es de {tiempo_en_minutos:.1f} minutos \n")

# ---------------------------------------- EJERCICIO 4 DEL RETO -------------------------------------------
# Función para transformar las coordenadas delitos de sistema geográfico al sistema proyectado.
def convertir_coordenadas_delitos(delitos, sistema_referencia_origen, sistema_referencia_destino):
    delitos_transformados = []

    for delito in delitos:
        coordenadas = delito["Coordenadas"]
        latitud = coordenadas["Latitud"]
        longitud = coordenadas["Longitud"]
        x, y = transformer.transform(latitud, longitud)
        delito_transformado = {
            "Núm. caso": delito["Núm. caso"],
            "Descripción": delito["Descripción"],
            "Arrestado": delito["Arrestado"],
            "Núm. área comunitaria": delito["Núm. área comunitaria"],
            "Cuadra": delito["Cuadra"],
            "Fecha": delito["Fecha"],
            "Coordenadas geográficas": {
                "Latitud": latitud,
                "Longitud": longitud
            },
            "Coordenadas proyectadas": {
                "X": x,
                "Y": y
            }
        }
        delitos_transformados.append(delito_transformado)
    return delitos_transformados

# Función que transforma las coordenadas comisarias de sistema geográficas a coordenadas proyectadas.
def convertir_coordenadas_comisarias(comisarias, sistema_referencia_origen, sistema_referencia_destino):
    comisarias_transformadas = []

    for comisaria in comisarias:
        latitud_comisaria = comisaria["Coordenadas"]["Latitud"]
        longitud_comisaria = comisaria["Coordenadas"]["Longitud"]
        nombre_comisaria = comisaria["Nombre del Distrito"]
        x, y = transformer.transform(latitud_comisaria, longitud_comisaria)
        comisaria_transformada = {
            "Nombre del Distrito": nombre_comisaria,
            "Coordenadas geográficas": {
                "Latitud": latitud_comisaria,
                "Longitud": longitud_comisaria
            },
            "Coordenadas proyectadas": {
                "X": x,
                "Y": y
            }
        }
        comisarias_transformadas.append(comisaria_transformada)
    return comisarias_transformadas

# Función para calcular la distancia entre dos puntos.
def calcular_distancia(punto1, punto2):
    return np.sqrt((punto1['X'] - punto2['X'])**2 + (punto1['Y'] - punto2['Y'])**2)

# Función para ncontrar la comisaría más cercana a cada delito y guardar esa comisaria en la información del delito.
def encontrar_comisaria_mas_cercana():
    delitos_transformados = convertir_coordenadas_delitos(delitos, sistema_referencia_origen, sistema_referencia_destino)
    comisarias_transformadas = convertir_coordenadas_comisarias(comisarias, sistema_referencia_origen, sistema_referencia_destino)
    resultados = []

    for delito in delitos_transformados:
        coordenadas_delito = delito['Coordenadas proyectadas']
        distancia_minima = float('inf')
        comisaria_cercana = None

        for comisaria in comisarias_transformadas:
            coordenadas_comisaria = comisaria['Coordenadas proyectadas']
            distancia = calcular_distancia(coordenadas_delito, coordenadas_comisaria)

            if distancia < distancia_minima:
                distancia_minima = distancia
                comisaria_cercana = comisaria

        if distancia_minima < 1000:
            distancia = f"{distancia_minima:.2f} metros"
        else:
            distancia = f"{distancia_minima / 1000:.2f} kilómetros"

        resultados.append({
            "Núm. caso": delito["Núm. caso"],
            "Descripción": delito["Descripción"],
            "Arrestado": delito["Arrestado"],
            "Núm. área comunitaria": delito["Núm. área comunitaria"],
            "Cuadra": delito["Cuadra"],
            "Fecha": delito["Fecha"],
            "Coordenadas geográficas": delito["Coordenadas geográficas"],
            "Coordenadas proyectadas": delito["Coordenadas proyectadas"],
            "Comisaria más cercana": comisaria_cercana["Nombre del Distrito"],
            "Distancia a la comisaria más cercana": distancia
        })

    # Mostramos los delitos y la comisaría más cercana
    for delito in resultados:
        print(f"Núm. caso del delito: {delito['Núm. caso']}")
        print(f" - Descripción del delito: {delito['Descripción']}")
        print(f" - Comisaria más cercana al delito: {delito['Comisaria más cercana']}")
        print(f" - Distancia entre el delito cometido y la comisaría: {delito['Distancia a la comisaria más cercana']}")

# ---------------------------------------- LLAMAMOS A MAIN -------------------------------------------

# LLamamos a main. La función main() la hemos definido para establecer un menú con el que pueda interactuar el usuario "Agente de Policía".
main()




