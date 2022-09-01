s1=int(input("enter the first no. "))
s2=int(input("enter the second no. "))
s3=int(input("enter the third no. "))
# if(s1>40):
#     print("first subject he is pass")
# if(s2>40):
#     print("he is pass in second subject ")
# if(s3>40):
#     print("student is pass in third subject")
# else:
#     print("student is failed")

if(s1<33 or s2< 33 or s3<33):
    print("you are fail")
elif(s1+s2+s3)/3<40:
    print("you are fail in this exam")
else:
    print("you are pass")
