# # Py-functions-hw - hw 3
# Question 1: Build a phone book program that receives the phone number, and returns the name of the owner.
# You can follow the table below:
# ## Contact Table
# | Name | Number |
# | --- | ------------- |
# | Ahmed | 0551112222 |
# | Saad | 0551113333 |
# | Sultan | 0551114444 |
# | Morad | 0551115555 |
# | Abdullah| 0551116666 |

# This is the list of dictionaries you can use to build this function:

contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},
 {"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}] 

def checkContact():
    
    num=input("please enter your phone# ")
    for phoneNumber in contactTable:
        if phoneNumber.get("Phone")==num:
            print(phoneNumber["name"])

    if type(num)!=int and len(num)!=10:
        print("This is invalid number") 
    else:
        print("Sorry, the number is not found")
        

checkContact()



# - If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
# - If the number is less or more than 10 numbers, print "This is invalid number".
# - If the number contains letters or symbols, print "This is invalid number".

    

