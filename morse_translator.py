"""

File Name: morse_translator.py

Developer: Samuel Gordon

Date last modified: Sunday, November 25th 2012

Description: Asks the user for a phrase to translate, and then asks the user if they want
                to translate said phrase into morse code, or from morse code into alphanumeric characters.

email address: sam.gordon.vvc@gmail.com

"""
tomorse = {
    'a': '.-',      'b': '-...',    'c': '-.-.',    'd': '-..',
    'e': '.',       'f': '..-.',    'g': '--.',     'h': '....',
    'i': '..',      'j': '.---',    'k': '-.-',     'l': '.-..',
    'm': '--',      'n': '-.',      'o': '---',     'p': '.--.',
    'q': '--.-',    'r': '.-.',     's': '...',     't': '-',
    'u': '..-',     'v': '...-',    'w': '.--',     'x': '-..-',
    'y': '-.--',    'z': '--..',    '0': '-----',   '1': '.----',
    '2': '..---',   '3': '...--',   '4': '....-',   '5': '.....',
    '6': '-....',   '7': '--...',   '8': '---..',   '9': '----.',
    ',': '--..--',  '.': '.-.-.-',  '?': '..--..',  ';': '-.-.-.',
    ':': '---...',  "'": '.----.',  '-': '-....-',  '/': '-..-.',
    '(': '-.--.-',  ')': '-.--.-',  ' ': ' ',       '_': '..__._',
}

frommorse = dict((b,a) for a,b in tomorse.items())

text=input("Type a phrase to translate.\n").lower()
choice=input("Type 2 to translate from morse code. Type 1 to translate to morse code.")
value = ' '

for char in text:

    if choice == '1':
        value += tomorse[char] + ' '
    if choice == '2':
        value += frommorse[char] + ' '
value = value.rstrip()
print(value)