dic = str(input("what direction do you want to count u/d?: ")).lower()

if dic == "u":
    tnum = int(input("Please enter the number you want to count up to: "))
    for i in range(0,tnum):
        print(i)
elif dic == "d":
    dnum = int(input("please enter a number below 20 to count down to: "))
    for i in range(dnum,0,-1):
     print(i)

else:
    print("i dont understand")
