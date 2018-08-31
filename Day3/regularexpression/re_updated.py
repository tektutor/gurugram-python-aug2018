import re

'''
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
user.name@example.com
'''

def extractEmailIDs():
    file = open ( 'emails.txt', 'r' )
    content = file.read()
    file.close()

    #print ( content )

    pattern = re.compile( r'[a-zA-Z0-9.+-_]+@\w+?\+?\.?\w+?\.\w+' )

    matches = pattern.finditer ( content )

    for match in matches:
        print(match.group(0))

def extractURLs():
    file = open ( 'urls.txt', 'r' )
    content = file.read()
    file.close()

    pattern = re.compile( r'http://www.\w+\.\w+' )

    matches = pattern.finditer ( content )

    for match in matches:
        print ( match.group(0) )

def extractMDNs():
    file = open ( 'contacts.txt', 'r' )
    content = file.read()
    file.close()

    pattern = re.compile( r'(\d{3}(-|.)?\d{3}(-|.)?\d{4}|\(\d{3}\)(-|.|)?\(\d{3}\)(-|.|)?\(\d{4}\))' )

    matches = pattern.finditer ( content )

    for match in matches:
        print ( match.group(0) )


extractEmailIDs()
extractURLs()
extractMDNs()
