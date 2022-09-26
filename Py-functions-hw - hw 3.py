"""
Question 1: Build a phone book program that receives the phone number,
and returns the name of the owner. You can follow the table below:
"""
contactTable=[{"name":"Ahmed","Phone":"0551112222"},\
              {"name":"Saad","Phone":"0551113333"},\
              {"name":"Sultan","Phone":"0551114444"},\
              {"name":"Morad","Phone":"0551115555"},\
              {"name":"Abdullah","Phone":"0551116666"}]

def PhoneCheck():
    allowed_chars = set("0123456789")
    print(allowed_chars)
    PhoneNumber = input("Please Enter the Phone Number 'Only Numbers': ")
    validation = set((PhoneNumber))
    if len(PhoneNumber) != 10 or not validation.issubset(allowed_chars):
        print("This is invalid number")
    else:
        #print(validation)
        for item in contactTable:
            # n.get("Phone")
            if PhoneNumber == item.get("Phone"):
                item.get("name")
                print(item.get("name"))
                return
        print("Sorry, the number is not found")

    #return PhoneNumber


    #PhoneNumber = input("Please Enter the Phone Number: ")
    #validation = set((PhoneNumber))
    #if len(PhoneNumber) == 10 and validation.issubset(allowed_chars):
    #    pass
        #print("Wait for check")
    ##else:
      #  print("This is invalid number")

    #if not filter(lambda d: d['Phone'] == PhoneNumber, contactTable):
     #   print('Item does not exist')
    #if not any(d["Phone"] == '0551112222' for d in contactTable):
     #   print('Not exists!')

    #for entry in checkphone:
     #       if entry[key] == value:
      #          print("found")

        #return {}

    #value_to_check = some_value
    #exist = PhoneNumber.exist['Phone']
    #for exist in PhoneNumber:
       # for key in exist:
        #        if exist[key] == value_to_check:
        #            print
          #          "Value is present"
    #exists = list(filter(lambda phoneexist: phoneexist.get("Phone")
    #for PhoneNumber in contactTable:
     #   if PhoneNumber == exists:
      #  #if value in contactTable.item():
       #     print("fount")



PhoneCheck()

"""def PhoneCheck():
    
    allowed_chars = set("0123456789")
    PhoneNumber = input("Please Enter the Phone Number: ")
    #validation = set((PhoneNumber))
    if len(PhoneNumber) == 10 : #and validation.issubset(allowed_chars):
        return 10
       print("This is invalid number")
    #elif validation.issubset(allowed_chars):
     #      print("This is invalid number")
PhoneCheck()"""
#else:
 #   print("False")
#def PhoneCheck():
 #   PhoneNumber = input("Please Enter the Phone Number: ")
    #while len(PhoneNumber) == (10):
  #  if len(PhoneNumber) != (10):
   #     print("This is invalid number")
    #if PhoneNumber.ASCII():
     #   print("This is invalid number")

        #return PhoneNumber
    #if "@_!#$%^&*()<>?/\|}{~:]" in PhoneNumber:
     #   print("This is invalid number")
    #elif "@_!#$%^&*()<>?/\|}{~:]" in PhoneNumber:  # If the number is less or more than 10 numbers, print "This is invalid number".
        #print("This is invalid number")
   # elif PhoneNumber.isalpha():
       # print("This is invalid number")




    #if (len(PhoneNumber) != (10):
     #   print("test")
#elif "@_!#$%^&*()<>?/\|}{~:]" in PhoneNumber:


#

    #
     #   for number in PhoneNumber:
      #      if number.isalpha():
       #         print("This is invalid number")
        #    elif number.c

#    str1.isalpha():

 #       print("This is invalid number")
#
# elif PhoneNumber.isalnum():
        #print("This is invalid number")



        #for Phone in contactTable.values():
         #print(Phone)
    #for key, value in contactTable.items():

     #   while len(PhoneNumber) == 10:
      #      if PhoneNumber in PhoneNumber.items():
       #         print("test")
        #    else:
         #       print("test2")
        #break
#PhoneCheck()

"""If the number exists, print the owner. Otherwise, print "Sorry, the number is not found".
If the number is less or more than 10 numbers, print "This is invalid number".
If the number contains letters or symbols, print "This is invalid number"."""
