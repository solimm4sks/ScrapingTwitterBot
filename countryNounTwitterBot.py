import main as mp
from time import sleep
import random

countryFile = open("ddone.txt", "r")
countryString = countryFile.read()
countryFile.close()
countryList = countryString.split(',')

nounFile = open("nouns.txt", "r")
nounString = nounFile.read()
nounFile.close()
nounList = nounString.split('\n')

tb = mp.TwitterBot()
tb.loginTwitter(1)

timeBetweenSend = 60 * 60 * 24

while True:
    rnd1 = random.randint(0, len(countryList))
    rnd2 = random.randint(0, len(nounList))
    tb.writeTextBox(countryList[rnd1] + ' ' + nounList[rnd2])
    sleep(timeBetweenSend)
