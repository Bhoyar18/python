
# Data Types :

# 1.Numeric = int,float,complex
"""x=10
y=3+4j
z=4.56
print(type(x))
print(type(y))
print(type(z))

x,y=10,3+4j
print(type(x),type(y))


str="python"
print(type(str))"""

'''x=10
y=20
z=30
x=15
x=40
print(x)'''#this x will print the last value given to x ,due to overriding

#2.sequence = list(collecction of objects) ,tuple,range
'''my_list=[10,20,30,"vaishu",2+3j,20]
print(my_list)
x = ("apple", "banana", "cherry")#tuple
print(type(x))
y = range(6)
print(type(y))'''


#set = set,frozenset
#a={10,20,10,30}#duplicates are not allowed in set
#print(set(a))


"""str='python'
print (str.index('h'))
print(str.index('o',25))"""#it will show value error beacuse our 
# string does not contain more than 5 characters

'''my_list=[10,20,30,40,50,60,'vaishu']
print(my_list.index(40))
print(my_list.index('vaishu'))
print(my_list.index("Vaishu"))'''#it will show value error that is
# Vaishu is not in the list 

#tuple ke objects ko change nhi kar skte hai
#list kr andr ke objects ko change kr skte hai
#static content = the content which can't be change 


#inbuild fuctions of python=print(),type(),id(),input(),max(),min(),len()

"""name=input("Enter your name : ")
age=input("Enter your age : ")
print("My name is :",name)
print("My age is :",age)"""

#type casting = ek data type ko dusre data type me convert karna 



#x="vaishu"
#print(int(x))
'''y=(10,20,30,40,50)
print(list(y))
print(set(y))
z={10,20,30,"vaishu",10,20}
print(type(z))
print(type(set (z)))'''

#String=collection of characters ,duplicates are allowed by string
'''str="vaishuu"
print(str[5])#index
str1="i'love' python"
print(str1)
str2='i "love" python'
print(str2)
str3=''''''i''''love'"python"'''
print(str3)
print(str1+ ' ' +str2)'''#to add(concatenate) two srings

#x='n'
#y='rer rt'#space is also considered as a charcter in python
#z='t'
#print(ord(x))#ord used to find ASCII value
#print(len(y))#len is used to find length of the string


'''my_list=[10,20,30,40,50]
x=my_list.index(30)#index 2 = 30
my_list[x]=50
my_list[1]=50
print(my_list)#this will change the value of 20 and in place of 20 there will be 50
my_list.append(60)#this append is used add any object in last of the list
print(my_list)
my_list.clear
print(my_list)
x=[]
print(type(x))#it will show class list in the output
x=[50,60,70,80,90,]
y=x
x.remove(70)
print(y)
y=x.copy()
print(y)
print(id(x))
print(id(y))
'''

'''new_list1=[80,90]
new_list=[30,40,50,60,70]
new_list.extend(new_list1)
print(new_list)
new_list1.extend(new_list)
print(new_list1)'''

'''list=[20,40,60,80]
list.insert(3,100)
print(list)'''

'''list=[20,40,60,80]
list.pop()#pop will remove last element fron the list
print(list)'''


'''x=list(tuple)
print(type(x))
x[0]=90#to change 90 in place of 10
print(x)
y=tuple(x)
print(type(y))
print(y)'''

# List=['vaishu', 10,20,30,10,20]
# List[0]="maanu"
# print(List)

# List=[ 10,20,30,10,20]
# List.insert(2,90)
# print(List)



#tuple
'''tuple=(12,45,56,78,56,78)
print(len(tuple))#len is used to find length of the tuple
print(id(tuple))#id is used to find the id
print(max(tuple))#max is used to find which is greatest number in the given tuple
print(min(tuple))#min is used for smallest number
print(sum(tuple))#sum is used to find thr sum of numbers in the tuple
print(type(tuple))#type is used to find type of the given tuple
#print(tuple.index(56))#index is used to find index number of the given object in tuple
#print(tuple(-1))
print(tuple.count(78))'''#count is used to count how many times a nimber is repeated in the tuple

# tuple=(122,56,78,34)
# print(len(tuple))
# print(sum(tuple))
# print(min(tuple))
# print(max(tuple))


# Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# print(Tuple.index(3,4))


# x=(1,2,3,4,5,6,7,8,9)
# y=list(x)
# y[5]=89
# print(y)
# x=tuple(y)
# print(x)




#dictionary=in this object is in the form of ("key":"value") pair format,also
#value can be duplicate but key can not be duplicate,object is created ,deleted
#as well as accessed by the help of key
'''x=dict()
x['name']='vaishu'#here [name] is key and [vaishu] is value = object
print(x)
print(x['name'])
x['age']=21
print(x)
x['name']='maanu'#to update the value of name 
print(x)#after printing the value will be changed to maanu
print(len(x))'''
#max and min methods will not work for dictionary

'''my_dict={'name':'vaishu','age':'21','city':'bhopal'}
#my_dict.clear()# this will remove all the object from the my_dict,
#it will delete the full dict
x=my_dict.values()#vaishu,21,bhopal are values
print(x)
print(my_dict.keys())#name , age,city are keys
print(my_dict.items())#this items operation will create a pair of key and values together
print(my_dict.pop('name'))#pop is used to remove particular item that is key of particular pair
print(my_dict)
del my_dict['age']#del is used to delete the full key instead of deleting any value or key 
print(my_dict)
print(my_dict.copy())'''
 

#set=the order of set is not fixed,so indexing and slicing are not allowed  in set,
# also it does not allows duplicates 
#x={10,20,20,30,40,50,60}
#print(x)
#y={10,20,30,40,'vaishu','manu'}
#print(y)
#methods of set = add(koi ek object ko add kr skte),update(ek se jada object add kr skte hai),
#copy,pop(random value ko delete kr deta hai ),remove,discard,clear,
#union,intresection

'''z={23,56,34,56,78,89}
a={23,24,34,78,90,66}
print(z.intersection(a))
print(z.union(a))
z.add(91)
print(z)
z.discard(56)
print(z)
'''
'''set={23,45,'vaishu',67,56,89}
set.discard('vaishu')
print(set)
set.remove(45)
print(set)'''
'''The discard() method removes the specified item from the set. 
This method is different from the remove() method, because the 
remove() method will raise an error if the specified item does not exist, 
and the discard() method will not'''
