


contactTable = [{"name": "Ahmed", "Phone": "0551112222"}
                , {"name": "Saad", "Phone": "0551113333"},
                {"name": "Sultan", "Phone": "0551114444"},
                {"name": "Morad", "Phone": "0551115555"},
                {"name": "Abdullah", "Phone": "0551116666"}
                ]

def phone_book():
    
    while True:
        
     number = input('Please Enter Phone Number :\n')
     
     if len(number) != 10 or not (number.isdigit()):
        print("invalid phone number")
        continue
    
     for contact in contactTable :
        if contact.get("Phone") == number:
            print(contact["name"])
            return
            
     print("Sorry, the number is not found")      


if __name__ == '__main__':
   
    phone_book()