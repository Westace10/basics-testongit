#def sentence_maker(phrase):
    #interogatives = ("how", "why", "who", "where")
    #capitalized = phrase.capitalize()
    #if phrase.startswith(interogatives):
        #return "{}?".format(capitalized)
    #else:
        #return "{}.".format(capitalized)

#results = []
#while True:
    #fname = input("Enter First name: ")
    #sname = input("Enter Surname: ")
    #fone = input("Enter Phone Number: ")
    #pnum = input("Enter Vehicle Registration Number: ")
    #save = input("Enter Save: ")
   #if save == "save":
     #   break
   # else:
   #     results.append(fname)
   #     continue
#print (results)

results = []
while True:
    fname = input("Enter First name: ")
    endname = input("Enter save: ")
    if endname == 'save':
        break
    else:
        results.append(fname)

print(results)