#!/usr/bin/python
# Global varaibles - considered as bad coding practice
filename = 'out.txt'
fileWriter = open ( filename, 'a+' )
msg = 'Line '

def readCount( ):
    fileReader  = open ( filename, 'r' )
    tokens = []
    for line in fileReader:
        tokens = line.split()
    fileReader.close()

    count = len(tokens)

    if ( count == 0 ):
        return 0

    count = int ( tokens[1] )

    return count


def createFile( ):
    count = readCount() + 1 

    print (count)

    for index in range(5):
        writeLine (count)
        count = count + 1

    fileWriter.close()

def writeLine( count ):
    fileWriter.write ( msg + str ( count ) + '\n' )

def main():
    createFile ( )

main()
