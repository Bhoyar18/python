

#control flow statements=> 
#Conditional statements = 1.if(this condition can be used without else in python individually) 
# 2.if-else  3.if-elif-else
#Transfer statements = 1.continue 2.break 3.pass
#Iterative statements = (string,list,tuple,dict)1.for loop 2.while loop
#loop kitni baar chlna agr ye pta h to for loop use hoga and agr ni pta 
#ki loop kitni baar chlna hai to while loop use hoga

#conditional

x=input("Enter your age:")#input function by default string data type return krta hai
print(type(x))
y=int(input("Enter your age"))
#we can use complex,float intead of int to get the correct type in return
print(type(y))

#if 
x=int(input("Enter your age here : "))
if x>=21:
    print("You can vote")
    print("Welcome to first python program")
    print("Thankyou for visiting")
 
y=int(input("Enter your age here : "))
if y>=60:
    print("Goto counter 1")
if y<21:
    print("You can not vote")

#if-else
a=int(input("Enter your age : "))
if a>21:
    print("You can vote")
else:
    print("You can't vote")

#if-elif-else
b=int(input("Enter your age : "))
if b>=60:
    print("Goto counter 1")
elif b>=40:
    print("Goto counter 2")
elif b>=20:
    print("Goto counter 3")
else:
    print("You are not allowed")



 
    
