# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are square of keys.
n=int(input("enter the number"))
d={}
for i in range(1,n+1):
    d.update({i:i**2})
print(d)
