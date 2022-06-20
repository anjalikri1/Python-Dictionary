# Q31.. Write a Python program to get the top three items in a shop. Go to
# the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,
# 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

l={'item1': 45.50, 'item2':55, 'item3': 41.30, 'item4':55,'item5': 24}
m1=0
m2=0
m3=0
for i in l:
    for j in l:
        if l[j]>m1:
            m1=l[j] 
            a=j
        if l[j]>m2 and l[j]!=m1:
            m2=l[j] 
            b=j
        if l[j]>m3 and l[j]!=m1 and l[j]!=m2:
            m3=l[j] 
            c=j
print(a,m1)
print(b,m2)
print(c,m3)


            








