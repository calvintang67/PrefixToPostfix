# Name: Calvin Tang

# conversionFunctions.py
# This module contains functions to convert prefix expressions to postfix
# The stack.py module is imported to define these functions using Stack ADT

# Functions:
# checkPrefix(prefix): Checks prefix for test case errors
#     A. No numerical characters
#     B. Exclusive operators: +, -, *, /, $, (, )
#     C. Excessive operands
#     D. Excessive operators
# prefixToInfix(prefix): Converts prefix expression to infix
# infixToPostfix(infix): Converts infix expression to postfix

import stack

exclusiveSymbols = ["+", "-", "*", "/", "$", "(", ")"]

# Function: Checks prefix for test case errors
# Input: prefix expression "prefix" string, Output: 'Error value'
def checkPrefix(prefix):
    operandStack = stack.Stack()
    operatorStack = stack.Stack()
    for char in prefix:
        if char.isalpha():
            operandStack.push(char)
        elif char.isdigit():
            return "A"  # Fail, numerical characters included in expression
        elif char not in exclusiveSymbols:
            return "B"  # Fail, expression does not use exclusive operators
        else:
            operatorStack.push(char)
    # Prefix expressions must have one more operand than operator
    operandSize = operandStack.getLength()
    operatorSize = operatorStack.getLength()
    if operandSize-operatorSize == 1:
        return "P"  # Pass
    elif operandSize-operatorSize > 1:
        return "C"  # Fail, expression holds excessive number of oeprands
    else:
        return "D"  # Fail, expression holds excessive number of operators

# Function: Convert a prefix expression to infix
# Input: prefix expression "prefix" string, Output: infix expression string
def prefixToInfix(prefix):
    stackObj = stack.Stack()
    for char in reversed(prefix):
        if char.isalpha():
            stackObj.push(char)
        # Prefix to Infix conversion
        else:
            operand1 = stackObj.pop()
            operand2 = stackObj.pop()
            newStackPush = "("+ operand1 + char + operand2 + ")"
            stackObj.push(newStackPush)
    return stackObj.pop()

# Function: Convert a infix expression to postfix
# Input: infix expression "infix" string, Output: postfix expression string
def infixToPostfix(infix):
    operandStack = stack.Stack()
    operatorStack = stack.Stack()
    for char in infix:
        if char.isalpha():
            operandStack.push(char)
        else:
            if char != ")":
                operatorStack.push(char)
            # Infix to postfix conversion
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                newStackPush = operand1 + operand2 + operatorStack.pop()
                operatorStack.pop()
                operandStack.push(newStackPush)
    return operandStack.pop()