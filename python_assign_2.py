while True:
    age = input("Are you a cigarette addict older than 75 years old? (Yes/No) : ")
    if age == "Yes":
        age = True
        break      
    elif age == "No":
        age = False
        print(age)
        break
    else:   
        print("Please enter Yes/No only!")
        continue
print(age)