#!/usr/bin/env python

# create object definition
class Vehicle:
  """
    This is a vehicle.
  """

  # attributes
  # [ if using an __init__ method: don't list
  #   attributes here because it is redundant ]
  #color = None
  #make = None
  #model = None
  #name = ''
  #year = None

  # methods
  def __init__(
    self,
    color=None,
    make=None,
    model=None,
    name='',
    year=None
  ):
    self.color = color
    self.make = make
    self.model = model
    self.name = name
    self.year = year

  def __str__(self):
    return self.name

  def engine_start(self):
    """
      Start the vehicle's engine.
    """
    print('%s: starting engine' % (self))

  def engine_stop(self):
    """
      Stop the vehicle's engine.
    """
    print('%s: stopping engine' % (self))

  def honk_horn(self):
    """
      Honk the vehicle's horn.
    """
    print('%s says, "HONK!"' % (self))


class Car(Vehicle):

  def __init__(
    self,
    wheels=None,
    *args,
    **kwargs,
  ):
    """
      This is a car. It inherits from Vehicle.

      Instantiate it by listing first Car
      attributes, then Vehicle attributes.
    """
    super().__init__(*args, **kwargs)
    self.wheels = wheels

  # override a method
  def engine_start(self):
    print('vroom')


"""
  This was the in-line testing we did.
"""
#car = Car()
#print(car.wheels)
#print(car.color)
#car.engine_start()
#
## apply our class (create some objects)
#vehicle_1 = Vehicle(
#  'silver',
#  'Toyota',
#  'Sienna',
#  'Matt',
#  2004,
#)
#
#car_1 = Car(
#  100,
#  'silver',
#  'Toyota',
#  'Sienna',
#  'Matt',
#  2004,
#)
#print(car_1.year)
#
#car_2 = Car(color='blue')
#print(car_2.color)
#
#vehicle_1.engine_start()
#print(vehicle_1.year, vehicle_1.color)
#vehicle_1.honk_horn()
#vehicle_1.engine_stop()
#
#vehicle_2 = Vehicle(year=2020)
#print(vehicle_2.year)
