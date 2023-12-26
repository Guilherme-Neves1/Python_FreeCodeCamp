# CLASSES

class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def moves(self):
    print('Moves along..')

  def get_make_model(self):
    print(f"\nI'm a {self.make} {self.model}.")

my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
  def moves(self):
    print('Flies along..')

class Truck(Vehicle):
  def moves(self):
    print('Rumbles along..')

class GolfCart(Vehicle):
  pass

cessna = Airplane('Cessna', 'Skyhawk')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()


