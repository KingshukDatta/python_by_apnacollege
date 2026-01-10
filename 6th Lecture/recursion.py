#print n to 1 backwards using RECURSION
# RECURSIVE FUNCTION:
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

# RECURSION for factorial n (n!)
def fact(m):
    if(m==0 or m==1):
        return 1
    else:
        return m * fact(m-1)
print(fact(5))