#!/usr/bin/python

def readCSVData( filename ):

    fileReader = open ( filename, 'r' )

    for record in  fileReader:
        tokens = record.split(';')
        for token in tokens:
            print ( token )

readCSVData('/home/jegan/Downloads/history_export_2018-08-30T09_22_20.csv')
