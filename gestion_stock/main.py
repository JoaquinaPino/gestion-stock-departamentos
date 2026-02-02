from utilitarios.validaciones import *
from servicios.logica_departamento import *
from modelo.constantes import *

print("\n--- SISTEMA PARA GESTIÓN DE ARRIENDOS ---")

while True:

    print("\n" + "=" * 60)

    OPCIONES_MENU = (
        "¿Qué deseas hacer hoy? \n"
        "\n1. Registrar un nuevo departamento \n"
        "2. Ver base de datos de departamentos \n"
        "3. Buscar Departamento \n"
        "4. Cuadro de pago \n"
        "5. Cambiar estado departamento \n"
        "6. Salir \n"
        "\n>>> ")

    opcion = evaluar_numero_entero(OPCIONES_MENU, "opciones", 6)

    if opcion == 1:
        registrar_departamento()

    elif opcion == 2:
        listar_departamento()

    elif opcion == 3:
        buscar_departamento()

    elif opcion == 4:
        mostrar_cuadro_pago()

    elif opcion == 5:
        cambiar_estado_departamento()

    elif opcion == 6:
        print("Cerrando sistema...")
        if len(inventario_deptos) > 0:
            exportar_datos_csv()
            
        print("¡Hasta luego!")
        break