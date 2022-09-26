import re


def contactTables(mobile):
    print("input mobile number lookink for: ")
    mobile=input()
    #If the number is less or more than 10 numbers, print "This is invalid number".
    if (len(mobile)>10):
        print("this is not mobile number !")
    # elif len(str(mobile)) > 10:
    #         print('This is invalid number')
    # elif len(str(mobile)) < 10:
    #         print('This is invalid number')
    # elif mobile not in contactTable:
    #         print('Sorry, the number is not found')
    # else:
    #     print('This is invalid number')    
        #--If the number contains letters or symbols, print "This is invalid number".
        #re.match(r'^([\s\d]+)$', mobile)
    contactTable = [{"name": "Ahmed", "Phone": "0551112222"}, {"name": "Saad", "Phone": "0551113333"}, {
        "name": "Sultan", "Phone": "0551114444"}, {"name": "Morad", "Phone": "0551115555"},
        {"name": "Abdullah", "Phone": "0551116666"}]

    result = next(
        (item for item in contactTable if item['Phone'] == mobile),
    {}
)
    print(result.get('name'))  # 👉️ 




contactTables(mobile=True)
