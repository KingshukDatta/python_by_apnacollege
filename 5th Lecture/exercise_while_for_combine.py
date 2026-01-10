# Write a program to find the sum of first n natural numbers.(While Loop)
'''
n = int(input("Enter a number to continue: "))

i = 0
j= 0
while i <=n:  # for i in range(1,n+1): sum+=i
    j= j+i
    i+=1
print("The sum of the inputted number",n,"is",j)

'''

# Write a program to find factorial of first n numbers.(For Loop)
m = int(input("Enter a number to start factorial: "))
fact= 1
'''
i =1
while i<=n:
    fact *=i
    i+=1
'''
for k in range(1,m+1):
    fact *= k
    
print("The factorial is", fact)