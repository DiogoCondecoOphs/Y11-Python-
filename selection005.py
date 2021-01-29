rain = str(input("Is it raining right now?: ")).lower()

if rain == "yes":
 wind= str(input("Is it windy?: ")).lower()
 if wind == "yes" : 
  print("it is too windy for an umbrella")
 else:
  print("Take an umbrella")
else:
 print("Enjoy your day")
