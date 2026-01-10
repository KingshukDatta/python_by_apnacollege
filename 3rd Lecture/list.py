# List are accessible and Changeable

marks = [45, 95.3, 100, 55.67]
student = ["kingshuk", 85, "Dhaka"]

print(student) # access
print(type(student))
print(len(student))

print(marks)
print(type(marks))
print(len(marks))  

student[0] = "King" # change
print(student)
print("\n")

# List Slicing

print(marks[1:4])
print(marks[ :4])
print(marks[0:])

# List Method

list = [2,1,3,1]

list.append(4) # Adding  element in past position of the list
print(list)

list.sort() # Ascending Order
print(list)

list.sort(reverse=True) # Descending Order
print(list)

list.reverse() # Reverse the list
print(list)

list.insert(1,5) # Specific Insertion of an element
print(list)

list.remove(1) # Removes '1' when first occures
print(list)

list.pop(3) # Removes specific index
print(list)