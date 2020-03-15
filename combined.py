
# Dependencies and Setup
import numpy as np
import requests
import json
import time
import requests
import pandas as pd
import numpy as np


from pandas.io.json import json_normalize
from pprint import pprint
from apiCallObjects import topOneHundred
from apiCallObjects import attributesObject
from apiCallObjects import compiledAPIcall

response_list = compiledAPIcall
popularity =[]
jreq = topOneHundred
for response in jreq['tracks']['items']:
    p = response['track']['popularity']
    popularity.append(p)
#print(popularity)

results_df = pd.DataFrame(response_list)
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.max_seq_items = None
danceability = [item["danceability"] for  item in attributesObject ]
results_df['danceability'] = danceability

results_df['energy'] = [item["energy"] for  item in attributesObject ]
results_df['key'] = [item["key"] for  item in attributesObject ]
results_df['loudness'] = [item["loudness"] for  item in attributesObject ]
results_df['mode'] = [item["mode"] for  item in attributesObject ]
results_df['speechiness'] = [item["speechiness"] for  item in attributesObject ]
results_df['acousticness'] = [item["acousticness"] for  item in attributesObject ]
results_df['instrumentalness'] = [item["instrumentalness"] for  item in attributesObject ]
results_df['liveness'] = [item["liveness"] for  item in attributesObject ]
results_df['valence'] = [item["valence"] for  item in attributesObject ]
results_df['tempo'] = [item["tempo"] for  item in attributesObject ]
results_df['duration_ms'] = [item["duration_ms"] for  item in attributesObject ]
results_df['time_signature'] = [item["time_signature"] for  item in attributesObject ]

print(results_df["response"])

pprint(results_df.head())



