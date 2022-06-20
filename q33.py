# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
# 'rolld_id':2},
# 'Puja':{'class':'V',
# 'roll_id':3}}
# Sample Output:
# Aex
# class : V
# rolld_id : 2


d={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for i in d:
    print(i)
    d1=d[i]
    for j in d1:
        print(j,":",d1[j])
