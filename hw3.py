contactTable=[{"name":"Ahmed","Phone":"0551112222"}
              ,{"name":"Saad","Phone":"0551113333"}
              ,{"name":"Sultan","Phone":"0551114444"}
              ,{"name":"Morad","Phone":"0551115555"}
              ,{"name":"Abdullah","Phone":"0551116666"}]


def foundName(phoneNumber): 
    if len(phoneNumber) != 10 or phoneNumber.isnumeric() != True :
            return print("This is invalid number")
            
    for i in range(len(contactTable)):
        x = contactTable[i].get("Phone")
        
        if x == phoneNumber:
            print("the owner is",contactTable[i].get("name"))
            break
        elif x!=phoneNumber and i == len(contactTable)-1:
            print("Sorry, the number is not found")
         

foundName("0551116666")
      
            