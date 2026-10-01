temp = float(input("Enter the Temprature:- "))

choice = (input("Enter C for celcious to Fahranheit Or F for Fahrenheit to celcious:- "))
if choice.upper() == "C":
    fahrenheit = (temp *9/5) + 32
    print(f"Temprature is  {fahrenheit} F'")

elif choice.upper() == "F":
    celcious = (temp - 32)* 5/9
    print(f"Temprature is   {celcious}  C'")

else:
    print("Invalid ")