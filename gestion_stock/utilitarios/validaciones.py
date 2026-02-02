# Validación y obtención de números enteros (precio y número de departamento)
def evaluar_numero_entero(mensaje, clave, rango, minimo=1):
    while True:
        valor_ingresado = input(f"\n{mensaje}")
        try:
            valor = int(valor_ingresado)

            if valor >= minimo:
                if rango == None:
                    return valor
                elif minimo <= valor <= rango:
                    return valor
                else:
                    mensaje_error = "mayor a cero" if minimo == 1 else f"mayor o igual a {minimo}"
                    print(f"\n{'-'*40}")
                    print(f"Error: El campo '{clave}' debe ser {mensaje_error}")
                    print(f"{'-'*40}\n")
            else:
                print(f"\n{'-'*40}")
                print(f"Error: El campo '{clave}' debe ser mayor a cero")
                print(f"{'-'*40}\n")

        except ValueError:
            print(f"\n{'-'*40}")
            print(f"Error: El campo '{clave}' debe tener un valor numérico")
            print(f"{'-'*40}\n")

# Validación y obtención de texto para sigla y dirección
def evaluar_texto(mensaje, clave):
    while True:
        texto = input(f"\n{mensaje}").strip().upper()
        
        if len(texto) > 0:
            return texto
        else:
            print(f"\n{'-'*40}")
            print(f"Error: El campo '{clave}' no puede estar vacío.")
            print(f"{'-'*40}\n")

# Validación y obtención de entrada de listas
def evaluar_opcion_lista(lista_opciones, clave):
    print(f"\nSeleccione {clave}:")

    for i, opcion in enumerate(lista_opciones, start=1):
        print(f"{i}. {opcion}")

    while True:
        entrada = input(f"\nIngrese número de opción para {clave}: \n>>> ")
        try:
            indice = int(entrada) - 1
            
            if 0 <= indice < len(lista_opciones):
                return lista_opciones[indice] 
            else:
                print(f"\n{'-'*40}")
                print("Error: Opción fuera de rango.")
                print(f"{'-'*40}\n")
                
        except ValueError:
            print(f"\n{'-'*40}")
            print("Error: Debe ingresar el número de la opción.")
            print(f"{'-'*40}\n")


