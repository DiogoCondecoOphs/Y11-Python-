#2017NEA_Task2.py
#Diogo.c

def calculator():

    print("Welcome to the registration calculator")

    val = "y"

    while val == "y":

     email = str(input("Please enter your email: "))
     print(" ")

     skill = str(input("Please enter your skill E/C ")).upper()
     print(" ")

     country = str(input("Please enter your country of residence UK,US,AU: ")).upper()
     print(" ")

     fee = 10.00
     
     e_fee = 35.00

     c_fee = 20.00

     total = 0.00

     if country == "UK":
         total = fee

         if skill == "E":
             total = total + e_fee
             print("total is",total,"GBP")

         else:
            total = total + c_fee
            print("total is",total,"GBP")

     elif country == "US":
         total = fee

         if skill == "E":
             total = total + e_fee
             total = total * 1.5
             print("total is",total,"USD")

         else:
            total = total + c_fee
            total = total *1.5
            print("total is",total,"USD")

     elif country == "AU":
         total = fee

         if skill == "E":
             total = total + e_fee
             total = total * 2.00
             print("total is",total,"AUD")

         else:
            total = total + c_fee
            total = total * 2.0
            print("total is",total,"AUD")

     else:
         print("Please enter a valid country")
     print(" ")
     val = str(input("Would you like to calculate another fee? y/n ")).lower()

    print("Thank you for using our fee calculator")
         
calculator()
