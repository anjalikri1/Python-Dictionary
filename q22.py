# Q22. Write a Python program to create and display all combinations of letters, selecting each
# letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd

d={'1':['a','b'], '2':['c','d']}
a=d["1"]
b=d["2"]
for i in a:
    for j in b:
        print(i+j)

