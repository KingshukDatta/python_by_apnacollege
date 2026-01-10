'''Create student class that takes name and marks of 3  subjects as arguments in construstor.
then create a method to print average.'''

'''# creating class.
class Student:
  #initial method/ constructor
  def __init__(self, name, marks1, marks2, marks3):
    self.name = name
    self.marks1 = marks1
    self.marks2 = marks2
    self.marks3 = marks3
  
  # method to calculate average
  def average(self):
    avg = (self.marks1 + self.marks2 + self.marks3)/3
    return avg

# taking input from the user.
m1 = int(input("Enter 1st mark for a subject: "))
m2 = int(input('Enter 2nd marks for a subject: '))
m3 = int(input("Enter 3rd marks for a subject: "))

# Creating object of the class Student.
s1 = Student("Karan", m1, m2, m3)
# calling average method and printing the average.
print(f"The average of the student {s1.name} is {s1.average()}.")'''


# Alternate way..
# creating class.
'''class Student_info:
  # initial method/ constructor
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    
  # method to calculate average
  def average(self):
    sum = 0
    for i in self.marks:
      sum += i
    avg = sum / len(self.marks)
    return avg

# taking input from the user in a list.
marks = [] # empty list
i = int(input("Enter number of subjects: ")) # number of subjects

# loop to take marks as input
for val in range(i):
  m = int(input(f"Enter marks for subject no{val+1}: "))
  marks.append(m)
  
# Creating object of the class Student_info.
s1 = Student_info("Kingshuk", marks)
print(f"The average of the student {s1.name} is {s1.average()}")'''

'''Create Account class with 2 attributes- balance and account no.
Create methods for debit, credit & printing the balance'''

class Account:
  def __init__(self, bal, acc_no):
    self.balance = bal
    self.account_no = acc_no
  
  # Debit method
  def debit(self, amount):
    self.balance -= amount
    print(f"Debited {amount}. New balance is {self.balance}")

  # Credit method
  def credit(self, amount):
    self.balance += amount
    print(f"Credited {amount}. New balance is {self.balance}")

  # Print balance method
  def get_balance(self):
    return self.balance

account1 = Account(10000, 12345)
account1.debit(2000)  # Debited 2000. New balance is 8000
account1.credit(5000)  # Credited 5000. New balance is 13000
print(f"Current balance is {account1.get_balance()}")  # Current balance is 13000