# Dependencies and Setup
import numpy as np

import json
import time
from apiCallObjects import topOneHundred
from apiCallObjects import attributesObject
from apiCallObjects import apiCallObjects
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint

# function to flatten json object

'''

# get top 100 playlist
url3 = "https://api.spotify.com/v1/playlists/4hOKQuZbraPDIfaGbM3lKI"

# get a song
url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQBRbZjpQkaZf2LswzNHUbpu5T4_xJIrDS34vcIygRGLq0cnbMqb1XBjguzOEi29xLLlAQDqtDSLLjxSMMO56kLqxkf_wCdlhzsVkuh906uh57_dEXMDBfw32hcnJG_mJjKMxPUIi8o'}

req = requests.get(url3, headers=headers)
jreq = req.json()
#print(jreq)

topAttributes = []

for i in range(100):
    val = jreq['tracks']['items'][i]['track']['id']
    #print(val)
    url4 = "https://api.spotify.com/v1/audio-features/" + val
    attributeRequest = requests.get(url4, headers=headers)
    jsonAttributeRequest = attributeRequest.json()
    #print(json.dumps(jsonAttributeRequest, indent=4, sort_keys=True))
    topAttributes.append(jsonAttributeRequest)

print(topAttributes)

attributesFrame  = pd.DataFrame(topAttributes)
#print(attributesFrame)


'''

'''print(topOneHundred)






