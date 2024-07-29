
class Computadora:
    def __init__(self):
        self.cpu = None
        self.ram = None
 
    def __str__(self):
        return f"Computadora con CPU: {self.cpu}, RAM: {self.ram}"


class Constructor():
    def agregar_cpu(self, cpu):
        pass

    def agregar_ram(self, ram):
        pass

    def obtener_computadora(self):
        pass

class ConstructorConcreto(Constructor):
    def __init__(self):
        self._computadora = Computadora()

    def agregar_cpu(self, cpu: str) -> None:
        self._computadora.cpu = cpu

    def agregar_ram(self, ram: str) -> None:
        self._computadora.ram = ram

    def obtener_computadora(self) -> Computadora:
        return self._computadora


class Director:
    def __init__(self, constructor: Constructor):
        self._constructor = constructor

    def construir_computadora_gaming(self):
        self._constructor.agregar_cpu("Amd r7")
        self._constructor.agregar_ram("32GB")
    def construir_computadora_basica(self):
        self._constructor.agregar_cpu("Intel i5")
        self._constructor.agregar_ram("8GB")

# Crear un constructor concreto
constructor = ConstructorConcreto()

# Crear un director con el constructor
director = Director(constructor)

# Construir una computadora de gaming
director.construir_computadora_gaming()
computadora_gaming = constructor.obtener_computadora()
print(f"Computadora Gaming: {computadora_gaming}")

# Reconstruir la computadora básica
constructor = ConstructorConcreto()
director = Director(constructor)
director.construir_computadora_basica()
computadora_basica = constructor.obtener_computadora()
print(f"Computadora Básica: {computadora_basica}")

