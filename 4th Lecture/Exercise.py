'''
    store following word meanings in python dictionary:
    table : "a piece of furniture", "list of facts & figures"
    cat : "a small animal"
'''
# Creating Dictionary:
meaning = {
    "table" : ["a piece of furniture", "list of facts & Figures"],
    "cat" : "a small animal"
}

# Output:
print("The list of meanings are : \n", meaning)

'''
    You are given a list of subjects for students. Assume one classroom 
    is required for 1 subject. How many classrooms are needed by all students.
    
    "python", "java", "C++", "python", "javascript", "java", "python", "java",
    "C++", "C"
'''
# Creating set:
classroom = {"python", "java", "C++", "python", "javascript", "java", "python", "java","C++", "C"}

# Output:
print("We need ", len(classroom), "classrooms")

'''
    Write a program to enter marks of 3 subjects from the user and store them in a dictionary.
    Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
'''
# Creating Dictionary:
grade = {}

# Taking Input from user:
grade[input("Enter 1st subject's Name: ")] = input("Enter 1st subject's number: ")
grade[input("Enter 2nd subject's Name: ")] = input("Enter 2nd subject's number: ")
grade[input("Enter 3rd subject's Name: ")] = input("Enter 3rd subject's number: ")

# Output:
print("The Grades of the 3 subject are: \n",grade)

'''
    Figure out a way to store 9 & 9.0 as separate values in the set.
    Hint: You can take help of built-in data types
'''

# Create set:=
values = {("int", 9),("float", 9.0)}

# Output:
print("The values set is :",values)