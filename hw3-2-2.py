# author: CCG 9/30/21

height = input("What is your height in centimeters?")
weight = input("What is your weight in kilograms?")

bmi = (int(weight) / int(height) ** 2) * 1000

if bmi < 19:
    print("You are underweight")
elif bmi < 25:
    print("You are healthy")
elif bmi < 25:
    print("You are overweight")
elif bmi < 25:
    print("You are obese")
else:
    print("You are very obese")
