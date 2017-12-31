import string

def doTrans(word, alphabet, code):
    
    translatedString = str.translate(word, str.maketrans(alphabet, code))
    return translatedString

def encodeMessage(S, code):
    myList = []
    alphabet = string.ascii_lowercase
    for i in S:
        myList.append(doTrans(i, alphabet, code))
    return myList

def decodeMessage(word, code):
    
    alphabet = "abcdefghijklmnopqrstupwxyz"
    print(doTrans(word, alphabet, code))

word = "paul"
code = "bcdefghijklmnopqrstuvwxyza"

decodeMessage(word, code)

