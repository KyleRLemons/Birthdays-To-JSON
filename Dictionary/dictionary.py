#USE JSON TO TURN DICTIONARY INTO JSON FILE THAT WILL PERSIST THE SAVED DATA
#IF NAME IS ALREADY IN DIC THEN ASK IF YOU WANT IT TO BE EDITED

import json


birthdays = {}
data = birthdays
def WriteToJsonFile(path,fileName,data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data,fp)
path = './'
filename = "birthdays"



while True:
    print("Enter a first and last name to find their birthday.")
    print("Type \"delete\" to enter delete mode or type \"all\" to print all names and birthdays: ")
    name = input().upper()
    if name == "DELETE":
        print("What name would you like to delete? Type nothing to cancel")
        name = input().upper()
        if name == "":
            continue
        del birthdays[name]
        print("Okay",name,"has been deleted.")
        continue
    elif name == 'ALL':
        for names in birthdays:
            print(names + " " + birthdays[names])
    elif name == '':
        break
    elif name in birthdays:
        print("Their birthday is",birthdays[name])
        print("Would you like to edit their name? Yes or no?")
        command = input().upper()
        if command == 'YES':
            del birthdays[name]
            print("Please enter their name:")
            name = input().upper()
            print("Please enter their birthday")
            bday = input()
            birthdays[name] = bday
            print("Okay,",name,"'s birthday is",birthdays[name])
            continue
    else:
        print("I don't have their birthday in my information.")
        print("Please type their birthday or enter nothing to cancel")
        bday = input()
        if bday == "":
            continue
        birthdays[name] = bday

        print("Okay, their name is",name,"and their birthday is",birthdays[name] )

WriteToJsonFile(path,filename,data)
