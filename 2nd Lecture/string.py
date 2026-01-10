# Type of ways to use a string.
a = 'Hello I am Kingshuk' # Here we can't use ' in the middle of the string.
print(a)

b = "I am going to school" # Here we can't use " in the middle of the string.
print(b)

c = """I want to go there""" # in this we can use ' and " in the middle of the string
print(c)

# Basic Operation
# Concatenation

x = a + b

print(x)

# Length function. len()
print(len(x)) # shows the length of string in numbers.

# Selecting a character from a string

k = "Kingshuk"
ch = k[0]
print(ch)

print(k[1:4]) # slicing with positive index
print(k[-1:-3]) # slicing with negative index

# String function

str = "i am studying python from ApnaCollege"

print(str.endswith("ege")) # use str.endswith() function

print(str.capitalize()) # use str.capatilize() function

print(str.replace("o","a")) # use str.replace("old","new")
print(str.replace("python","Javascript")) # use str.replace("old_sub str","new_sub str")

print(str.find("o")) # # use str.find("word")
print(str.find("from")) # # use str.find("word")
print(str.find("q")) # # use str.find("word")

print(str.count("from")) # # use str.count("word")
print(str.count("o")) # # use str.count("word")