# Write a program to Print numbers from 1 to 100.
for i in range(1,101):
    print(i)
print("\n")
# Write a program to Print numbers from 100 to 1.
for j in range(100,0,-1): # Starts from 100, ends to 1 and decreases by -1
    print(j)

# Write a program to Print multiplication table of "n" number.
n = int(input("Enter a number to start: "))

for k in range(1,11):
    m = n * k
    print(n,"x",k,"=",m)