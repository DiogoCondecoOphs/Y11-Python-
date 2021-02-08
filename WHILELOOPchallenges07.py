val = 10


while val > 0:
 print("There are",val,"green bottles hanging on the wall,")
 print(val,"green bottles hanging on the wall")
 print("and if one green bottle should accidnetally fall")
 print(" ")
 
 
 guess = int(input("How many green bottles will be hanging on the wall? "))
 val = val -1
 if guess == val:
     print("")
     print("There'll be",val,"bottles hanging on the wall!")

 else:
 
  while guess != val:
     print("no, try again")
     print("")
     guess = int(input("How many green bottles will be hanging on the wall? "))
     print("")
     print("There'll be",val,"bottles hanging on the wall!")


   
print("There'll be no green bottles hanging on the wall")
