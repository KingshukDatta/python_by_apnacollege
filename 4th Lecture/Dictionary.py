# Creating Dictionary 
# It's a built-in data-type

info = {
    "key" : "value",
    "name" : "Kingshuk",
    "learning" : "coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.5,
    "subjects" : ["python", "java", "C", "C++"],
    "topics" : ("dict", "set")
}

print(info)
print(type(info)) # Shows the data-type
print("\n")

print(info["age"]) # Shows specific value of the dictionary called "info"
print(info["key"])
print("\n")

info["key"] = "Hello World" # Overwriting Old Value
info["is_adult"] = False # Overwriting Old Value
info["surname"] = "Datta" # Creating new key and value (key:value) pair
print(info) # Getting output
print("\n")

# Nested Dictionary

student = {
    "name": "Kingshuk",
    "subject" : {
        "phy" : 97,
        "chem" : 95
    }
}

print(student) # Printing whole dictionary
print(student["subject"]) # printing dictionary name "subject" nested in "student"
print("\n")

# Dictionary Methods:
# myDict.key() function:
print(len(student))
print(student.keys()) # Returns Key names in List formate. Does not return nested Dictionary Keys.
print(list(student.keys())) # Typecasting to List
print("\n")

# myDict.values() Function:
print(student.values()) # Returns Values of the dictionary.
print(list(student.values())) # Returns values as list.
print("\n")

# myDict.items() Function:
print(student.items()) # Returns key:value pairs like tuples
print(list(student.items())) # Returns key:value pairs as list.
print("\n")

#myDict.item() Function:
print(student.get("name")) # Returns value of the mentioned key
print(list(student.get("name"))) # Returns value  as list.
print("\n")

# Note:
"""
    1. print(student("name"))
    2. print(student.get("name"))
This two works like same. So why the use of .get() method?
    1. print(student("name2")) ---> Output: Error
    2. print(student.get("name")) ---> Output: None
Because in no 1 there is no key named "name2". SO the output will be Error.
On the other hand in no 2, though there is no key named "name2", the output will be "None".

If we encounter error, the code will not run fully. It will stop executing at the error part.
But if we use method, The code will run fully.
"""

##myDict.update(newDict) Function:
new_dict = {
    "city" : "dhaka",
    "age" : 16
}
student.update(new_dict) # Adds new key:value to a dictionary
print(student) # Output
# Note:
'''
We can also write it as:
student.update({"city" : "dhaka","age" : 16})
The result will be same.
'''