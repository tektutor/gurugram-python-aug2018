#!/usr/bin/python

import sys

def main():

    numbers = [ 10, 20, 60, 30, 10, 40, 50 ]

    print ("List elements are ...")
    for x in numbers:
        print ( x )

    print ("Reversed list elements are ...")
    numbers.reverse()
    for x in numbers:
        print ( x )

    #Slicing
    print ('Current list')
    print ( numbers )
    print ( numbers[-2:] )

    print ( numbers[1:3] )

    #Sorting

    numbers.sort()
    print ( numbers )

    numbers.append( 60 )
    print ( 'list after appending 60 ...' )
    print ( numbers )

    print ( 'Size of list ' + str ( len ( numbers ) ) )

    print ( 'Bytes utilized by the list is ', sys.getsizeof( numbers ) );
    print ( 'Bytes utilized by the one int in list is ', sys.getsizeof( numbers[0] ) )

    print ( '60 appears ' + str ( numbers.count( 60 ) ) + ' times.' )

    numbers.remove( 60 )

    print ( numbers )

    del numbers 

    #print ( numbers ) - This will fail if uncommented as list is deleted

    l1 = [100, 200, 300]
    l2 = [400, 500, 600]

    l3 = l1 + l2 

    print ( l3 )




main()
