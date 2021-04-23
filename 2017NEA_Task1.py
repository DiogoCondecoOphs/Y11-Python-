#2017NEA_Task1.py
#Diogo.c

print("""
          ######################
            League registration
          ######################""")
print(" ")

val = "n"

while val == "n":
    
 fname = str(input("Please enter your first name: "))

 lname= str(input("Please enter your last name: "))

 nick = str(input("Please enter your nickname: "))

 email = str(input("Please enter your email: "))
 

 skill = str(input("Please enter your skill level E/C ")).upper()

 if skill == "E":
     print("""
              Expert""")
     print(fname)
     print(lname)
     print(nick)
     print(email)
     print(" ")

     val = str(input("Are your details correct? y/n ")).lower()

 else:
     print("""
              Casual""")
     print(fname)
     print(lname)
     print(nick)
     print(email)
     print(" ")

     val = str(input("Are your details correct? y/n ")).lower()


print("Thank you for your entry")
