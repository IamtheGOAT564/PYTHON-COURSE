temp=input("Enter the temperature in Celsius")
if temp<20:
    outfit="Jacket"
    print("It is cold today.")
    print("Wear a", outfit )
else:
    outfit="T-Shirt"
    print("It is warm today")
    print("Wear a", outfit)
rain=input("Is it raining today?")
if rain=="yes":
    print("Bring an umbrella.")
    