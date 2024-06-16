weight = float(input('Input Weight(kg): '))
height = float(input('Input Weight(m): '))
bmi = weight/(height*height)

if bmi >= 30.0:
    print('Obese')
elif bmi >= 25.0:
    print('Overweight')
elif bmi >= 18.5:
    print('Normal or Healthyweight')
else:
    print('Underweight')



