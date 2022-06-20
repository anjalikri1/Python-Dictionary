# city_population = {"NewYorkCity":8550405,"LosAngeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print()
# print(city_population)
# print()
# print(type(city_population))


# Dict = {'ball' : 'green','Ball': 'red'}
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])


# student=dict(name= "Ravina",age= 20)
# print(student)


# my_dict = {1: 'apple', 2: 'ball'}
# print(my_dict)

# my_dict = {'name': 'John',1: [2, 4, 3]}
# print(my_dict)


# Dic= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To', 'C' : 'DHARAMSALA'}}
# print(Dic)


# person={'name':'jack','age':20,'gender':'male',4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# person={'name':'jack','age':20,'gender':'male',4:{'organisation':'navgurukul','place':'dharamsala'}}
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)



# dic= {'Name': 'RAM', 'Age': 17,}
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)



# dic= {'Name': 'RAM',
#    'Age': 17,}
# dic['student']={'id':22, 'place':'dharamsala'}
# print(dic)

# car ={"brand":  "ford","model":  "mustang","year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")


# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# details={'Name': 'RAM','Age': 17, 'student': {'id': 22,'place': 'dharamsala'}} 
# details['student']['id']=35
# print(details)


# classes ={"room1":  "6th","room2":  "7th","room3":  "8th"}
# mydict=classes.copy()
# print(mydict)


# CAR_DETAILS={"brand": "Ford","model": "jason","year": 1964}
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)


# person={'name':'jack','id':22,'place':'dharamsala'}
# person.popitem()
# print(person)


# person={'name':'jack','id':22,'place':'dharamsala'}
# del person['place']
# print(person)


# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   print(state)


# states_capitals = {'Gujarat' : 'Gandhinagar','Maharashtra' : 'Mumbai','Rajasthan' : 'Jaipur','Bihar' : 'Patna'}
# for state in states_capitals:
#     print(states_capitals[state])

# details ={"name":  "Bijender","age":  17,"class":  "10th"}
# for x in details.values():
#     print(x)




# movie ={"name":  "Puli",
# "hero":  "Vijay",
# "rating":  7.5}
# for x,y in movie.items():
#     print(x,y)


# meal ={"monday":  "Chole chawal","sunday":  "Fried rice","wednesday":  "dosa"}
# print(len(meal))


# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# # print(dic1)
# dic1.update(dic3)
# print(dic1)



# str=input("enter the string :")
# dict1={"name":"Raju", "marks":56}
# if str=="name" or str=="marks":
#     print("exists")
# else:
#     print("not exists")


# d= {'data1':100,'data2': -54,'data3': 247}
# l=d["data1"]+d["data2"]+d["data3"]
# print(l)


# Dic= {1: 'NAVGURUKUL',2: 'IN',3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del Dic[3]['B']
# print(Dic)





# Create a dictionary from 2 lists, where the elements of 1st list are the keys and the elements of the 2nd list are the corresponding values.
# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# d={}
# for i in range(len(list1)):
#     d[list1[i]]=list2[i]
# print(d)


# Write a program to remove duplicate keys.
# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# d={}
# for i in dic:
#     if i not in d:
#         d.update({i:dic[i]})
# print(d)


# Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
#op=['2', '7', '9', '5', '1']
# l=[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# list=[]
# for i in l:
#     for j in i:
#         if i[j] not in list:
#             list.append(i[j])
# print(list)



# Take input of name and marks of 10 students and store to a dictionary.
# d={}
# for i in range(10):
#     name=input('enter the name :')
#     marks=int(input("enter the marks :"))
#     d.update({name:marks})
# print(d)


#????
# q_9.)Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
#op={'M':1,'I':4,'S':4,'P':2}
# s="MISSISSIPPI"
# d={}
# c=0
# for i in range(len(s)):
#     for j in range(len(s)):
#         if s[i]==s[j]:
#             c+=1

















































