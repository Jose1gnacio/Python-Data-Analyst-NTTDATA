import mysql.connector

# Función consulta delitos
def buscar_delitos_por_valor():
    # Solicitar al usuario el valor de búsqueda
    valor = input("Introduce el valor a buscar: ")

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chicago_safety_data"
        )
        cursor = conexion.cursor()

        # Consulta SQL para buscar delitos que coincidan con el valor proporcionado en cualquier campo
        consulta = '''
            SELECT * FROM delitos
            WHERE num_caso LIKE %s
            OR descripcion LIKE %s
            OR cuadra LIKE %s
            OR fecha LIKE %s
            OR latitud LIKE %s
            OR longitud LIKE %s
        '''

        # Agrega comodines para buscar coincidencias parciales
        valor_busqueda = '%' + valor + '%'

        # Ejecutar la consulta con el mismo valor de búsqueda aplicado a todos los campos
        cursor.execute(consulta, (valor_busqueda, valor_busqueda, valor_busqueda, valor_busqueda, valor_busqueda, valor_busqueda))

        # Obtener resultados de la consulta
        resultados = cursor.fetchall()

        # Imprimir los resultados
        if resultados:
            print("\nSe encontraron los siguientes delitos:")
            for resultado in resultados:
                print(f"""
                Número de caso: {resultado[1]}
                Descripción: {resultado[2]}
                Arrestado: {resultado[3]}
                Área comunitaria: {resultado[4]}
                Cuadra: {resultado[5]}
                Fecha: {resultado[6]}
                Latitud: {resultado[7]}
                Longitud: {resultado[8]}
                """)
        else:
            print("\nNo se encontraron delitos que coincidan con el valor proporcionado.\n")

    except mysql.connector.Error as error:
        print("\nError al conectar a la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función mostrar delitos
def mostrar_todos_los_delitos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chicago_safety_data"
        )
        cursor = conexion.cursor()

        # Consulta SQL para obtener todos los delitos
        consulta = '''
            SELECT * FROM delitos
        '''

        # Ejecutar la consulta
        cursor.execute(consulta)

        # Obtener resultados de la consulta
        resultados = cursor.fetchall()

        # Imprimir los resultados
        if resultados:
            print("Listado de todos los delitos:")
            for resultado in resultados:
                print(f"""
                Número de caso: {resultado[1]}
                Descripción: {resultado[2]}
                Arrestado: {resultado[3]}
                Área comunitaria: {resultado[4]}
                Cuadra: {resultado[5]}
                Fecha: {resultado[6]}
                Latitud: {resultado[7]}
                Longitud: {resultado[8]}
                """)
        else:
            print("\nNo se encontraron delitos en la base de datos.\n")

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para editar un delito
def editar_delito():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chicago_safety_data"
        )
        cursor = conexion.cursor()

        # Pedir al usuario el número de caso del delito a editar
        num_caso = input("Ingrese el número de caso del delito que desea editar: ")

        # Verificar si el delito existe en la base de datos
        consulta_existencia = "SELECT * FROM delitos WHERE num_caso = %s"
        cursor.execute(consulta_existencia, (num_caso,))
        delito = cursor.fetchone()

        if not delito:
            print("El delito con el número de caso especificado no existe.")
            return

        # Pedir al usuario el parámetro a editar
        print("Seleccione el parámetro que desea editar:")
        print("1. Descripción")
        print("2. Arrestado")
        print("3. Área comunitaria")
        print("4. Cuadra")
        print("5. Fecha")
        print("6. Latitud")
        print("7. Longitud")
        opcion = int(input("Ingrese el número correspondiente al parámetro: "))

        # Pedir al usuario el nuevo valor para el parámetro seleccionado
        if opcion == 2:  # Si se selecciona el parámetro "Arrestado"
            nuevo_valor = input("Ingrese el nuevo valor para el parámetro seleccionado (true/false): ").lower()
            # Convertir el valor a un booleano apropiado
            nuevo_valor = nuevo_valor == "true"
        else:
            nuevo_valor = input("Ingrese el nuevo valor para el parámetro seleccionado: ")

        # Actualizar el delito en la base de datos según el parámetro seleccionado
        campos = ["descripcion", "arrestado", "area_comunitaria", "cuadra", "fecha", "latitud", "longitud"]
        campo_actualizar = campos[opcion - 1]

        consulta_actualizacion = f"UPDATE delitos SET {campo_actualizar} = %s WHERE num_caso = %s"
        cursor.execute(consulta_actualizacion, (nuevo_valor, num_caso))
        conexion.commit()

        print("El delito ha sido actualizado correctamente.")

    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

   


#if __name__ == "__main__":
    #editar_delito()
    #buscar_delitos_por_valor()