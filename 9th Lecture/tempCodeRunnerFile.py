class Person:
  name = "JJ"
  
  @classmethod
  def changeName(cls, name):
    cls.name = name

person1 = Person()
person1.name = "Alex"
print(Person.name)
print(person1.name)  # Output: Alex
Person.changeName("Sam")
print(Person.name)  # Output: Sam
print(person1.name)  # Output: Alex