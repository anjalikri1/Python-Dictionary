# .Write a Python program to sort a dictionary by key.
d1={"a":23,"b":34,"f":67,"c":20}
l=[]
d={}
for i in d1:
    l.append(i)
    for a in range(len(l)):
        for b in range(len(l)):
            if l[a]<l[b]:
                l[a],l[b]=l[b],l[a]


for x in l:
    for y in l:
        if y==x:
            d.update({x:d1[y]})
print(d)





