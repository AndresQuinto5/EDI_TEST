class EDI2Calculator:
    def __init__(self, respuestas):
        # Guardar las respuestas del EDI-2
        self.respuestas = respuestas
        self.resultados = {
            "Impulso a la delgadez": 0,
            "Sintomatologia bulimica": 0,
            "Insatisfaccion corporal": 0,
            "Inefectividad y baja autoestima": 0,
            "Perfeccionismo": 0,
            "Desconfianza interpersonal": 0,
            "Conciencia interoceptiva": 0,
            "Miedo a madurar": 0
        }

    def calcular_puntuaciones(self):
        self.resultados["Impulso a la delgadez"] = self.calcular_impulso_delgadez()
        self.resultados["Sintomatologia bulimica"] = self.calcular_sintomatologia_bulimica()
        self.resultados["Insatisfaccion corporal"] = self.calcular_insatisfaccion_corporal()
        self.resultados["Inefectividad y baja autoestima"] = self.calcular_inefectividad()
        self.resultados["Perfeccionismo"] = self.calcular_perfeccionismo()
        self.resultados["Desconfianza interpersonal"] = self.calcular_desconfianza_interpersonal()
        self.resultados["Conciencia interoceptiva"] = self.calcular_conciencia_interoceptiva()
        self.resultados["Miedo a madurar"] = self.calcular_miedo_madurar()

    def ingresar_respuestas(self):
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

    def calcular_sintomatologia_bulimica(self):
        # Lógica para calcular "Sintomatología bulímica"
        items_comunes = [4, 5, 28, 38, 46, 53, 61]
        puntuacion = 0
        
        for item in items_comunes:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6:
                puntuacion += 3
            elif respuesta == 5:
                puntuacion += 2
            elif respuesta == 4:
                puntuacion += 1
                
        return puntuacion

    def calcular_insatisfaccion_corporal(self):
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

    def calcular_inefectividad(self):
        # Lógica para calcular "Inefectividad y baja autoestima"
        set_1 = [10, 18, 24, 27, 41, 56]
        puntuacion = 0
        
        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6: # Siempre
                puntuacion += 3
            elif respuesta == 5: # Habitualmente
                puntuacion += 2
            elif respuesta == 4: # A menudo
                puntuacion += 1
        
        set_2 = [20, 37, 42, 50]
        
        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1: # Nunca
                puntuacion += 3
            elif respuesta == 2: # Raramente
                puntuacion += 2
            elif respuesta == 3: # Algunas veces
                puntuacion += 1
        return puntuacion

    def calcular_perfeccionismo(self):
        # Lógica para calcular "Perfeccionismo"
        items_comunes = [13, 29, 36, 43, 52, 63]
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

    def calcular_desconfianza_interpersonal(self):
        # Lógica para calcular "Desconfianza interpersonal"
        set_1 = [34, 54]
        puntuacion = 0
        
        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6: # Siempre
                puntuacion += 3
            elif respuesta == 5: # Habitualmente
                puntuacion += 2
            elif respuesta == 4: # A menudo
                puntuacion += 1
        
        set_2 = [15, 17, 23, 30 ,57]
        
        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1: # Nunca
                puntuacion += 3
            elif respuesta == 2: # Raramente
                puntuacion += 2
            elif respuesta == 3: # Algunas veces
                puntuacion += 1
        return puntuacion

    def calcular_conciencia_interoceptiva(self):
        # Lógica para calcular "Conciencia interoceptiva"
        items_comunes = [8 ,21, 33, 40, 44, 47, 51, 60, 64]
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
        respuesta_item_1 = self.respuestas.get(26, 0)
        if respuesta_item_1 == 1:  # Nunca
            puntuacion += 3
        elif respuesta_item_1 == 2:  # Raramente
            puntuacion += 2
        elif respuesta_item_1 == 3:  # Algunas veces
            puntuacion += 1

        return puntuacion

    def calcular_miedo_madurar(self):
        # Lógica para calcular "Miedo a madurar"
        set_1 = [3, 6, 14, 22, 35, 39, 48, 58]
        puntuacion = 0
        
        for item in set_1:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 6: # Siempre
                puntuacion += 3
            elif respuesta == 5: # Habitualmente
                puntuacion += 2
            elif respuesta == 4: # A menudo
                puntuacion += 1
        
        set_2 = [22, 39, 58]
        
        for item in set_2:
            respuesta = self.respuestas.get(item, 0)
            if respuesta == 1: # Nunca
                puntuacion += 3
            elif respuesta == 2: # Raramente
                puntuacion += 2
            elif respuesta == 3: # Algunas veces
                puntuacion += 1
        return puntuacion

    def obtener_resultados(self):
        return self.resultados

if __name__ == "__main__":
    calculadora = EDI2Calculator()
    calculadora.ingresar_respuestas()
    calculadora.calcular_puntuaciones()
    resultados = calculadora.obtener_resultados()

    print("\nResultados EDI-2:")
    for metrica, puntuacion in resultados.items():
        print(f"{metrica}: {puntuacion}")