amout = float(input('Input amout: '))
serviceCharge = int(input('Input Service Charge(%): '))
tip = amout*(serviceCharge/100)
print(f'Tip:{tip:0.2f}, Total: {amout+tip:0.2f}')