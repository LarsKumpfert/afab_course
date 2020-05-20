class Car():

    def __init__(self, colour='green', brand = 'porsche'):
        self.colour = colour
        self.brand = brand

    def repaint(self, new_colour):
        self.colour = new_colour

my_car = Car (colour='yellow', brand='bmw')
my_second_car = Car (colour='blue', brand='mercedes')

print(my_car.colour)
print(my_second_car.colour)

my_car.repaint('black')

print(my_car.colour)