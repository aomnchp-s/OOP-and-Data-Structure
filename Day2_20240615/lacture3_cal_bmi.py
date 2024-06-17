weight = float(input('Enter weight (kg.): '))
height = float(input('Enter height (m.): '))
bmi = weight/(height*height)
print(f'BMI is {bmi:.2f}')
print('Weight Status: ', end='')

#1
if bmi < 18.5:
    print('Underweight')
elif bmi < 24.9:
    print('Normal or Healthyweight')
elif bmi < 29.9:
    print('Overweight')
else:
    print('Obese')

#2
print(f'{" ":4} {"BMI":20} {"Weight Status":30}')
print(f'{"===>" if bmi<18.5 else "    "} {"Below 18.5":20} {"Underweight":30}')
print(f'{"===>" if 18.5<=bmi<24.9 else "    "} {"18.5 - 24.9":20} {"Normal or Healthyweight":30}')
print(f'{"===>" if 24.9<=bmi<29.9 else "    "} {"25.0 - 24.9":20} {"Overweight":30}')
print(f'{"===>" if bmi >= 29.9 else "    "} {"30.0 and Above":20} {"Obese":30}')