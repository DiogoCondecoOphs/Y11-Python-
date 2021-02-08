inv = int(input("please enter the number of invitees you want "))

if inv < 10:
    for i in range(0,inv):
         name = str(input("What is the invitee's name: "))
         print(name,"has been invited")
         print("")
         
else:
    print("Too many people")
    
