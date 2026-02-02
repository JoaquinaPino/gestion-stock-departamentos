import os
from utilitarios.validaciones import *
from modelo.constantes import *
from modelo.datos import inventario_deptos

def registrar_departamento():
    while True:
        print("\nREGISTRO DE DEPARTAMENTO")
        print(f"\n{'-'*40}")

        print("\n1. IDENTIFICACIÓN")
        
        sigla = evaluar_texto("Ingrese sigla del edificio (ej: SCL): \n>>> ", "sigla")
        depto = evaluar_numero_entero("Ingrese número de departamento (ej: 1004): \n>>> ", "número de departamento", None)
        id_unico = f"{sigla}-{depto}"

        if id_unico in inventario_deptos:
            print(f"\n{'-'*40}")
            print(f"Error: El departamento {id_unico} ya existe en el sistema.")
            print(f"{'-'*40}\n")
            print("¿Desea intentar con otro ID?")
            opcion = evaluar_numero_entero("1. Sí \n2. Volver al menú \n>>> ", "opción", 2)
            if opcion == 1:
                continue
            else:
                break

        print(f"\n{'-'*40}")
        print("\n2. UBICACIÓN")
        
        direccion = evaluar_texto("Ingrese  dirección completa (ej: av. providencia 123): \n>>> ", "dirección")
        lista_comunas = list(COMUNA_METRO.keys())
        comuna = evaluar_opcion_lista(lista_comunas, "Comuna")
        lista_estaciones = COMUNA_METRO[comuna]
        estacion = evaluar_opcion_lista(lista_estaciones, "estación de metro")

        print(f"\n{'-'*40}")
        print("\n3. CARACTERÍSTICAS")
        
        dormitorios = evaluar_numero_entero("Ingrese cantidad de dormitorios (1-5): \n>>> ", "cantidad de dormitorios", 5)
        baños = evaluar_numero_entero("Ingrese cantidad de baños (1-5): \n>>> ", "cantidad de baños", 5)       
        
        set_extras = set()

        for extra in OPCIONES_EXTRAS:
            opcion_extra = evaluar_numero_entero(f"¿Incluye {extra}? (1-2) \n1. Sí \n2. No \n>>> ", extra, 2)
            if opcion_extra == 1:
                set_extras.add(extra)

        str_extras = ", ".join(sorted(set_extras))

        print(f"\n{'-'*40}")
        print("\n4. VALOR Y DISPONIBILIDAD")
        
        precio = evaluar_numero_entero("Ingrese canon de arriendo del departamento (sin puntos ni comas): \n>>> $", "canon de arriendo", None)
        estado = evaluar_opcion_lista(ESTADO, "disponibilidad" )

        nuevo_depto = {
            "id": id_unico,
            "direccion": direccion,
            "comuna": comuna,
            "metro": estacion,
            "dormitorios": dormitorios,
            "baños": baños,
            "extras": str_extras,
            "precio": precio,
            "estado": estado
        }

        inventario_deptos[id_unico] = nuevo_depto
        print(f"\n{'-'*60}")
        print(f"Departamento {id_unico} registrado correctamente")
        print(f"{'-'*60}")

        print("\n¿Qué desea hacer ahora?")
        print("1. Registrar nuevo departamento")
        print("2. Volver al Menú Principal")
        
        decision = evaluar_numero_entero(">>> ", "opción", 2)
        
        if decision == 2:
            break

def listar_departamento():

    while True:
        print("\n--- BASE DE DATOS DE DEPARTAMENTOS ---")

        if len(inventario_deptos) == 0:
            print("Aún no hay departamentos registrados.")
            input("\nPresione Enter para volver al menú principal... ")
            break
        
        print(f"{'ID':<10} | {'TIPOLOGÍA':<15} | {'PRECIO':<10} | {'COMUNA':<15} | {'ESTADO':<10}")
        print("-" * 75)

        for id_depto, datos in inventario_deptos.items():
            
            tipologia_str = formatear_tipologia(
                datos['dormitorios'],
                datos['baños'],
                datos['extras']
            )

            precio = datos['precio']
            comuna = datos['comuna']
            estado = datos['estado']

            print(f"{id_depto:<10} | {tipologia_str:<15} | ${precio:<9} | {comuna:<15} | {estado:<10}")

        print("-" * 75)

        print("\nOpciones de Base de Datos:")
        print("1. Filtrar departamentos (Próximamente)")
        print("2. Volver al Menú Principal")
        
        opcion = evaluar_numero_entero("Seleccione una opción: \n>>> ", "opción", 2)
        
        if opcion == 1:
            print("\nFuncionalidad de filtro en construcción...")
            input("Presione Enter para continuar... ")

        elif opcion == 2:
            break

