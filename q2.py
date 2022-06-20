# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# s="w3resource"
# d={}
# for i in range(len(s)):
#     c=0
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             c+=1
#         d.update({s[i]:c})  
# print(d)   



s="w3resource"
d={}
for i in s:
    if i not in d:
        d[i]=0
    d[i]+=1
print(d)