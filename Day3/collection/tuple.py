#!/usr/bin/python

def main():
   #Tuple collection class is immutable(read only) unlike list
    t = ( 10, 20, 30 )

    for item in t:
        print ( item )

    print ( t )

    del t 
    # print t - This will fail if uncommented as tuple is deleted

main()
