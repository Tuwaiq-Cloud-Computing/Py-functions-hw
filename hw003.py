
def fen():

    i=True
    contactTable=[{"name":"Ahmed","Phone":"0551112222"},{"name":"Saad","Phone":"0551113333"},
        {"name":"Sultan","Phone":"0551114444"},
        {"name":"Morad","Phone":"0551115555"},{
            "name":"Abdullah","Phone":"0551116666"}]
    while i:
        print("plese Enter mobile number looking for:")
        n1=input()
        n1.isnumeric()

        if len(n1) != 10 :
                print("This is invalid number")
        else:
            i = False

    for item in contactTable:
                if item['Phone'] == n1:
                    print(item.get('name'))
                    return
    print("Sorry, the number is not found")

fen()