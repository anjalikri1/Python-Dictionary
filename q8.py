# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.
d={"name":"anjali","age":20,"marks":68,"address":"Bihar"}
key=input("enter to check:")
if key in d:
    print("exist")
else:
    print("not exist")
