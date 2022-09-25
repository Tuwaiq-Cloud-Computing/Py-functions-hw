


contactTable =[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]


def num():
    
    for x in contactTable:
        
            x = int(input("Please Enter Phone number :\n"))
        
            print("This is invalid number!!!")

    else:
        x = contactTable.index(x)
        print(contactTable[x])
    
        print("Sorry,the number is not found!!!")

def name():
     
    if x in contactTable:
       
            x = str(input("enter name:\n"))
            x = contactTable.index(x)
        
            print("This is invalid number!!!")
        
print(name(),num())
