'''
    Write a program to print the elements of the following list using For Loop:
    [1,4,9,16,25,36,49,64,81,100]
'''
lst = [1,4,9,16,25,36,49,64,81,100]

for val in lst:
    print("Elements is :", val)
print('\n')

'''
    Write a program to search a number x in this tuple using loop:
    (1,4,9,16,25,36,49,64,81,100)
'''

tup = (1,4,9,16,25,36,49,64,16,81,100)
x = int(input("Enter the number you want to search: "))

idx = 0
for search in tup:
    if(search == x):
        print(x," is found at index ",idx)
    idx+=1