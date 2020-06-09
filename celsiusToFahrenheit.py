#Program Name: CelsiustoFahrenheit.py
#Last Updated: 2/28/2020
#Last Updated by: Aaron Amos
#Program Description: Convert Celsius to Fahrenheit

#Create Celsius input
celsius = float(input('Please input the temperature in Celsius:'))

#define conversion formula - celsius to fahrenheit
def convert_fahrenheit(celsius):
    return(celsius * (9.0/5.0)) + 32.0

print('The temperature is: ',(convert_fahrenheit(celsius)),chr(176)+"F")

