# Write a recursive function to calculate the sum of the first "n" natural numbers.
# 1+2=3+......+n=?
def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n 

s = sum(5)
print(s)