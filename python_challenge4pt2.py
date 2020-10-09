print("Welcome to the official registration program for  You Dunn Know")

fee= 10.0
ex_fee = 35.0
cas_fee = 20.0
us_exc = 1.5
au_exc = 2.0
#creates the variables that are about to be used

def info():
 email = str(input("Please enter your  You Dunn Know email address: "))

 global skill
 skill = str(input("Please enter the skill level on your card E or C: "))
 #casts the data to check with the database if availabe
 
 while skill != "E" and skill != "C":
    skill = str(input("please enter your skill level properly: "))
    
    #ensures that values are entered properly
 global country   
 country = str(input("Please enter your country of residence: UK, US or AU "))

 while country != "UK" and country != "US" and country != "AU":
    country = str(input("please enter your country properly: "))
    
    if skill == "E":
       global s_fee
       s_fee = fee + ex_fee
    
 else:
    s_fee = fee + cas_fee
    
#creates a fee for the difference in skill and the fee associated

info()
#calls subprogram

def calc():
    if country == "US":
        cost = (s_fee*us_exc)
        print("Your entry fee is",cost,"USD")
    elif country =="AU":
        cost = (s_fee*au_exc)
        print("Your entry fee is",cost,"AUD")
    else:
        cost = s_fee
        print("Your entry fee is",cost,"GBP")
#creates the subprogram for the calculation of the tournament

calc()
#calls subprogram
