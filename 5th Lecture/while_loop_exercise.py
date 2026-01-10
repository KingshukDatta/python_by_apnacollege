# Print number from 1 to 100:
print("print numbers from 1 to 100:") 
num = 1 # Initial value
while num <= 100: # condition
    print(num)
    num+=1
print("\n")

# print numbers from 100 to 1:
print("print numbers from 5 to 1:") 
num1 = 100 # Initial value
while num1 >=1: # condition
    print(num1)
    num1-=1
print("\n")

# Print the multiplication table of a number n:
n = int(input("Enter the number for the multiplication table: ")) # Taking Input
j = int(input("Enter the limit of the multiplication table: ")) # Taking Input

i = 1 # Initial value

while i<=j: # condition
    print(n ,"x",i,"=",(n*i)) # output: n x i = (n*i) formate.
    i+=1
print("\n")

# print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]

print("The list elements are: ")

i = 0 # Initial value. Index = 0

while i <= (len(list)-1): # condition will run from index 0-9 and print
    print(list[i]) # output
    i+=1 # update value
print("\n")

# Search for a number "x" in this tuple using loop:
#(1,4,9,1625,36,49,64,81,100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x= int(input("enter the number for search: ")) # Input the number for search

i = 0 # Initial value. Index = 0

while i < len(nums): # Condition
    if (nums[i] == x): # if statement
        print("Found the number in", i)
        break # breaks the loop.
    else: # else statement
        print("finding..")
    i+=1