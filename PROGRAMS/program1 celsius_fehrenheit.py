'''
Write a menu driven program to convert the given temperature from Fahrenheit to Celsius and vice versa depending upon user’s choice.
'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("Enter your choice : \n1]Celcius to fehrenheit\n2]Fehrenheit to Celsius\n\n")
ans = int(input("Enter your choice : "))
if ans == 1:
    celsius = float(input("Enter your termperature in celsius : "))
    answer = celsius_to_fahrenheit(celsius)
    print("The temperature in fahrenheit is :", answer)
elif ans == 2:
    fehranheit = float(input("Enter your termperature in fehranheit : "))
    answer = fahrenheit_to_celsius(fehranheit)
    print("The temperature in celsius is :", answer)
else:
    print("Invalid choice \n Try again !")

