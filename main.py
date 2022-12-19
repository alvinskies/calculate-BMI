print("calculate your body mass index")
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height metres:  "))
BMI = weight/height**2
BMI = round(BMI,1)
if BMI > 24.9:
  print("You are overweight, BMI is:", BMI)
else:
  print("You are healthy, BMI is:",BMI)

