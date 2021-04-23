#stringslicing06.py
#Diogo.c

fname = str(input("Please enter your first name: "))
length = len(fname)

if length > 5:
    lname = str(input("Please enter your last name: "))
    fname = fname.upper()
    fullname = fname + lname
    print(fullname)

else:
    fname = fname.lower()
    print(fname)
    
