# Dependencies and Setup
import numpy as np

import json
import time

import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint

# function to flatten json object

'''
def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out
    
'''

# get top 100 playlist
url3 = "https://api.spotify.com/v1/playlists/4hOKQuZbraPDIfaGbM3lKI"

# get a song
url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQBUXlwycB1ebzum_uqLdplaohXd0sqzqdPdPZULKl4_-4jKAIZFS7EuDZtkRmyPl2FwQcAuEU3HOsfKUDv_DS_k5H7gM6dgo5tQKRdy49C9VmZxrmLk7IYc-iqvDAZVc5NO4TFHPc0'}

# call api for top 100
req = requests.get(url3, headers=headers)
jreq = req.json()
print(jreq)

#print(json.dumps(jreq, indent=4, sort_keys=True))

'''
f = flatten_json(jreq)

data = pd.DataFrame(json_normalize(f))
# make rows into columns so it's easier to read
data = data.transpose()
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#    print(data)
# First element is general information, second is countries themselves
#val = countries_response[1][26]['name']
#print(val)
'''
val = jreq['tracks']['items'][93]['track']['id']
print(val)




