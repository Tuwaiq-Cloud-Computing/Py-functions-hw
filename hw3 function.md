#Qustion 1

contactTable=[
    {"name":"Ahmed","Phone":"0551112222"},
    {"name":"Saad","Phone":"0551113333"},
    {"name":"Sultan","Phone":"0551114444"},
    {"name":"Morad","Phone":"0551115555"},
    {"name":"Abdullah","Phone":"0551116666"}
    ]

def theowner():
    
    #Qustions 2,3,4

    for i in contactTable:
     Num = input('Enter your Number:\n')


     if len(Num) != 10 :
        print("This is invalid phone number")

        continue

     for contactNumber in contactTable :
        if contactNumber.get("Phone") == Num:
            print(contactNumber["name"])

     else:
      return
      print("Sorry, the phone number is not found")

theowner()

