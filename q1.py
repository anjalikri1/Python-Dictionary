# Q1.Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400,'e':500}
d={}
for i in d1:
    if i in d2:
        d[i]=d1[i]+d2[i]
    else:
        d[i]=d1[i]
for j in d2:
    if j in d1:
        d[j]=d1[j]+d2[j]
    else:
        d[j]=d2[j]
print(d)




