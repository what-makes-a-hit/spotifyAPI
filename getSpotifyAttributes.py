# Dependencies and Setup
import numpy as np

import json
import time

import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint

# function to flatten json object



# get top 100 playlist
url3 = "https://api.spotify.com/v1/playlists/4hOKQuZbraPDIfaGbM3lKI"

# get a song
url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQDR1qCXN_HU-GaCxuC7f738blfyQld3bjRc8SmDqxgOcCjs1Aw_cuDllvSV65_KBjWYyWAYd9CUqiY3h5fJqJENjdgc92TtG7JEXfgOTVHAnhQ5ufErnCLLmPRXycBXQ16_oy7bOd8'}
# call api for top 100

req = requests.get(url3, headers=headers)
jreq = req.json()
#print(jreq)

topAttributes = []

for i in range(100):
    val = jreq['tracks']['items'][i]['track']['id']
    print(val)
    url4 = "https://api.spotify.com/v1/audio-features/" + val
    attributeRequest = requests.get(url4, headers=headers)
    jsonAttributeRequest = attributeRequest.json()
    print(json.dumps(jsonAttributeRequest, indent=4, sort_keys=True))
    topAttributes.append(jsonAttributeRequest)

print(topAttributes)







