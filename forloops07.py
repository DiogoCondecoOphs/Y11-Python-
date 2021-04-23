#forloops07.py
#Diogo.c

total = 0
for i in range(0,6):
    num = int(input("please enter a number"))
    print("")
    val = str(input("Would you like to include that number? y/n ")).lower()
    
    if val == "y":   
     total = total + num

    else:
        print("")

print(total)
