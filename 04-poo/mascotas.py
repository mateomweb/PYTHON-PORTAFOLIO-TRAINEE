class Mascota:
    def __init__(self, nombre, especie, energia):
        self.nombre = nombre
        self.especie = especie
        self.energia = energia

    def jugar(self, horas):
        self.energia = self.energia - (horas * 10)
        print(f"{self.nombre} jugó durante {horas} horas ! Su energía ha bajado")

    def mostrar_info(self):
        print("INFORMACIÓN DE LA MASCOTA ")
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Energía Actual: {self.energia}%")
        print("----------------------------------")

mascota1 = Mascota("Firulais", "Perro", 80)
mascota2 = Mascota("Michi", "Gato", 95)

mascota1.mostrar_info()
mascota2.mostrar_info()

mascota1.jugar(2)

mascota1.mostrar_info()
