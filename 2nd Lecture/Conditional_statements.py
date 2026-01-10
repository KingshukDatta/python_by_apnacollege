# Conditional Statement
# we can use "if" and "elif" statement as many time as we want
# we can use "else" statement only one time.

light = "pink"

if(light == "red"):
    print("Stop") # indentation = proper spacing

elif(light == "green"):
    print("Go")

elif(light == "yellow"):
    print("Wait & look")

else:
    print("Light is broken")
print("End of code")

# Nesting in conditional statement.

age = 34

if(age >= 18):
    if(age >= 80):
        print("Can not drive")
    else:
        print("Can drive.")
else:
    print("Can not drive")