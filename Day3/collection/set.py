#!/usr/bin/python

def main():

    l1 = [ 10, 20, 30 ]
    l2 = [ 10, 20, 30, 40, 50, 60 ]

    s = { 0 } 

    for item in l1:
        s.add ( item )

    for item in l2:
        s.add ( item )
    print ( s )

    s1 = { 1, 2, 3, 5, 4, 6 }
    s2 = { 2, 4, 6 }

    print ( s1.union( s2 ) )

    print ( "Print difference " )
    print ( s1.difference ( s2 ) )

    print ( "Subset " )
    print ( s2.issubset ( s1 ) )
    



main()
