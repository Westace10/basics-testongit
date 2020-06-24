while True:
    year = input("Enter the Year:")
    message = "You entered '%s'" %year
    centurydiv = int(year)/100
    centuryrem = int(year)%100
    centurycheck = int(centurydiv)
    print(message)
    if (centuryrem > 1 and centurycheck > 1):
        print("It has been " + str(centurycheck) + " Centuries" + " and " + str(centuryrem) + " years!")
    elif (centuryrem <= 1 and centurycheck > 1):
        print("It has been " + str(centurycheck) + " Centuries" + " and " + str(centuryrem) + " year!")
    elif (centuryrem <= 1 and centurycheck <= 1):
        print("It has been " + str(centurycheck) + " Century" + " and " + str(centuryrem) + " year!")