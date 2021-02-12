val = "y"
loop = 1

while val == "y":
    name=str(input("Please eneter the last name of the member: "))
    print(" ")
     
    memname = name[0:3] + str(loop)
    print(memname)
    
    loop = loop + 1

    print(" ")
    val = str(input("Would you like to add another member y/n? ")).lower()
    

print(" ")
print("Thank you for using our service")
    
    
