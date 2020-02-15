import main as mp
from time import sleep
import random

# countries.txt is a file with countries (in their possesive adjective form)
countryFile = open("countries.txt", "r")
countryString = countryFile.read()
countryFile.close()
countryList = countryString.split(',')

# nouns.txt is a file with some commonly used nouns
nounFile = open("nouns.txt", "r")
nounString = nounFile.read()
nounFile.close()
nounList = nounString.split('\n')

tb = mp.TwitterBot()
# login with second account (different account from your scrape.py file), for example
tb.loginTwitter(1)

# time between posts, current = 1day
timeBetweenSend = 60 * 60 * 24

while True:
    rnd1 = random.randint(0, len(countryList))
    rnd2 = random.randint(0, len(nounList))
    tb.post(countryList[rnd1] + ' ' + nounList[rnd2])
    sleep(timeBetweenSend)
