
contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},
    {"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]

def checkOwner(phone):
    
    for i in contactTable:
      if i.get("Phone") == phone:
        print(i["name"])

      elif len(phone)>10 or len(phone)<10:
        print("This is invalid number ")
    
      elif not phone.isnumeric():
        print("This is invalid number")

    else:
     print("Sorry, the number is not found")


phone = input("Enter Phone number : ")
checkOwner(phone)