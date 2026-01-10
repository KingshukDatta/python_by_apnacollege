# Write a function to convert USD to TAKA
# Defining Function:
def convert_currency(u):
    t = 110 * u # USD --> Taka
    print("The Value after converting USD to TAKA is ",t)
    return t

u = float(input("Enter the USD amount to start conversion:"))
convert_currency(u) # Calling Function