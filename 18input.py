# by default input gives string format
x=int(input("Enter 1st number"))
# print(type(x))
# a=int(x)
y=int(input("Enter 2nd number"))
# b=int(y)
z=x+y
print(z)

# there is no char data type in python
# Method-1
ch=input('enter a char')
print(ch[0])
# Method-2
ch=input('enter a char')[0]
print(ch)

#input experrision
res=eval(input('enter an expr'))
print(res)

#to implement by comand prompt
import sys
x=int(sys.arvg[1])
y=int(sys.arvg[2])
z=x+y
print(z)