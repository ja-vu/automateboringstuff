"""
upper
lower
isupper
islower
isalpha
isalnum
isspace
istitle
title
startswith
endswith
"""
import pyperclip

spam = 'Hello World'
print(spam.upper())

spam = spam.upper()
print(spam)

print(spam.lower())

print("hello".islower())

print("hello".isalpha())

print("hello123".isalpha())

print("hello123".isalnum())

print("  ".isspace())

print("This Is Title Case".istitle())

print("hello world".title())

print("Hello World!".startswith("Hello"))

print("Hello World!".startswith("H"))

print("Hello World!".startswith("ello"))

print("Hello World!".endswith('World!'))

print(','.join(['cats','rats','bats']))

print('My name is Simon'.split())

print("My name is Simon".split('m'))

print('Hello'.rjust(10))

print('Hello'.ljust(20))

print('Hello'.rjust(15,'*'))

print('Hello'.ljust(30,'-'))

print("Hello".center(30, '='))

spam2 = "    Hello World! My Name is James"
print(spam2.strip('Name'))

print(spam2.replace('e',"LOL"))

pyperclip.copy("HELLO !@#!@#!@#")
pyperclip.paste()