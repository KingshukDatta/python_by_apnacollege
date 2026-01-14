#  accessing and modifying class variables
'''class Person:
  name = "JJ"
  
  def changeName(self, name):
    #self.name = name
    Person.name = name
    
person1 = Person()
print(person1.name)  # Output: JJ
print(Person.name)  # Output: JJ'''

'''class Person:
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
print(person1.name)  # Output: Alex'''

# @property decorator
class Student:
  def __init__(self, phy, chem, bio):
    self.phy =phy
    self.chem = chem
    self.bio = bio
    # 1st approach
    '''self.percentage = str((self.phy+ self. chem+ self.bio)/3) + "%"'''
    
  # 2nd approach
  '''def calPercentage(self):
    self.percentage = str((self.phy+ self. chem+ self.bio)/3) + "%"
    return self.percentage'''
  
  # 3rd approach
  @property
  def percentage(self):
    return str((self.phy + self.chem + self.bio) / 3) + "%"
    
stu1 = Student(90, 80, 70)
'''print(stu1.calPercentage())  # Output: 80.0%'''
print(stu1.percentage)  # Output: 80.0%