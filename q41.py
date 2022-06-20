# Q41.Write a Python program to filter the height and width of students, which are stored in a
# dictionary.
# Original Dictionary:
# {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,
# 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}



d={'Cierra Vega': (6.2,70), 'Alden Cantrell': (7, 75), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8,66)}
d1={}
for i in d:
    t=d[i]
    h=d[i][0]
    w=d[i][1]
    if h>=6 and w>=70:
        d1.update({i:(h,w)})
print(d1)














# t=(12,34,456)
# for i in range(len(t)):
#     print(t[i])


