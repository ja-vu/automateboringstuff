"""
*************************
*                       *
*                       *
*************************
"""

import traceback


def boxPrint(symbol,width,height):
    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')
    if (width < 2) or (height <2):
        raise Exception('"Width" and "height" must be greater or equal to 2.')
    print(symbol * width)

    for i in range (height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)
import traceback

try:
    raise Exception("This is the error message.")
except:
    errorFile = open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written in error_log.txt")


boxPrint('L', 1, 1)
boxPrint('**', 5, 16)

