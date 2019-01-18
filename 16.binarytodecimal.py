# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17, 2019

File: binarytodecimal.py
Converts a string of bits to a decimal integer.
@author: Byen23
"""

# This will be my 16th program to be uploaded on Github

bitString = input("Enter a string of bits: ")
decimal = 0 
exponent = len(bitString) - 1
for digit in bitString:
	decimal = decimal + int(digit) * 2 ** exponent
	exponent = exponent - 1
print("The integer value is", decimal)



