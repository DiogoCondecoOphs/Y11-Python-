compnum = 50
num = int(input("please enter a number "))
count = 1
val = "y"

while num != compnum:
    while val == "y":

     if num > compnum:
        print ("your guess was too high")
        num = int(input("please enter a number "))
        val = str(input("would you like another guess? y/n ")).lower()
        count = count +1


     elif num < compnum :
        print("your guess was too low")
        num = int(input("please enter a number "))
        val = str(input("would you like another guess? y/n ")).lower()
        count = count +1

     else:
        val = "n"


print("well done, you took",count,"attempts")
