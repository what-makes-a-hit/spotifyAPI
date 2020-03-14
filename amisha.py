# Dependencies and Setup
import numpy as np

import json
import time
from apiCallObjects import topOneHundred
from apiCallObjects import attributesObject
from apiCallObjects import compiledAPIcall
import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint

'''
# get top 100 playlist
url3 = "https://api.spotify.com/v1/playlists/4hOKQuZbraPDIfaGbM3lKI"
# get a song
# url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQBZzeiNy830BN8tq_in9DHnbPq-Mqa__ZcL-Ta6imYgIQ5L6oT4MUe05dWxeTY8ewrVmYM9VKKusgJhSvvrAxCDjy6WVj33tNJzY36LGvz8CUn-FrX-_ZWNuWDJDGl57gqa4JUQlg56fcI8-xxTBE9jd0-0mM_jcOAZ0DDb8dhvxbBOchI7ZkTTbaZ6nGRmI6k_3VIfOaGyU0tINgtXZSEIsn1bjKIGkJLpEZsCtM54LleVhEWC3cyfm2xxIDVKfu08ek4o'}
req = requests.get(url3, headers=headers)
jreq = topOneHundred
response_list = []
track_name = ""
track_id = ""
for response in jreq['tracks']['items']:
    # retreive track details
    track_name = response["track"]["name"]
    track_id =  response["track"]["id"]
    # read data for analysis
    val = response['track']['id']
    url4 = "https://api.spotify.com/v1/audio-features/" + val
    response = requests.get(url4, headers=headers)
    j_response = response.json()
    # compile the results
    results = {"track_name" : track_name, "track_id": track_id, "response": j_response}
    response_list.append(results)

print(response_list)

'''

response_list = compiledAPIcall

results_df = pd.DataFrame(response_list)
print(results_df.head())
