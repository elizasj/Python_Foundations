import os
import urllib.request

def read_text():
    text = open('text.txt')
    contents = text.read()
    print(contents)
    text.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.request.urlopen('http://www.wdylike.appspot.com/?q='.format(text_to_check))
    output = connection.read()
    print(output)
    connection.close()

read_text()
