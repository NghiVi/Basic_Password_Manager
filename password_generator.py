import itertools
import string
import random

lowercase   = string.ascii_lowercase # [a-z]
uppercase   = string.ascii_uppercase # [A-Z]
numbers     = string.digits          # [0-9]
punctuation = string.punctuation     # punctuations like : !/=+#....

# lowercase and uppdercase should "theoretically" appear 2x more often in the password
inputPool = lowercase + uppercase + numbers + punctuation + uppercase + lowercase

def generateRandomString(inputlength):
    passList = random.sample(inputPool,inputlength)
    password = ""
    for x in passList:
        password += x
    return password

# Method for Testing password genration method
def printSample(count = 10, inputLength = 15):
    for _ in itertools.repeat(None,count):
        print(generateRandomString(inputLength))

#printSample()
