# find double space in string 
# line=" god how are you ?  good  and what about  me i am  also good  god by  "
# doublespace=line.find("  ")
# print(doublespace)
#  replace the doublespace with single space
line = " hello god how  are you  i am good"
print(line)
dou = line.find("  ")
print(dou)
line =line.replace("  "," ")
print(line)