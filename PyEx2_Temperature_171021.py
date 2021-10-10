import math

temp = eval(input("Enter a temperature in Fahrenheit: "))

while temp < -58 or temp > 41:
    print("Temperature must be between -58F and 41F.")
    temp = eval(input("Re-enter temperature in F: "))

speed = eval(input("Enter wind speed: "))

while speed < 2:
    print("Speed must be greater or equal to 2")
    speed = eval(input("Re-enter speed in mph: "))

wind_chill = 35.74 + (0.6215 * temp) - (35.75 * math.pow(speed, 0.16)) + (0.4275 * temp * math.pow(speed, 0.16))

print("The wind chill index is {:.3f}".format(wind_chill))