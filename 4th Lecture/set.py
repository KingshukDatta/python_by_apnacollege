# Set:
# It is just like in math where every value must be unique and Immutable.
# Duplicated values are ignored and just prints it once. But does not show error.
 
collection = {1, 2, 3, 4, "hello", "world",5 ,6}

print("Collection = ",collection) # Outputs the set
print(type(collection)) # Shows the Data-type
print("Length is ",len(collection)) # Prints the total number of items or elements
print("\n")

# Creating empty sets:
sets = set() # Syntax of empty:- set set_name = set()
print("Empty Set = ",sets)
print(type(sets))
print("\n")

# Methods of Set:
# setName.add(el) Function:
sets.add(1) # Number adding
sets.add(2) # Number adding
sets.add(2) # Number adding
sets.add(3) # Number adding
sets.add(4) # Number adding
sets.add(5) # Number adding
sets.add(6) # Number adding
sets.add("Kingshuk") # String adding
sets.add("Utshuk") # String adding
sets.add("Hello") # String adding
sets.add((1,2,3,4)) # tuple adding
sets.add((7,8,9,10)) # tuple adding

print("setName.add(el) Function: ")
print("Set = ",sets)
print("\n")

# setName.remove(el) Function:
sets.remove(2) # Number removing
sets.remove(5) # Number removing
sets.remove("Hello") # String removing
sets.remove((7,8,9,10)) # tuple removing

print("setName.remove(el) Function: ")
print("Set = ",sets)
print("\n")

# setName.clear() Function:
collection.clear() # Clearing set

print("Collection = ",collection) # Outputs the set
print(type(collection)) # Shows the Data-type
print("Length is ",len(collection)) # Prints the total number of items or elements
print("\n")

# setName.pop() Function:
collection = {"hello", "hi", "bye", "b", "a"}

print("Random Element = ",collection.pop()) # Random value will be shown from set
print("\n")

# setName.union() Function:
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print("The 1st set: ", set1,"\n", "The 2nd set: ", set2)
print("The Union of the sets is :-", set1.union(set2))
print("\n")

# setName.intersection() Function:
'''set1 = {1, 2, 3}
set2 = {2, 3, 4}'''

print("The 1st set: ", set1,"\n","The 2nd set: ", set2)
print("The Union of the sets is :-", set1.intersection(set2))
print("\n")