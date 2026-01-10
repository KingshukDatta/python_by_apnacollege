class Student:
  # "self" is mandatory in method definitions inside a class. For every method in a class,
  # we have to pass "self" as the first parameter.
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    
  @staticmethod # decorator to define static method.
  def college():
    print("Hello")

  def welcome(self):
    print("Welcome Student", self.name)
  
  def get_marks(self):
    return self.marks
  
s1 = Student("Karan", 90)
s1.welcome()  # Output: Welcome Student Karan
print(s1.get_marks())  # Output: 90

# Abstraction and Encapsulation
# Abstraction: Hiding the implementation details of a class and only showing the essential features.
class Car:
  def __init__(self):
    self.acc = False
    self.brk = False
    self.clutch = False
  
  def start(self):
    self.acc = True
    self.acc =  True
    print("Car started")
    
car1 = Car()
car1.start()  # Output: Car started