contactTable=[{"name":"Ahmed","Phone":"0551112222"},                                         
              {"name":"Saad","Phone":"0551113333"},                                          
              {"name":"Sultan","Phone":"0551114444"},                                        
              {"name":"Morad","Phone":"0551115555"},                                         
              {"name":"Abdullah","Phone":"0551116666"}                                       
            ]                                                                                

a = input("Enter a number :")                                                                

def isValidNumber(phone):                                                                    
    return not (len(a) != 10 or a.isdigit() != True)                                         

def findPhone(input_phone, contacts):                                                        
    for contact in contacts:                                                                 
        phone = contact.get("Phone")                                                         
        name = contact.get("name")                                                           
        if phone == input_phone:                                                             
            return contact                                                                   
    return False                                                                             

if isValidNumber(a):                                                                         
    contact = findPhone(a, contactTable)                                                     
    if contact:                                                                              
        print("this phone number:",contact.get("Phone"), "belong to :", contact.get("name")) 
    else:                                                                                    
        print("Sorry, the number is not found")                                              
else:                                                                                        
    print("This is invalid number")