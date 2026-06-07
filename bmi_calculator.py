weight = input("type your weight (kg)")
height = input("type your height (m)")
BMI = (float(weight) / (float(height) * float(height)))
print("your BMI is  :  " + str(BMI))

if BMI <= 18.5:
    print("you are underweight")
elif 18.5 < BMI <= 25:
    print("you are normal")
elif 25 < BMI <= 30:
    print("you are Overweight")
elif 30 < BMI:
    print("you are obese")