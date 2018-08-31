#!/usr/bin/python

class Employee:

    def __init__(self, name='', id=0, designation=''):
        self.name = name
        self.id = id
        self.designation = designation

    def __privateMethod__(self):
        print ('Private Method')

    def _protectedMethod__(self):
        print ('Protected Method')

    def setDetails(self, name, id, designation ):
        self.name = name
        self.id = id
        self.designation = designation

    def printDetails(self):
        print ( 'Name        : ' + self.name )
        print ( 'ID          : ' + str(self.id) )
        print ( 'Designation : ' + self.designation )
        self.__privateMethod__()

def main():
    rishi = Employee( 'Rishi Kumar', 1000, 'Technical Expert' )
    #rishi.setDetails ( 'Rishi Kumar', 1000, 'Technical Expert' )
    rishi.printDetails ( )

    arun = Employee( 'Arun KR', 2000, 'Program Manager' )
    #arun.setDetails ( 'Arun KR', 2000, 'Program Manager' )
    arun.printDetails ( )

    rishi.printDetails()
    rishi._protectedMethod__()

    dummyEmployee = Employee()
    dummyEmployee.printDetails()

   # rishi.__privateMethod__() - Can't be accessed outside the Employee object

main()
