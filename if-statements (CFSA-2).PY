while True:
    age = input("Are you a cigarette addict older than 75 years old? (Yes/No) : ")
    if age == "Yes":
        age = True
        break      
    elif age == "No":
        age = False
        break
    else:   
        print("Please enter Yes/No only!")
        continue
while True:
    chronic = input("Do you have a severe chronic disease? (Yes/No) : ")
    if chronic == "Yes":
        chronic = True
        break      
    elif chronic == "No":
        chronic = False
        break
    else:   
        print("Please enter Yes/No only!")
        continue
while True:
    immune = input("Is your immune system too weak? (Yes/No) : ")
    if immune == "Yes":
        immune = True
        break      
    elif immune == "No":
        immune = False
        break
    else:   
        print("Please enter Yes/No only!")
        continue
extreme = age and chronic and immune
very = age and chronic or chronic and immune or age and immune
high = age or chronic or immune

if extreme == True:
    risk = "in extremely risky"
elif very == True:
    risk = "in very risky"
else:
    if high == True:
        risk = "in risky"
    else: risk = "not in risky"

print ("You are " + risk + " group.")