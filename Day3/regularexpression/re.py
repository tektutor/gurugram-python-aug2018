#!/usr/bin/python

import re

'''
   123-456-9897
   127.456.9898
   (127).(456).(9898)
   (127)-(456)-(9898)
   (127)(456)(9898)
'''

def extractMobileDirectoryNumber( filename ):
    file = open ( filename, 'r' )
    content = file.read()
    file.close()

    #pattern = re.compile(r'(\d{3}(-|.)?\d{3}(-|.)?\d{4}|\(\d{3}\)(-|.|)?\(\d{3}\)(-|.|)? (\d{4}\))') 
    pattern = re.compile(r'((\d{3}(-|.)?\d{3}(-|.)?\d{4})|\(\d{3}\)(-|.|)?\(\d{3}\)(-|.|)? (\d{4}\))') 
    contacts = re.finditer( pattern, content )

    for mobile in contacts:
       print mobile.group(0)


def extractEmailIDs( filename ):

    file = open ( filename, 'r' )
    content = file.read()
    file.close()

    pattern = r'[a-zA-Z0-9.+-_]+@[a-zA-Z0-9.+-_]+.\w+'

    emails = re.findall ( pattern, content )

    for item in emails:
       print item 

#extractEmailIDs( 'emails.txt' )
extractMobileDirectoryNumber( 'contacts.txt' )
