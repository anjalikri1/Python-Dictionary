# Q42.
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

d={'Cierra Vega':12,'Alden Cantrell':12,'Kierra Gentry':12,'Pierre Cox':123}
# n=int(input("enter the number :"))
for i in d:
    for j in d:
        if d[i]==d[j]:
            p=(True)
        else:
            p1=(False)
print(p)

        








