#This code is used to create details for a username signing up for a game service for the first time (really basic)
print("Welcome to [insert game name]")
age= int(input("Please enter your age: "))
sex = str(input("Please enter your gender: "))
email = str(input("Please enter your email address: "))
username= str(input("Please enter your username :"))
#This initialises the data of the player

print(age)
age_conf =str(input("Is this your age? y/n "))
while age_conf != "y":
     age=int(input("Please re-enter your age :"))
     print(age)
     age_conf =str(input("Is this your age? y/n "))
#keeps asking user to input age until they're happy
     
print(sex)
sex_conf =str(input("Is this your gender? y/n "))
while sex_conf != "y":
     sex=str(input("Please re-enter your gender :"))
     print(sex)
     sex_conf =str(input("Is this your gender? y/n "))
     
#keeps asking user to input gender until they're happy

print(email)
email_conf =str(input("Is this your Email? y/n "))
while email_conf != "y":
     email=str(input("Please re-enter your Email :"))
     print(email)
     email_conf =str(input("Is this your Email? y/n "))
     
print(username)
username_conf =str(input("Is this your username? y/n "))
while username_conf != "y":
     username=int(input("Please re-enter your username :"))
     print(username)
     username_conf =str(input("Is this your username? y/n "))

print("""Here are your details
      age is""",age,"""
      username is""",username,"""
      email is""",email,"""
      gender is """,sex,)
print("Thank you for regsitering to [insert game name], have fun")     
exit
#data is registered for the user correctly and exits from the screen

     
