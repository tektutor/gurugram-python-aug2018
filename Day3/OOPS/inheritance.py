#!/usr/bin/python

class Parent:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setValues(self, val1, val2):
        self.__x = val1
        self.__y = val2

    def printValues(self):
        print ('Value of x is ', self.__x )
        print ('Value of y is ', self.__y )

class Child(Parent):

    def __init__(self, x=0, y=0, z=0):
        Parent.__init__(self,x, y)
        self.__z = z

    def setValues(self, val1, val2, val3):
        Parent.setValues(self, val1, val2 )
        self.__z = val3

    def printValues(self):
        Parent.printValues(self)
        print ('Value of z is ', self.__z )

def main():
    obj = Child(10,20,30)
    obj.printValues()

main()
