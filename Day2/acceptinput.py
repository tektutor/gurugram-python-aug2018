#!/usr/bin/python

from secondfile import *

def acceptInput():

    firstValue = input ('Enter your first float number: ')
    secondValue = input ('Enter your second float number: ')

    print ( 'Type of firstValue is ' + str( type(firstValue) ) )

    return firstValue, secondValue

def addNumbers(firstNumber, secondNumber):
    return firstNumber + secondNumber

def main():

    x, y = acceptInput()

    print ( type ( x ) )
    print ( type ( y ) )
        
    result = addNumbers ( x , y ) 

    print ( 'The sum of ' + str(x) + ' and ' + str(y) + ' is ' + str(result) )

main()

'''
if __name__ == '__main__':
    print ( __name__ )
    main()
'''
