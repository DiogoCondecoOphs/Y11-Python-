#WHILELOOPchallenges03
#Diogo.c

num1= int(input("please enter a number "))
total = num1
val= "y"

while val == "y":
    num2 = int(input("please enter another number "))
    total = total + num2
    val=str(input("would you like to add another number y/n "))

print("total was",total)
