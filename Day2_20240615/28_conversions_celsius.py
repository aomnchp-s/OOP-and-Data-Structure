def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * (celsius+32)
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit-32)
    return celsius

def main():
    enterC = float(input('Enter Temperature (°C) : '))
    enterF = float(input('Enter Temperature (°F) : '))

    fahrenheit = celsius_to_fahrenheit(enterC)
    celsius = fahrenheit_to_celsius(enterF)
    
    print(f'{"Celsius":5}  {"Fahrenheit":5}')
    print(f'{"-"*20}')
    print(f'{enterC:.2f}    {fahrenheit:.2f}')
    print(f'{celsius:.2f}     {enterF:.2f}')
    

if __name__=='__main__':
    main()