#-------------------------------------------------------------Code Begins Here----------------------------------------------------------------------------#
import csv
platelist = []
reader = []
#-------------------------------------------------------Login Section Begins------------------------------------------------------#
print('Welcome, Kindly input your login details')
username = input("Username: ")
password = input("Password: ")
while True:
    if username == 'admin' and password == 'wython':
        welcomemess = f"Hello, {username}" 
        print (welcomemess)
        break
    else:
        print ('Incorrect username/password, try again!!!')
        continue
#--------------------------------------------------------Login Section Ends-------------------------------------------------------#
#-----------------------------------------------------Activity Section Begins-----------------------------------------------------#
while True:
    activity = input("What would you like to do, Retrieval or Registration: ")
    if activity == "registration":
#------------------------------------------------------Registration Section-------------------------------------------------------#
        print("Let's Start.....")
        while True:
            firstname = input("Enter First Name: ")
            if firstname == "cancel":
                cancelaction = input("Are you sure (Y/N): ")
                if cancelaction == 'y':
                    print("You terminated the process, enjoy your day!")
                    break
                else:
                    continue
            Surname = input("Enter Last Name: ")
            if Surname == "cancel":
                cancelaction = input("Are you sure (Y/N): ")
                if cancelaction == 'y':
                    print("You terminated the process, enjoy your day!")
                    break
                else:
                    continue
            Phonestr = input("Enter Phone Number: ")
            if Phonestr == "cancel":
                cancelaction = input("Are you sure (Y/N): ")
                if cancelaction == 'y':
                    print("You terminated the process, enjoy your day!")
                    break
                else:
                    continue
            platenumber = input("Enter Registration Number: ")
            if platenumber == "cancel":
                cancelaction = input("Are you sure (Y/N): ")
                if cancelaction == 'y':
                    print("You terminated the process, enjoy your day!")
                    break
                else:
                    continue
            save = input("Type Save: ")
            Phone = int(Phonestr)
            message = "Kindly confirm details below:\n" + "First Name: " + firstname + "\n" + "Last Name: " + Surname + "\n" + "Phone Number: 0" + str(Phone) + "\n" + "Vehicle Registration Number: " + platenumber
            platelist = [platenumber, firstname, Surname, Phonestr]
            if save == "save":
                print(message)
                confirmation = input("is this correct? Y or N: ")
                if confirmation == "Y" or confirmation =="y":
                    with open('vehireg.csv', 'a', newline='\n') as my_file:
                        writer = csv.writer(my_file)
                        writer.writerow(platelist)
                    print(platelist[0])
                    print("Saved")
                    morereg = input("Do you wish to add more? Y or N: ")
                    if morereg == "Y" or morereg == "y":
                        continue
                    elif morereg == "N" or morereg == "n":
                        print("Have a lovely day!")
                        break
#-----------------------------------------------------------------Retrieval Section--------------------------------------------------#
        break
    elif activity == "retrieval":
        while True:
            retrievestep = input("Enter Vehicle Registration Number: ")
            with open('vehireg.csv', 'r') as one_file:
                reader = csv.reader(one_file, skipinitialspace=True)
                for row in reader:
                    if retrievestep == row[0]:
                        numb = row[0]
                        name = row[1]
                        sname = row[2]
                        fone = row[3]
                        fmessage = "Here are the details of vehicle with registration number " + numb + ','+ '\n' + 'First name: ' + name + '\n'+ 'Surname: ' + sname + '\n' + 'Phone Number: ' + fone
                        print(fmessage)
                        moreret = input("Do you wish to check again? Y or N: ")
                        if moreret == "Y" or moreret == "y":
                            continue
                        elif moreret == "N" or moreret == "n":
                            print("Have a lovely day!")
                            break
            break
        break
#----------------------------------------------------------Activity Section Ends----------------------------------------------------------#
#-------------------------------------------------------------Code Ends Here----------------------------------------------------------------------------#