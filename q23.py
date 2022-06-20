# Q23.Write a Python program to find the highest 3 values of corresponding keys in a
# dictionary.
d={"a":100,"d":500,"s":300,"p":200}
l=[]
for a in d:
    l.append(d[a])
print(l)
m1=0
m2=0
m3=0
for i in l:
    if i>m1:
        m1=i
    if i>m2 and i!=m1:
        m2=i
    if i>m3 and i!=m1 and  i!=m2:
        m3=i
print(m1,m2,m3)
