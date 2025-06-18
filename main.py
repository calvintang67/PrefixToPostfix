# Name: Calvin Tang

# main.jpynb
# This program reads .txt files containing prefix expressions & test cases and
# writes their corresponding postfix expressions on an output .txt file

# Modules:
# 1. stack: Allows for Stack ADT creations and manipulation
# 2. conversionFunctions: Provides functions to convert btwn prefix to postfix

# Usage:
# Program requests user to input name of .txt file to be used as the program
# input. Program will output postfix expressions onto corresponding .txt files

# Test cases to consider:
# 1. No numerics - check
# 2. Excessive operands - check
# 3. Excessive operators - check
# 4. Remove spaces in lines of the input text file - check
# 5. Make sure program is run with exclusive variables ONLY: +, -, *, /, $, (, ) - check

import conversionFunctions
import stack
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py \"inputFile.txt\" \"outputFile.txt\"")
    sys.exit(1)

inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Reads the user specified .txt file from the user
# Separates and stores each prefix line in the file into array "inputLines"
with open(inputFile, "r") as file:
    inputLines = []  # Will store all input file lines separately
    for line in file:
        if len(line.strip()) == 0:
            continue
        else:
            # Removes all white space from input prefix expressions
            inputLines.append(line.strip())

# Outputs the postfix expressions on user specified .txt file
# Converts each prefix expression, from inputLines array, to infix to postfix
count = 0
# Writes introduction on output .txt file
with open(outputFile, "w") as file:  # Overwrites file content
        file.write("")
with open(outputFile, "a") as file:
        file.write("Prefix to Postfix conversions from Test Case file: "+ inputFile)
        file.write("\n")
        file.write("\n")
# Writes prefix and corresponding postfix expressions onto output .txt file
for line in inputLines:
    count += 1
    prefixLine = line.replace(" ","")
    with open(outputFile, "a") as file:
        file.write(str(count) + ". Given prefix expression: " + line)
        file.write("\n")
        file.write("Simplified prefix expression: " + prefixLine)
        file.write("\n")
    errorValue = conversionFunctions.checkPrefix(prefixLine)
    if errorValue == "A":
        postfixLine = "Error: Numerical character found in prefix expression."
    elif errorValue == "B":
        postfixLine = "Error: Prefix expression holds special characters."
    elif errorValue == "C":
        postfixLine = "Error: Prefix expression contains excessive operands."
    elif errorValue == "D":
        postfixLine = "Error: Prefix expression contains excessive operators."
    else:
        # Prefix to Infix
        infixLine = conversionFunctions.prefixToInfix(prefixLine)
        # Infix to Postfix
        postfixLine = conversionFunctions.infixToPostfix(infixLine)
        # Outputs prostfix expressions
    with open(outputFile, "a") as file:
        file.write("Converted postfix expression: " + postfixLine)
        file.write("\n")
        file.write("\n")
