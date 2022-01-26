from string import *
from random import *

lowercase   = string.ascii_lowercase # [abc...z]
uppercase   = string.ascii_uppercase # [ABC...Z]
numbers     = string.digits          # [0123..9]
punctuation = string.punctuation     # punctuations like : !/=+#....
inputPool = lowercase + uppercase + numbers + punctuation

def generateString(inputlength):
    passList = sample(inputPool,inputlength)
    password = ""
    for x in passList:
        password += x
    return password

