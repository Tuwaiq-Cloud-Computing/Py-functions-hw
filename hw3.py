contactTable=[{"name":"Ahmed","Phone":"0551112222"},
{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},
{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}] 




def digit (n):
    if len(n)!=10:
        print("This is invalid number")
     

def char(n):
    try:
      int(n)  
    except ValueError:
       print("This is Invalid number") 


def own(n):
    char(n)
    digit(n)
    for i in range(len(contactTable)):
        if n==contactTable[i]["Phone"]:
            return contactTable[i]["name"]
    return "Sorry, the number is not found"      

print(own("0551215555"))











