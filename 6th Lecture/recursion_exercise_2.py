# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.
def print_list(list, idx=0):
    if (idx == len(list)): # Base case
        return
    print(list[idx]) # Output
    print_list(list, idx+1) # calling again

fruits = ["mango","lichi","apple","banana"]
print_list(fruits)