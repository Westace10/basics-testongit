activity = input("What would you like to do, Retrieval or Registration: ")
if activity == "registration":
    print("Let's Start.....")
    while True:
        firstname = input("Enter First Name: ")
        surname = input("Enter Last Name: ")
        phonestr = input("Enter Phone Number: ")
        platenumber = input("Enter Registration Number: ")
        phone = int(phonestr)
        message = "Kindly confirm details below:\n" + "First Name: " + firstname + "\n" + "Last Name: " + surname + "\n" + "Phone Number: 0" + str(phone) + "\n" + "Vehicle Registration Number: " + platenumber
        vehiregdict = {platenumber: [firstname, surname, phone]}
        with open("vehiclereg.json", "r+") as file:
            regdata = json.dumps(file)
            regdata.update(vehiregdict)
            file.seek(0)
            json.dumps(regdata, file)
                #morereg = input("Do you wish to add more? Y or N: ")
                #if morereg == "Y" or morereg == "y":
                    #continue
                #elif morereg == "N" or morereg == "n":
                    #print("Have a lovely day!")
                    #break
        #break
    #reader = json.load(open("userpass.json"))
        #def getreader(retpassword):
           #return reader[retpassword]

        #user = getreader(retpassword)
        #if user == retusername:
         #   mess1 = "Welcome, " + user
          #  print(mess1)
         #  break
        #else:
          #  print("Incorrect username/password!")
           # continue