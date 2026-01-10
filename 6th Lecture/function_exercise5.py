# Write a Function which will take number as input and show the output as "ODD" or "EVEN" string.
def odd_even_string(n):
    if (n%2 == 0):
        print("EVEN")
    elif (n%2 != 0):
        print("ODD")
    else:
        print("Invalid Input")

num = float(input("Enter a number: "))
odd_even_string(num)