# Arithematic Operators 
a = 6
b = 2

sum = a + b # sum of two numbers
diff = a - b # Difference of 2 numbers
mult = a * b # Multiplication of 2 numbers
div = a / b # Division of 2 numbers 
mod = a % b # remainder of 2 numbers
power = a ** b # power of a ^ b

print(sum)
print("The sum is",sum)

print(diff)
print("The difference is",diff)

print(mult)
print("The multiplication is",mult)

print(div)
print("The division is",div)

print(mod)
print("The mod / remainder is",mod)

print(power)
print("The a to the power b is",power)

# Relational / Comparison operator

x = 50
y = 20

print("Is the two number is equal? :", x == y) #False
print("Is the two number is not equal? :", x != y) #True

print("Is x greater than y ? :", x > y) #True
print("Is x lesser than y ? :", x < y) #False

print("Is x greater equal to y ? :", x >= y) #True
print("Is x lesser equal to y ? :", x <= y) #False

# Assignment Operators

num = 10
num = num + 10 # num is 10 so 10 + 10 = 20
print("The num is :", num)

num1 = 20
num1+= 20 # num1 = num1 +20
print("The num1 is :", num1)

num-=10 #num = num - 10
print("The num diff is :", num)

num*=10 #num = num * 10
print("The num mult is :", num)

num/=10 #num = num / 10
print("The num div is :", num)

num%=10 #num = num % 10
print("The num remainder is :", num)

num = 10
num**=10 # num = num^10
print("The num power is :", num)

#Logical Operators
# Works on boolean value

print("Not operator where False is_",not False)
print("Not operator where True is_",not True)

a = 50
b = 20

print(not(a>b)) #True is going to be false

val1 = 1
val2 = 2

print("And Result is ", val1 and val2)

val1 = True
val2 = False

print("Or Result is ", val1 or val2)

print("A Or B Result is ", (a==b) or (a>b))
