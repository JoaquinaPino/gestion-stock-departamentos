# PROYECTO MÓDULO 3: Sistema de Gestión de Stock - Corredora de Propiedades

## Sobre el proyecto
Este programa fue diseñado para gestionar el inventario de departamentos de una corredora. Permite registrar nuevas propiedades, listarlas en una tabla organizada, buscar fichas técnicas por ID y generar cotizaciones de pago inicial con cálculos de proyección a futuro.

## Funciones Principales
- **Validación de Entradas:** Control de tipos de datos (números, texto, opciones de lista) y prevención de IDs duplicados.
- **Visualización de Datos:** Tabla dinámica con formato de tipología corta (ej: 2D+1B (E,T)) para optimizar el espacio en consola.
- **Cálculo Financiero:** Desglose de costos de arriendo, garantía, comisión y gastos administrativos, descontando abonos de reserva.
- **Proyección IPC (Recursividad):** Función que proyecta el valor del arriendo a 5 años aplicando un reajuste estimado del 5% anual.
- **Persistencia en CSV:** Guardado automático de toda la información al cerrar el programa.

## Instalación y Uso
1. Clonar el repositorio o descargar la carpeta `PROYECTO_MODULO_3`.
2. Abrir una terminal en la carpeta raíz que contiene el proyecto.
3. **Importante:** Entrar a la carpeta del proyecto antes de ejecutar:
   `cd PROYECTO_MODULO_3`
4. Ejecutar el programa:
   `python gestion_stock/main.py`

## Estructura del Código
El proyecto sigue una arquitectura modular para facilitar el mantenimiento:
- `main.py`: Orquestador del menú y flujo principal.
- `modelo/`: Contiene `constantes.py` (listas estáticas) y `datos.py` (estado del inventario).
- `servicios/`: `logica_departamento.py` contiene todas las funciones de procesamiento y exportación.
- `utilitarios/`: `validaciones.py` maneja la limpieza y verificación de inputs del usuario.

## Ejemplo de Datos
Se utilizaron datos reales de departamentos en Santiago para las pruebas de estrés del sistema:

|ID | DIRECCION | COMUNA | METRO | TIPOLOGIA | PRECIO | ESTADO
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|LINE-1611 | ECUADOR 4579 | ESTACIÓN CENTRAL | ECUADOR | 2D+2B | 436000 | DISPONIBLE
|HC2-813 | VENECIA 1605 | INDEPENDENCIA | PLAZA CHACABUCO | 2D+1B (E) | 440000 | RESERVADO
|DIA-5646 | DIAGONAL ORIENTE 5646B | ÑUÑOA | PLAZA EGAÑA | 4D+3B (B, E, T) | 1300000 | RESERVADO
|LAZ-1302 | LAZO 1456 | SAN MIGUEL | EL LLANO | 1D+1B (B, E) | 325000 | DISPONIBLE
|SEN-709 | LOD COCHRANE 173 | SANTIAGO CENTRO | MONEDA | 3D+2B (E, T) | 580000 | DISPONIBLE
|NSE-1932 | PADRE ORELLANA 1646 | SANTIAGO CENTRO | ÑUBLE | 2D+1B (B) | 420000 | ARRENDADO
|PV3-131 | EL MOLINO 1845 | INDEPENDENCIA | HOSPITALES | 1D+1B (T) | 280000 | ARRENDADO
|AL3-1313 | PADRE HURTADO 39 | ESTACIÓN CENTRAL | PADRE HURTADO | 1D+1B | 300000 | DISPONIBLE


## Salida de Datos
Al cerrar el sistema (Opción 6), se genera o actualiza el archivo:
- `salidas/planilla_arriendos.csv`: Incluye el detalle completo (ID, Dirección, Comuna, Metro, Tipología, Precio y Estado).

## Desafíos Técnicos
El mayor reto fue implementar la **recursividad** para el cálculo del IPC de forma que fuera útil para el usuario y cumpliera con los requisitos del módulo. También se puso especial énfasis en la **limpieza de la terminal**, usando saltos de línea y separadores para que la experiencia de uso sea cómoda.