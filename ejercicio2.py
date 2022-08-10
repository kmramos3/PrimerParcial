class Operar:
    
    def __init__(self, carne, nombre, facultad, numero) -> None:
        self._carne = carne
        self._nombre = nombre
        self._facultad = facultad
        self._numero = numero

    def datos(self):
        return f"Carne: {self._carne}, Nombre: {self._nombre}, Facultad: {self._facultad}" 

    def __str__(self) -> str:
        return f"Carne: {self._carne}, Nombre: {self._nombre}, Facultad: {self._facultad}, Numero: {self._numero}" 
    

if __name__ == "__main__":
    operar = Operar(201801234, "Juan Perez", "Ingenieria", 12345678)
    print(operar.datos())
    print(operar)
