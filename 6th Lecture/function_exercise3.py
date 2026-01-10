# Write a function to find the factorial of N. (N is the parameter)
# Defining function:
def factorial_n(n):
    fact = 1
    for el in range(1,n+1):
        fact *= el
    print(fact)

n = int(input("Enter a number for factorial: "))

factorial_n(n) # Calling function