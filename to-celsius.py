#!/usr/bin/env python3.7

#Python implementation goes here 

farhrenheit = float(input("What temperature (in Farhrenheit) would you like converted to Celsius? "))

celsius = (farhrenheit -32) * 5/9

print(farhrenheit, "F is", round(celsius, 2), "C")