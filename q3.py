# Q3. Write a Python script to generate and print a dictionary that contains a number (between 1
# and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.

# n=int(input("enter the number"))
# d={}
# for i in range(1,n+1):
#     d.update({i:i**2})
# print(d)


# n=int(input("enter the number"))
# d={}
# for i in range(1,n+1):
#     d.update({i:i**2})
# print(d)



d=dict()
for i in range(1,6):
    d[i]=i*i
print(d)