# Py-functions-hw - hw 3
#q1
contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]
def CheckOwner():
    #q2,3,4
    for i in contactTable:
     Num = input('Enter ur Number:\n')
     if len(Num) != 10 or not (Num.isdigit()):
        print("invalid phone number")
        continue
     for ContactNum in contactTable :
        if ContactNum.get("Phone") == Num:
            print(ContactNum["name"])
            return   
    print("Sorry, the number is not found")      
CheckOwner()
