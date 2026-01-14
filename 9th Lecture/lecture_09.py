'''class Person:
  __name = "Anonymous" # Conceptual private attribute
  
# we can also make method conceptually private by using double underscores.
  def __hello(self, name):
    print("Hello!")
  def welcome(self):
    self.__hello("Guest")
p1 = Person()
#print(p1.__name)  # This will raise an AttributeError because __name is private
#print(p1.__hello())  # This will also raise an AttributeError because __hello is private
print(p1.welcome())  # This will work and print "Hello!"'''

'''# Static Methods and Inheritance Example
# Single Inheritance ( 1 parent class and 1 child class)
class Car:
  color = "Black"
  @staticmethod
  def start():
    print("Car started...")
  
  @staticmethod
  def stop():
    print("Car stopped.")
  

class ToyotaCar(Car):
  def __init__(self, name):
    self.name = name

car1 = ToyotaCar("Corolla")
car2 = ToyotaCar("Camry")

print(car1.name)  # Output: Corolla
print(car2.name)  # Output: Camry
print(car1.start())  # Output: Car started...
print(car2.stop())   # Output: Car stopped.
print(car1.color)  # Output: Black
print(car2.color)  # Output: Black'''

'''# Multi-Level Inheritance Example
class Car:
  @staticmethod
  def start():
    print("Car started...")
  
  @staticmethod
  def stop():
    print("Car stopped.")

class ToyotaCar(Car):
  def __init__(self, brand):
    self.brand = brand

class Fortuner(ToyotaCar):
  def __init__(self, type):
    self.type = type
    
car1 = Fortuner("diesel")
car1.start()  # Output: Car started...  '''

# Multiple Inheritance Example
class A:
  varA= "Welcome to class A"

class B:
  varB= "Welcome to class B"

class C(A, B):
  varC = "Welcome to class C"

c1 = C()
print(c1.varA)  # Output: Welcome to class A
print(c1.varB)  # Output: Welcome to class B
print(c1.varC)  # Output: Welcome to class C