# Enter your height in meters e.g., 1.55
height = float(input("How tall are you (meters): "))
# Enter your weight in kilograms e.g., 72
weight = int(input("What is your weight (kilograms): "))


imc = round(weight / (height * height))
if imc < 18.5:
    print(f"The body mass index is {imc}. You are underweight.")
elif imc < 25:
    print(f"The body mass index is {imc}. You have a normal weight.")
elif imc < 30:
    print(f"The body mass index is {imc}. You are slightly overweight.")
elif imc < 35:
    print(f"The body mass index is {imc}. You are obese.")
else:
    print(f"The body mass index is {imc}. You are clinically obese.")
