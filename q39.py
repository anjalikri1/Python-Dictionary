# Q39.Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d1={}
for i in d:
    if d[i]>170:
        d1.update({i:d[i]})
print(d1)