def formatear_tipologia(dormitorios, baños, str_extras):

    lista_extras = str_extras.split(", ")

    siglas = []

    for item in lista_extras:
        if item in MAPA_EXTRAS:
            siglas.append(MAPA_EXTRAS[item])

    txt_extras = ",".join(siglas)
    
    if txt_extras:
        return f"{dormitorios}D+{baños}B ({txt_extras})"
    else:
        return f"{dormitorios}D+{baños}B"
    
def buscar_departamento():
    print("\nBUSCADOR DE DEPARTAMENTOS")
    print(f"{'-'*40}")
    
    id_buscado = evaluar_texto("Ingrese el ID del departamento (ej: PN-1032): \n>>> ", "ID")
    
    if id_buscado in inventario_deptos:
        depto = inventario_deptos[id_buscado]
        
        tipologia = formatear_tipologia(depto['dormitorios'], depto['baños'], depto['extras'])
        
        print(f"\n{'-'*40}")
        print(f"FICHA TÉCNICA: {id_buscado}")
        print(f"{'-'*40}")
        
        print(f"- Edificio/Depto:  {id_buscado}")
        print(f"- Dirección:       {depto['direccion']}")
        print(f"- Ubicación:       {depto['comuna']} (METRO {depto['metro']})")
        print(f"- Tipología:       {tipologia}")
        print(f"- Precio:          ${depto['precio']}")
        print(f"- Estado Actual:   {depto['estado']}")
        print(f"{'-'*40}")
        
        input("\nPresione Enter para volver al menú... ")
        
    else:
        print(f"\n{'-'*40}")
        print(f"Error: No se encontró ningún departamento con el ID '{id_buscado}'.")
        print(f"{'-'*40}")
        input("\nPresione Enter para continuar... ")

def calcular_proyeccion_ipc(monto_actual, año_actual, tope_años):
    
    if año_actual > tope_años:
        return 

    print(f"   Año {año_actual}: ${int(monto_actual):,}".replace(",", "."))
    
    nuevo_monto = monto_actual * 1.05 
    calcular_proyeccion_ipc(nuevo_monto, año_actual + 1, tope_años)

