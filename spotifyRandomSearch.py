# Dependencies and Setup
import numpy as np

import json
import time
#from apiCallObjects import topOneHundred
#from apiCallObjects import attributesObject
#from apiCallObjects import compiledAPIcall
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint
import string
import random
import time

from random import seed
from random import randint
# seed random number generator
seed(7)


#function which generates a random search string
def getRandomSearch():


      #list of possible characters
      characters = 'abcdefghijklmnopqrstuvwxyz'

      #choose one randomly
      randomCharacter = random.choice(characters)

      #create a search query string
      randomSearch = ''

      #toss a coin
      coin = [0,1]

      toss = random.choice(coin)

      # Places the wildcard character at the beginning, or both beginning and end, randomly.
      if toss == 0:
          randomSearch = randomCharacter + '%'
      else:
          randomSearch = '%' + randomCharacter + '%'


      return randomSearch

# pick a number randomly less than 10000 as an offset


randomOffset = random.sample(range(0, 2000), 40 )
search = []
for i in range(40):

#type=track
      query = getRandomSearch()
      offset = randomOffset[i]
      #print(offset)

      url = 'https://api.spotify.com/v1/search?q=' + str(query) +  '&offset=' +str(offset) + '&type=track'
      print(url)
      headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQAViQRE_MCBe3q1ORbgoomCwhbXxGoEWYT0fV7L588mtItJ_dVeRnRXjjC9O5Ape_0sFchd2zOhEzM0Pi3jVXy5-UBV2McrJ-YvhOIO_o9FANGPAWtfYYuXCF4dYN68ysSstulDkqr0Am0SLVQwEVQoLUvMk4H-4ThCzRytKkOuteP9QOp9b0WOG841ilSmNyHMRQspZGVjX_NdAl7IKguQirZcg-MIUCkdkO5ku0CqsYnH3BqnWtaPAMX3M3T__L463CNe'}
      req = requests.get(url, headers=headers)
      print(req)
      jreq = req.json()
      id = jreq['tracks']['items'][0]['id']
      name = jreq['tracks']['items'][0]['name']
      res = {id, name}
      #search.append(res)
      #print(res)
      search.append(res)

      time.sleep(1)


print(search)
