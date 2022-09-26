contactTable = [{'name': 'Ahmed', 'phone': '0551112222'}, {'name': 'Saad', 'phone': '0551113333'},
                {'name': 'Sultan', 'phone': '0551114444'}, {'name': 'Morad', 'phone': '0551115555'}, {'name': 'Abdullah', 'phone': '0551116666'}]


def phonebook():

 user_number = input("Enter the phone number:-> ")

 if len(user_number) != 10 or not user_number.isdigit():
    return("Number is invalid")


 for contact in contactTable:
    if contact['phone'] == user_number:
        return contact['name']


 return("Sorry the number is not found")


print(phonebook())