def mostrar_cuadro_pago():
    print("\nGENERADOR DE CUADRO DE PAGO")
    print(f"{'-'*50}")
    
    id_buscado = evaluar_texto("Ingrese el ID del departamento a cotizar: \n>>> ", "ID")
    
    if id_buscado not in inventario_deptos:
        print(f"\nError: El departamento {id_buscado} no existe.")
        return

    datos_depto = inventario_deptos[id_buscado]
    canon_mensual = datos_depto['precio']
    
    print(f"\nAnalizando costos para depto {id_buscado} (Canon base: ${canon_mensual:,})")
    print(f"{'-'*50}")

    print("\n¿Aplica algún descuento por promoción?")
    descuento_pct = evaluar_numero_entero("Ingrese % descuento (0 para ninguno, 100 para gratis): \n>>> ", "%", 100, 0)
    
    if descuento_pct > 0:
        valor_primer_mes = int(canon_mensual * ((100 - descuento_pct) / 100))
        txt_descuento = f"(Desc. {descuento_pct}%)"
    else:
        valor_primer_mes = canon_mensual
        txt_descuento = ""

    valor_garantia = canon_mensual
    valor_comision = int(canon_mensual * 0.60)
    valor_admin = 60000
    valor_reserva = 100000

    subtotal = valor_primer_mes + valor_garantia + valor_comision + valor_admin
    total_final = subtotal - valor_reserva

    cat_arriendo = f"1. Mes de Arriendo {txt_descuento}"
    cat_garantia = "2. Mes de Garantía"
    cat_comision = "3. Comisión Corretaje (60%)"
    cat_admin = "4. Gastos Administrativos"
    cat_reserva = "- Abono Reserva"

    print(f"\n{'-'*52}")
    print(f"DETALLE DE PAGO INICIAL")
    print(f"{'-'*52}")
    
    print(f"{cat_arriendo:<35} : ${valor_primer_mes:>11,}".replace(",", "."))
    print(f"{cat_garantia:<35} : ${valor_garantia:>11,}".replace(",", "."))
    print(f"{cat_comision:<35} : ${valor_comision:>11,}".replace(",", "."))
    print(f"{cat_admin:<35} : ${valor_admin:>11,}".replace(",", "."))
    
    print(f"{'-'*52}")
    print(f"{'SUBTOTAL':<35} : ${subtotal:>11,}".replace(",", "."))
    print(f"{cat_reserva:<35} : -${valor_reserva:>10,}".replace(",", ".")) 
    
    print(f"{'='*52}")
    print(f"{'TOTAL A PAGAR FIRMA CONTRATO':<35} : ${total_final:>11,}".replace(",", "."))
    print(f"{'='*52}")

    print("\n¿Desea ver la proyección de valor a 5 años (IPC)?")
    print("Esto es útil para contratos de largo plazo.")
    opcion_ipc = evaluar_numero_entero("1. Sí, mostrar proyección \n2. No, volver al menú \n>>> ", "opción", 2)

    if opcion_ipc == 1:
        print(f"\n{'-'*40}")
        print("PROYECCIÓN DE ALZA (RECURSIVA)")
        print("Si renueva contrato anualmente (IPC est. 5%):")
        print(f"{'-'*40}")
        calcular_proyeccion_ipc(canon_mensual, 1, 5)
        input("\nPresione Enter para finalizar... ")
    else:
        print("\nVolviendo al menú...")

def cambiar_estado_departamento():
    print("\nACTUALIZAR ESTADO DE DEPARTAMENTO")
    print(f"{'-'*40}")
    
    id_buscado = evaluar_texto("Ingrese el ID del departamento: \n>>> ", "ID")
    
    if id_buscado in inventario_deptos:
        depto = inventario_deptos[id_buscado]
        estado_actual = depto['estado']
        
        print(f"\nEstado actual del {id_buscado}: [{estado_actual}]")
        
        print("\nSeleccione el nuevo estado:")
        nuevo_estado = evaluar_opcion_lista(ESTADO, "Nuevo Estado")
        
        depto['estado'] = nuevo_estado
        
        print(f"\n{'-'*40}")
        print(f"El departamento {id_buscado} ahora está {nuevo_estado}.")
        print(f"{'-'*40}")
        input("\nPresione Enter para volver... ")
        
    else:
        print(f"\nError: No se encontró el departamento {id_buscado}.")
        input("\nPresione Enter para continuar... ")

def exportar_datos_csv():

    carpeta_salida = "salidas"
    nombre_archivo = "planilla_arriendos.csv"
    ruta_completa = os.path.join(carpeta_salida, nombre_archivo)
    
    try:
        if not os.path.exists(carpeta_salida):
            os.makedirs(carpeta_salida)
            print(f"Directorio '{carpeta_salida}' creado.")

        with open(ruta_completa, 'w', encoding='utf-8') as archivo:
            linea_cabecera = ",".join(ENCABEZADOS_CSV) + "\n"
            archivo.write(linea_cabecera)
            
            for id_depto, datos in inventario_deptos.items():
                tipologia = formatear_tipologia(datos['dormitorios'], datos['baños'], datos['extras'])
                
                linea = (
                    f"{id_depto},"
                    f"{datos['direccion']},"
                    f"{datos['comuna']},"
                    f"{datos['metro']},"
                    f"{tipologia},"
                    f"{datos['precio']},"
                    f"{datos['estado']}\n"
                )
                archivo.write(linea)
                
        print(f"\nArchivo generado con éxito en: {ruta_completa}")
        
    except Exception as e:
        print(f"Error al exportar: {e}")