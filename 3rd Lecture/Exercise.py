# Write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

# Taking Inputs
mov1 = input("Enter the 1st Movie: ") 
mov2 = input("Enter the 2nd movie: ")
mov3 = input("ENter the 3rd movie: ")

#Storing inputs
list_movie = [mov1, mov2, mov3]

#Printing output of the stored list and data type of the list

print("The movies are : ",list_movie)
print(type(list_movie))

'''There is another method using append():

1. create a empty list:
    list_movie = []

2. Taking input and storing: "using append() method"
    mov1 = input()
    list_movie.append(mov1)
    mov2 = input()
    list_movie.append(mov2)
    mov3 = input()
    list_movie.append(mov3)

3. Print the list for confirmation:
    print(list_movie)  
'''
# Note: We can also use append() method directly by list_movie.append(input("Enter 1st movie"))

# Write a program to check if a list contains a palindrome of elements.

list1 = [1,2,3,2,1]
list2 = [3,4,5,7,3]


cp_list1 = list1.copy()
cp_list1.reverse()

if(cp_list1 == list1):
    print("This List 1 is Palindrom")
else:
    print("This List 1 is not Palindrom")

cp_list2 = list2.copy()
cp_list2.reverse()

if(cp_list2 == list2):
    print("This List 2 is Palindrom")
else:
    print("This List 2 is not Palindrom")

# Write a  program to count the number of students with the "A" grade 
# in this tuple ("C", "D" , "A", "A", "B", "B", "A")

grade_tup = ("C", "D" , "A", "A", "B", "B", "A")

print("The Number of Grade A is ", grade_tup.count("A"))

# Write a Program to store ("C", "D" , "A", "A", "B", "B", "A") tuples value to a 
# list and sort them from A to D

store_list = []

store_list.append(input("Enter 1st Grade: "))
store_list.append(input("Enter 2nd Grade: "))
store_list.append(input("Enter 3rd Grade: "))
store_list.append(input("Enter 4th Grade: "))
store_list.append(input("Enter 5th Grade: "))
store_list.append(input("Enter 6th Grade: "))
store_list.append(input("Enter 7th Grade: "))

store_list.sort()
print("The sorted list is", store_list )