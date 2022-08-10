import datetime

class Vehiculo:
    def __init__(self, marca, modelo, color) -> None:
        self._marca = marca
        self._modelo = modelo
        self._color = color

class Sedan(Vehiculo):

    def __init__(self, marca, modelo, color) -> None:
        super().__init__(marca, modelo, color)

    def validar(self):
        if (self._modelo < 2000):
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = int(date.strftime("%Y"))
            message = f"El vehículo ya tiene más de {year - self._modelo} años, marca {self._marca}, color {self._color} modelo {self._modelo}"
            print(message)

class HatchBack(Vehiculo):

    def __init__(self, marca, modelo, color) -> None:
        super().__init__(marca, modelo, color)

    def validar(self):
        if self._modelo >= 2000 and self._modelo <= 2015:
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = int(date.strftime("%Y"))
            message = f"El vehículo ya tiene más de {year - self._modelo} años, marca {self._marca}, color {self._color} modelo {self._modelo}"
            print(message)


class PickUp(Vehiculo):
    def __init__(self, marca, modelo, color) -> None:
        super().__init__(marca, modelo, color)

    def validar(self):
        if self._modelo >= 2015 and self._modelo <= 2019:
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = int(date.strftime("%Y"))
            message = f"El vehículo ya tiene más de {year - self._modelo} años, marca {self._marca}, color {self._color} modelo {self._modelo}"
            print(message)


if __name__ == "__main__":
    sedan = Sedan("Toyota Yaris", 1999, "Rojo")
    sedan.validar()

    hatchBack = HatchBack("Mitsubishi", 2001, "Verde")
    hatchBack.validar()

    pickup = PickUp("Toyota", 2018, "Rojo")
    pickup.validar()
