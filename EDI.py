class EDI2Calculator:
    """
    Esta clase permite calcular las puntuaciones de las subescalas del EDI-2
    basándose en las respuestas proporcionadas por el usuario.

    Atributos:
        respuestas (dict): Diccionario que contiene las respuestas de los ítems.
        resultados (dict): Diccionario que contiene las puntuaciones calculadas para cada subescala.
    """

    def __init__(self):
        """
        Inicializa la clase con un diccionario vacío para las respuestas y otro para los resultados.
        """
        self.respuestas = {}
        self.resultados = {
            "Impulso a la delgadez": 0,
            "Sintomatología bulímica": 0,
            "Insatisfacción corporal": 0,
            "Inefectividad y baja autoestima": 0,
            "Perfeccionismo": 0,
            "Desconfianza interpersonal": 0,
            "Conciencia interoceptiva": 0,
            "Miedo a madurar": 0
        }
        self.nombre_paciente = input("Ingrese el nombre completo de la paciente: ")
        edad_input = input("Ingrese la edad de la paciente (o presione Enter para NA): ")
        self.edad_paciente = edad_input if edad_input else "NA"

    def ingresar_respuestas(self):
        """
        Solicita al usuario ingresar las respuestas para cada ítem del cuestionario.
        Las respuestas deben estar en el rango de 1 a 6.
        """
        print("Ingrese las respuestas para cada ítem (1-6):")
        for i in range(1, 65):
            while True:
                try:
                    respuesta = int(input(f"Ítem {i}: "))
                    if respuesta in range(1, 7):
                        self.respuestas[i] = respuesta
                        break
                    else:
                        print("Por favor, ingrese un número entre 1 y 6.")
                except ValueError:
                    print("Entrada inválida. Ingrese un número entero entre 1 y 6.")

    def calcular_impulso_delgadez(self):
        """
        Calcula la puntuación para la subescala 'Impulso a la delgadez'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        items_comunes = [7, 11, 16, 25, 32, 49]
        puntuacion = 0

        # Escalado para ítems 7, 11, 16, 25, 32, 49
        for item in items_comunes:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        # Escalado específico para el ítem 1
        respuesta_item_1 = self.respuestas.get(1, 0)
        if respuesta_item_1 == 1:  # Nunca
            puntuacion += 3
        elif respuesta_item_1 == 2:  # Raramente
            puntuacion += 2
        elif respuesta_item_1 == 3:  # Algunas veces
            puntuacion += 1

        return puntuacion

    def calcular_insatisfaccion_corporal(self):
        """
        Calcula la puntuación para la subescala 'Insatisfacción corporal'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        # Set 1: Ítems 2, 9, 45, 59
        set_1 = [2, 9, 45, 59]
        puntuacion = 0

        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        # Set 2: Ítems 12, 19, 31, 55, 62
        set_2 = [12, 19, 31, 55, 62]

        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1:  # Nunca
                puntuacion += 3
            elif respuesta == 2:  # Raramente
                puntuacion += 2
            elif respuesta == 3:  # Algunas veces
                puntuacion += 1

        return puntuacion

    def calcular_sintomatologia_bulimica(self):
        """
        Calcula la puntuación para la subescala 'Sintomatología bulímica'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        items_comunes = [4, 5, 28, 38, 46, 53, 61]
        puntuacion = 0

        for item in items_comunes:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6: # Siempre
                puntuacion += 3
            elif respuesta == 5: # Habitualmente
                puntuacion += 2
            elif respuesta == 4: # A menudo
                puntuacion += 1

        return puntuacion

    def calcular_inefectividad(self):
        """
        Calcula la puntuación para la subescala 'Inefectividad y baja autoestima'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        set_1 = [10, 18, 24, 27, 41, 56]
        puntuacion = 0

        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        set_2 = [20, 37, 42, 50]

        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1:  # Nunca
                puntuacion += 3
            elif respuesta == 2:  # Raramente
                puntuacion += 2
            elif respuesta == 3:  # Algunas veces
                puntuacion += 1

        return puntuacion

    def calcular_perfeccionismo(self):
        """
        Calcula la puntuación para la subescala 'Perfeccionismo'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        items_comunes = [13, 29, 36, 43, 52, 63]
        puntuacion = 0

        for item in items_comunes:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        return puntuacion

    def calcular_desconfianza_interpersonal(self):
        """
        Calcula la puntuación para la subescala 'Desconfianza interpersonal'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        set_1 = [34, 54]
        puntuacion = 0

        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        set_2 = [15, 17, 23, 30, 57]

        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1:  # Nunca
                puntuacion += 3
            elif respuesta == 2:  # Raramente
                puntuacion += 2
            elif respuesta == 3:  # Algunas veces
                puntuacion += 1

        return puntuacion

    def calcular_conciencia_interoceptiva(self):
        """
        Calcula la puntuación para la subescala 'Conciencia interoceptiva'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        items_comunes = [8, 21, 33, 40, 44, 47, 51, 60, 64]
        puntuacion = 0

        for item in items_comunes:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        # Escalado específico para el ítem 26
        respuesta_item_3 = self.respuestas.get(26, 0)
        if respuesta_item_3 == 1:  # Nunca
            puntuacion += 3
        elif respuesta_item_3 == 2:  # Raramente
            puntuacion += 2
        elif respuesta_item_3 == 3:  # Algunas veces
            puntuacion += 1

        return puntuacion

    def calcular_miedo_a_madurar(self):
        """
        Calcula la puntuación para la subescala 'Miedo a madurar'.

        Retorna:
            int: Puntuación total para la subescala.
        """
        set_1 = [3, 6, 14, 35, 48]
        puntuacion = 0

        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:  # Siempre
                puntuacion += 3
            elif respuesta == 5:  # Habitualmente
                puntuacion += 2
            elif respuesta == 4:  # A menudo
                puntuacion += 1

        set_2 = [22, 39, 58]

        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1:  # Nunca
                puntuacion += 3
            elif respuesta == 2:  # Raramente
                puntuacion += 2
            elif respuesta == 3:  # Algunas veces
                puntuacion += 1

        return puntuacion

    def calcular_todas_subescalas(self):
        """
        Calcula las puntuaciones para todas las subescala y actualiza el diccionario de resultados.
        """
        self.resultados["Impulso a la delgadez"] = self.calcular_impulso_delgadez()
        self.resultados["Sintomatología bulímica"] = self.calcular_sintomatologia_bulimica()
        self.resultados["Insatisfacción corporal"] = self.calcular_insatisfaccion_corporal()
        self.resultados["Inefectividad y baja autoestima"] = self.calcular_inefectividad()
        self.resultados["Perfeccionismo"] = self.calcular_perfeccionismo()
        self.resultados["Desconfianza interpersonal"] = self.calcular_desconfianza_interpersonal()
        self.resultados["Conciencia interoceptiva"] = self.calcular_conciencia_interoceptiva()
        self.resultados["Miedo a madurar"] = self.calcular_miedo_a_madurar()

    def mostrar_resultados(self):
        """
        Muestra los resultados calculados para cada subescala, junto con la información de la paciente.
        """
        print("\nResultados de las subescalas del EDI-2:")
        print(f"Nombre de la paciente: {self.nombre_paciente}")
        print(f"Edad de la paciente: {self.edad_paciente}\n")
        for subescala, puntuacion in self.resultados.items():
            print(f"{subescala}: {puntuacion}")

# Ejemplo de uso
edi_calculator = EDI2Calculator()
edi_calculator.ingresar_respuestas()
edi_calculator.calcular_todas_subescalas()
edi_calculator.mostrar_resultados()
