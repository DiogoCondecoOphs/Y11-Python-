#WHILELOOPchallenges04
#Diogo.c

count = 0
valid = "y"

while valid == "y":
    name = str(input("who would you like to invite to the party "))
    print(name,"has now been invited")
    count = count + 1
    valid = str(input("Would you like to invite someone else? y/n "))

print(count,"person/people were invited")
