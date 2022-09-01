# 
letter =''' Dear : <NAME>
           you are selected!
          date: <DATE> '''     
name = input("enter your name")
print("")
date = input("enter date ") 
print("")
print(name,date)
letter=letter.replace("<NAME>",name)
letter=letter.replace("<DATE>",date)
print(letter)
     
