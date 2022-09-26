# Py-functions-hw - hw 3
## Contact Table
#| Name | Number |
#| --- | ------------- |
#| Ahmed | 0551112222 |
#| Saad | 0551113333 |
#| Sultan | 0551114444 |
#| Morad | 0551115555 |
#| Abdullah| 0551116666 |


 
def myFun():
 contactTable=[{"name":"Ahmed","Phone": "0551112222"},{"name":"Saad","Phone":"0551113333"},{"name":"Sultan","Phone":"0551114444"},{"name":"Morad","Phone":"0551115555"},{"name":"Abdullah","Phone":"0551116666"}]
 request1 = str(input("please enter the phone number"))
 for x in contactTable:
   if request1 == contactTable ["phone"]:
      print(contactTable["name"])
      break
   else:
    print("Sorry, the number is not found")
   if request1 > 10 or request1 < 10:
    print("This is invalid number")
   elif request1.isalpha() and request1.isalnum():
    print("This is invalid number")


myFun()
