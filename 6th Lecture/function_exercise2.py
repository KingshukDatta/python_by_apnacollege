# Write a Function to print the elements of a list in a single line.( List is parameter)
# Defining Function:
def print_list(list):
    for item in list:
        print(item, end = " ")
# Defining list
p = ["hello","!@#$"]
q = ["Hell","Heven",1,3,5,7]
print_list(p) # Calling function
print_list(q) # Calling function