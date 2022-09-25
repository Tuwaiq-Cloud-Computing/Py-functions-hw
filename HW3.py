def contact():
    numb = input("Please Enter a number: ")
    contactTable=[
    {"name":"Ahmed","Phone":"0551112222"},
    {"name":"Saad","Phone":"0551113333"},
    {"name":"Sultan","Phone":"0551114444"},
    {"name":"Morad","Phone":"0551115555"},
    {"name":"Abdullah","Phone":"0551116666"}]
    if numb == "0551112222":
        print("This Number Belong to: Ahmed")
    elif numb == "0551113333":
        print("This Number Belong to: Saad")
    elif numb == "0551114444":
        print("This Number Belong to: Sultan")
    elif numb == "0551115555":
        print("TThis Number Belong to: Morad")
    elif numb == "0551116666":
        print("This Number Belong to: Abdullah")
    elif numb != contactTable:
        print("Sorry, the number is not found")
    elif numb <= 10:
           print("This is invalid number")
    else:    
        print("This is invalid number")
contact()