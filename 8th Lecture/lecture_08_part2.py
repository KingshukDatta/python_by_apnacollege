class Student:
  def __init__(self, name):
    self.name = name
s1 = Student("Karan")

# Deleting the object
# del can also be used to delete an object's attributes.
'''del s1'''
print(s1.name)  # This will raise an error since s1 has been deleted.
# Output: NameError: name 's1' is not defined

class Account:
  def __init__(self, acc_no, acc_pass):
    self.acc_no = acc_no
    # normally we write: self.acc_pass = acc_pass
    # but to make it private, we use double underscore
    self.__acc_pass = acc_pass
    
acc1 = Account("12345", "abcde")
print(acc1.acc_no)  # Output: 12345
# normally we would access acc_pass like this:
# print(acc1.acc_pass) for the code: self.acc_pass = acc_pass
# but since it's private, we cannot access it directly.
print(acc1.__acc_pass)  # This will raise an error since __acc_pass is private.