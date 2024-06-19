
#iterative statements => for loop ,while loop
#in python we do not use ++,-- operator in loop

#while loop
'''x=1
while x<=10:
    print(x)
    x=x+1'''

'''n=20
n=int(input("Enter any number"))
i=1
while i<=n:
    1<=20
    #print(i)
    print(i,end=",")
    i=i+1'''

'''n=20
n=int(input("Enter any number : "))
i=1
while i<=n:
    if i<=19:
        print(i,end=",")
    else:
        print(i)
    i=i+1'''

#even numbers
'''i = 2
while i <=100: 
    if(i%2==0):
         print(i,end=",")
    i=i+1'''


#sum of even numbers  
'''num = int(input('Enter a number: '))
sum = 0
i = 0
while i <= num:
    if i % 2 == 0:
        print(i,end="+")
        sum+=i
    i+=1
print("=" ,sum)
'''

#odd numbes
'''i = 2
while i <=100: 
    if(i%2!=0):
         print(i,end=",")
    i=i+1'''

#sum of odd numbers
'''num = int(input('Enter a number: '))
sum = 0
i = 0
while i <= num:
    if i % 2 != 0:
        print(i,end="+")
        sum+=i
    i+=1
print("=" ,sum)
'''

#prime number
'''x=int(input('Enter a number : '))
i=1
count=0
while i<x:
    if x%i==0:
        count=count+1
    i=i+1
if count>1:
    print(x,"is not a prime number")
else:
    print(x," is a prime number")'''



#fibonacci series
# n=int(input("Enter any  number : "))
# a,b,c,i=0,1,0,1
# print(a)
# print(b)



#for loop
#in range function we can pass only itegers we can't pass characters like a,b,c etc

#n=range(2,50,2)
#print(list(n))

#n=range(2,50,-2)#this will not give any output beacause of -2

'''for i in range(2,10,2):
    print(i)
    print("Hello")
    print("Welcome")'''




#sum of even numbers upto 10
# sum = 0
# for i in range(2,10,2):
#     if i<=8:
#         print(i,end=",")
#         sum=sum+i
#     else:
#         print(i,"=",sum)
#     i+=1


#sum of even numbers upto 20
sum = 0
for i in range(2,20,2):
    if i<=18:
        print(i,end=",")
        sum=sum+i
    else:
        print(i,"=",sum)
    i+=1    
    


#sum of numbers upto 10
'''sum = 0
for i in range(1,10):
    if i<=8:
        print(i,end=",")
        sum=sum+i
    else:
        print(i,"=",sum)
    i+=1
'''


#sum of odd numbers upto 20
'''sum = 0
for i in range(1,20,2):
    if i<=18:
        print(i,end=",")
        sum=sum+i
    else:
        print(i,"=",sum)    
    i+=1
'''