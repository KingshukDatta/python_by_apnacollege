'''# creating class
class Student:
  def __init__(self, fullname):
    self.name = fullname
    print("adding new student in database.")

#creating object(instance)
s1 = Student("Kingshuk")
print(s1.name)'''

'''print(s1.name)  # Output: Kingshuk'''

'''class Car:
  color = "blue"
  brand = "BMW"
  
car1 = Car()
print(car1.color)  # Output: blue
print(car1.brand)  # Output: BMW'''


# creating class
class Student:
  # class attribute
  college_name = "ABC College"
  name = "Anonymous"
  
  # default constructor: If we do not define any constructor, Python provides a default constructor
  def __init__(self):
    pass
  
  # parameterized constructor: If we define a constructor with parameters, it is called a parameterized constructor
  def __init__(self, fullname, marks):
    # Object attributes
    self.name = fullname
    self.marks = marks
    print("adding new student in database.")
# object attribute > class attribute

#creating object(instance)
s1 = Student("Kingshuk", 95)
print(s1.name)
print(s1.marks)
print(s1.name, s1.marks)
print(s1.college_name)

# Accessing class attribute using class name
# syntax : ClassName.attribute_name
print(Student.college_name)# Output: ABC College
