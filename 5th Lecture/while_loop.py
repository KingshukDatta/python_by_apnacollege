# While Loop:
count = 1
while count <= 5:
    print("Hello World", count)
    count+=1 #count = count + 1 . Just like i++ / i = i+1 / i+=1
print(count) # After looping and updating value count = 6
print("\n")

# print numbers from 1 to 5
print("print numbers from 1 to 5: \n") 
num = 1
while num <= 5:
    print(num)
    num+=1
print("\n")

# print numbers from 5 to 1
print("print numbers from 5 to 1: \n") 
num1 = 5
while num1 >=1:
    print(num1)
    num1-=1
print("\n")

# Break keyword:
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
print("\n")

# Continue keyword: printing odd number from 1 to 10
inn = 0
while inn<=5:
    if(inn%2 == 0):
        inn+=1
        continue #skip
    print(inn)
    inn+=1