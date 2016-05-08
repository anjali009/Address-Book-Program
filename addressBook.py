#!/usr/bin/python

print '*****MENU*****'
print "1. Create a new entry"
print "2. Search a new entry"
answer = raw_input()

if answer == "1": 
    lastname = raw_input("Enter the last name? ")
    firstname = raw_input("Enter the first name? ")
    phone = raw_input("Enter the phone number? ")
    email = raw_input("Enter the email address? ")
    address = raw_input("Enter the persons address? ")

    temp1 = open("addressbook.txt","a")
    print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address) 

    temp1.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    temp1.write("\n")

elif answer == "2" :
    searchdetail = raw_input("Enter your search Criteria: firstname, lastname, phone number, email, address etc ")
    print searchdetail
    temp1 = open("addressbook.txt","r")
    for line in temp1:
        if searchdetail in line:
        	print line

else :
    print ("You have selected a wrong option!!")
   
