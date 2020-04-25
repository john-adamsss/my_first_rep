a = input("Enter a number please \n")
if  a.isdigit() == True :
    c = 0
    for b in a:
        b = int(b)
        c += b**len(a)
    a = int(a)
    if c == a:
        print ("{} is an amstrong number.".format(a))
    else: 
        print ("{} is not an amstrong number.".format(a))
elif a[0] == "-" :
    print("Please enter a positive number")
elif "." in a or "," in a: 
    print("Please enter an integer number")
else : print("Do not use any entries other than numeric values")