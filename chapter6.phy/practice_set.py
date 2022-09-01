# find greatest number enter by the user
s=int(input("enter the first no. "))
t=int(input("enter the second no. "))
u=int(input("enter the third no. "))
v=int(input("enter the fourth no. "))
w=int(input("enter the value of no."))
x=int(input("enter the value of x no. "))
if(s>t):
    f1=s
else:
    f1=t
if(u>v):
    f2=U
else:
    f2=v     
if(w>x):
    f3=w
else:
    f3=x

if(f1>f2>f3):       
    print( str(f1) + " is the greatest no. ")
if(f1<f2<f3):
    print( str(f3) +"is the greatest no. ")
else:
    print(str(f2)+ " is the greatest no. ")    
