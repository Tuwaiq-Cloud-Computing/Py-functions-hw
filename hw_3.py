

contactTable=    [{"name":"Ahmed","Phone":"0551112222"},
                  {"name":"Saad","Phone":"0551113333"},
                  {"name":"Sultan","Phone":"0551114444"},
                  {"name":"Morad","Phone":"0551115555"},
                  {"name":"Abdullah","Phone":"0551116666"}]

def searchNumber():

    phonenum = input("Enter Phone number: ")

    if phonenum.isnumeric():

        if len(phonenum) == 10:

            for item in contactTable:
                if item['Phone'] == phonenum:
                    print(item['name'])
                    break

            else:
                print("Sorry, the number is not found")

        else:
            print("This is invalid number")
    else:
        print("This is invalid number###")


searchNumber()

searchNumber()

searchNumber()

searchNumber()

searchNumber()