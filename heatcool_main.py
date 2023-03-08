# Lab Exercise Heating/Cooling
import random
divider = '=' * 30 + '\n'
print('Exercise Heating/Cooling\n')
print(divider)

def heat_cool(actualTemp, desiredTemp):
    actualTemp = float(actualTemp)
    desiredTemp = float(desiredTemp)
    if(desiredTemp < actualTemp):
        print('Running A/C...')
        return (f'Current temp is now {desiredTemp}')
    elif(desiredTemp > actualTemp):
        print("Running heat...")
        return (f'Current temp is now {desiredTemp}')
    else:
        print('Standby..')
        return (f'Current temp is now {desiredTemp}')
# beginning prompt code
name = input("Hello! What is your name? ")
actual_temp = random.randint(-460,500)


desiredTemp = input(f"Hello {name}, the current temperature is {actual_temp}. What is your desired temp? ")
print(heat_cool(actual_temp, desiredTemp))

print(divider)
print('Exercise Extended Challenge\n')
print(divider)

# beginning extended challenge

def temp_converter(tempCelsius, targetUnit):
    targetUnit = targetUnit.lower()
    if (targetUnit[0] == 'k'):
        print(f'This is your current temp in Celsius: {tempCelsius}C')
        tempCelsius = (float(tempCelsius) + 273.15)
        return f'This is your temperature converted to Kelvin: {tempCelsius}K'

    elif(targetUnit[0] == 'f'):
        print(f'This is your current temp in Celsius: {tempCelsius}C')
        tempCelsius = (float(tempCelsius) * (9/5)) + 32
        return f'This is your temperature converted to Fahrenheit: {tempCelsius}F'
    elif(targetUnit[0] == 'c'):
        print(f'This is your current temp in Celsius: {tempCelsius}C')
        return f'There is no conversion needed, you already are in Celsius. Your temp is {tempCelsius}C'
    else:
        print('Please enter a correct unit of measurement for temperature (Kelvin, Celsius, Fahrenheit')
    return f'this is your temp in celsius: {tempCelsius}C'

tempCelsius = input(f'Hello {name}, please enter a temperature in Celsius: ')
targetUnit = input('What unit would you like to convert to? \nKelvin\nFahrenheit\nCelsius\n')
print(temp_converter(tempCelsius, targetUnit))
print('\n<END PROGRAM>')






