print("Welcome to the official registration program for  You Dunn Know")
email = str(input("Please enter your  You Dunn Know email address: "))
skill = str(input("Please enter the skill level on your card E or C: "))

while skill != "E" and skill != "C":
    skill = str(input("please enter your skill level properly: "))
    
country = str(input("Please enter your country of residence: UK, US or AU "))

while country != "UK" and country != "US" and country != "AU":
    country = str(input("please enter your country properly: "))

fee = 10.0
ex_fee = 35.0
cas_fee = 20.0
              
if skill == "E":
       fee = fee + ex_fee
else:
    fee = fee + cas_fee

def calc():
    if country =="US":
        fee = fee*1.50
        print("Your entry fee is",fee,"USD")
    elif country =="AU":
        fee= fee*2.0
        print("Your entry fee is",fee,"AUD")
    else:
        print("Your entry fee is",fee,"GBP")

calc()
              
