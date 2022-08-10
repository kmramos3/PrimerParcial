import math


class Cono:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura

    def volumen(self):
        return (1/3) * math.pi * self.radio**2 * self.altura

    def area(self):
        return math.pi * self.radio * (self.radio + (self.altura**2 + self.radio**2)**(1/2))

if __name__ == "__main__":
    cono = Cono(2, 3)
    print("Volumen: ",cono.volumen())
    print("Area: ",cono.area())
