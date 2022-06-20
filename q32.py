# Q32.Write a Python program to get the key, value and item in a dictionary.
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# Sample Output:

c=0
print("key","value","count")
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for i in d:
    c+=1
# print("key","value","count")
    print(i," ",d[i]," ",c)

