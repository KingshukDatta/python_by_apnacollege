# Grading student based on marks:-
# marks >= 90, grade "A"
# 90 > marks >= 80, grade = "B"
# 80 > marks >= 70, grade = "C"
# 70 > marks, grade = "D"

marks = float(input("Enter a student's marks: "))

if(90 <= marks and 100 > marks): # 100 > marks >= 90, grade "A" .
    print("Grade = 'A'\n")

elif(90 > marks and marks >=80): # 90 > marks >= 80, grade = "B" .
    print("Grade ='B'\n")
    
elif(80 > marks and marks >=70): # 80 > marks >= 70, grade = "C" .
    print("Grade = 'C'\n")

elif(70 > marks): # 70 > marks, grade = "D" .
    print("grade = 'D'\n")
    
else: # if there is an invalid number in input. 
    print("Grade not found.\nPlease input valid number")

# Write a program to check if a number entered by the user is odd or even

num = float(input("Enter a number: "))

if(num % 2 == 0):
    print("The number is Even\n")

else:
    print("The number is Odd\n")

# Write a program to find the greatest of 3 numbers entered by the user.

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd Number: "))

if(num1 > num2 and num1 > num3):
    print(num1," is Greater\n")
elif(num2 > num1 and num2 > num3):
    print(num2," is Greater\n")
elif(num3 > num1 and num3 > num2):
    print(num3," is Greater\n")
else:
    if(num1 == num2 == num3):
        print("\nAll the numbers are of same value")
    else:
        print("Invalid Input")


# Write a program to check if a number is a multiple of & or not.

a = float(input("\nEnter a Number: "))

if(a % 7 == 0):
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")