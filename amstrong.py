a = input("Enter a number please \n")
liste = list(a)
if  a.isdigit() == True :
    c = 0
    for b in liste:
        b = int(b)
        c += b**len(liste)
    a = int(a)
    if c == a:
        print ("{} is an amstrong number.".format(a))
    else: 
        print ("{} is not an amstrong number.".format(a))
elif "-" in liste:
    print("Please enter a positive number")
elif "." in liste or "," in liste: 
    print("Please enter an integer number")
else : print("Do not use any entries other than numeric values")