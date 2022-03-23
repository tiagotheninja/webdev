class Car():
    def __init__(self, tag, color, gas):
        self.tag = tag
        self.color = color
        self.gas = gas
        self.odometer = 0

    def add_km_odometer(self, distance):
        self.odometer += distance

    def paint_car(self, new_color):
        self.color = new_color

    def talk(self):
        print("Eu sou o " + self.name + " e faço " + self.sound)


car_list = []
#car_list.append(Car("11-AA-11", "Branco", 40.0))
#car_list.append(Car("99-ZA-11", "Branco", 11.0))

while True:
    tag = input("Introduza a matricula do novo carro")
    color = input("Introduza a cor do novo carro")
    volume = input("Introduza a volume de combustivel do novo carro")
    car_list.append(Car(tag, color, volume))

# PROGRAMA POO
# CLASS ANIMAL
# nome, especie, som
# function TALK - > print som animal