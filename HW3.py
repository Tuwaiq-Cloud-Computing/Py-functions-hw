# Py-functions-hw - hw 3
# Question 1: Build a phone book program that receives the phone number, and returns the name of the owner.
# You can follow the table below:
## Contact Table
# | Name | Number |
# | --- | ------------- |
# | Ahmed | 0551112222 |
# | Saad | 0551113333 |
# | Sultan | 0551114444 |
# | Morad | 0551115555 |
# | Abdullah| 0551116666 |

#from curses.ascii import isdigit

# This is the list of dictionaries you can use to build this function:

contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]

# Q1 - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".

userInput = str(input ("Please enter the phone number \n"))

#def fun1(userInput):
# for n in contactTable:   
#    if userInput == n["Phone"]: 
#       print(n["name"])
#       #break
#    else:
#        print("Sorry, the number is not found")  

#print(fun1(userInput)) 



# Q2 - If the number is less or more than 10 numbers, print "This is invalid number".

#for n in contactTable:
#    if len(userInput) == len(n["Phone"]):
#        print(userInput)
#        
#    else:
#        print("This is invalid number")



# Q3 - If the number contains letters or symbols, print "This is invalid number".

# i tried to solve it but i could not! sorry.


#import re 
#x = userInput
#pattern = r'\W+'
#t = re.split(pattern, x)
#print(t)
#print(t.isdigit())
    
# or 
#ifnum= re.split(r'\s', x)
#ifnum= re.findall(r'\s', x)
#for ifnum in userInput:
#    print(ifnum)

# i tried to solve it but i could not! sorry.
