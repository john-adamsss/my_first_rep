print("Welcome to simple conversion tool...")
print("Conversion Options: \n 1.\t Celsius to Fahrenheit \n 2.\t Fahrenheit to Celsius")
print(" 3.\t Kilometers to Miles \n 4.\t Miles to Kilometers")
while True:
    choose = input("Please choose your option. Press 1/2/3/4 : ")
    if choose == "1":
        celsius = input("Please input your Celsius value : ")
        celsius = float(celsius)
        fahrenheit = 1.8*celsius+32
        print("%.1f°C = %.1f°F" % (celsius, fahrenheit))
        break
    elif choose == "2":
        fahrenheit = input("Please input your Fahrenheit value : ")
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit-32)/1.8
        print("%.1f°F = %.1f°C" % (fahrenheit, celsius))
        break
    elif choose == "3":
        kmeters = input("Please input your Kilometer value : ")
        kmeters = float(kmeters)
        miles = kmeters/1.609
        print("%.1f kms = %.1f miles" % (kmeters, miles))
        break
    elif choose == "4":
        miles = input("Please input your Mile value : ")
        miles = float(miles)
        kmeters = miles*1.609
        print("%.1f miles = %.1f kms" % (miles, kmeters))
        break
    else: 
        print("Please enter 1,2,3,4 only!") 
        continue
    print("Thank You for Using This Tool!")