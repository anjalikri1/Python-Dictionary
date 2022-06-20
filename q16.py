# Q16.Write a Python program to map two lists into a dictionary.
l1=[2,3,1,5]
l2=["anjali","raj","priya","mohan"]
d={}
for i in range(len(l2)):
    d.update({l1[i]:l2[i]})
print(d)


