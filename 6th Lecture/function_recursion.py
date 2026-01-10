'''
Normal writing code.
a = 5
b = 10

sum = a+b
print(sum)

These can be repeated which is a bad practice.
So we have to reduce repeated parts.
'''

# Creating Function:
# Function Definition
def calc_Sum(a,b): # (*,*,*)- is called parameters 
    sum = a + b
    print(sum)
    return sum

# Calling function:
calc_Sum(2,3) # Calling function
calc_Sum(5,4) # Calling function
calc_Sum(12,10) # Calling function

def print_hello(): # Parameter is empty
    print("hello")
    
print_hello() # argument is empty
print_hello()

output = print_hello()
print(output) # Output is 'NONE' cause, this function does not returns anything.

# Exercise:
# Average of 3 numbers using function:
def avg_out(a,b,c):
    plus = a + b + c
    avg = plus / 3
    return avg

a = int(input("enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print(avg_out(a,b,c))