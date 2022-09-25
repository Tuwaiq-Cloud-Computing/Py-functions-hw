from asyncio.windows_events import NULL
from unicodedata import numeric


contactTable=[{"name":"Ahmed","Phone":"0551112222"},
{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},
{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]

phoneNumber=(input("Enter the phoneNumber:"))


def find(phoneNum):
    if phoneNum.__len__()!=10 or phoneNum.isnumeric() ==False:
        print("Invalid number")
        return

    for user in contactTable:
        if user["Phone"]==phoneNum:
            print("user found his name is",user["name"])
            return
    print("Not found")
    return
         
       


find(phoneNumber)# call find
