# EDI-2: Inventario de Trastornos de la Conducta Alimentaria

Este proyecto es una herramienta en Python diseñada para automatizar la calificación del Inventario de Trastornos de la Conducta Alimentaria (EDI-2). El EDI-2 es una prueba ampliamente utilizada en psicología para evaluar síntomas y comportamientos relacionados con los trastornos alimentarios.

## Descripción del Proyecto

La herramienta permite ingresar las respuestas de una paciente a los 64 ítems del EDI-2 y calcula automáticamente las puntuaciones para las 8 subescalas:

- **Impulso a la delgadez**
- **Sintomatología bulímica**
- **Insatisfacción corporal**
- **Inefectividad y baja autoestima**
- **Perfeccionismo**
- **Desconfianza interpersonal**
- **Conciencia interoceptiva**
- **Miedo a madurar**

Además, la herramienta permite registrar el nombre completo y la edad de la paciente, y muestra estos datos junto con los resultados de las subescalas.

## Requisitos Previos

Este proyecto requiere que tengas instalado Python 3.6 o superior. No se necesitan librerías externas adicionales.

## Uso

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/AndresQuinto5/EDI_TEST.git
    cd EDI_TEST
    ```

2. **Ejecutar el script**:
    ```bash
    python EDI.py
    ```

3. **Ingresar la información de la paciente**:
    - Se solicitará el nombre completo y la edad de la paciente. Si no se conoce la edad, puedes ingresar "NA".

4. **Ingresar las respuestas del test**:
    - El script te pedirá que ingreses las respuestas a los 64 ítems. Las opciones de respuesta son las siguientes:
        - 1: Nunca
        - 2: Raramente
        - 3: Algunas veces
        - 4: A menudo
        - 5: Habitualmente
        - 6: Siempre

5. **Ver los resultados**:
    - Al finalizar la entrada de las respuestas, el script mostrará las puntuaciones para cada subescala junto con la información de la paciente.

## Ejemplo de Uso

```bash
python EDI.py
