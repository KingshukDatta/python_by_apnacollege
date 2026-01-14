# super() method
class Car:
  def __init__(self, type):
    self.type = type
    
  @staticmethod
  def start():
    print("Car started...")
  
  @staticmethod
  def stop():
    print("Car stopped.")
  

class ToyotaCar(Car):
  def __init__(self, name, type):
    super().__init__(type)
    self.name = name
    super().start()

car1 = ToyotaCar("Prius", "Hybrid")
# print(car1.type)  # This will raise an AttributeError because 'type' is not initialized in ToyotaCar
print(car1.name)  # Output: Prius
print(car1.type)  # Output: Hybrid