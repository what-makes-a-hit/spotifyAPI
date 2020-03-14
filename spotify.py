# Dependencies and Setup
import numpy as np
import requests
import json
import time

# get top 100 playlist
url3 = "https://api.spotify.com/v1/playlists/4hOKQuZbraPDIfaGbM3lKI"

# get a song
url = "https://api.spotify.com/v1/audio-features/06AKEBrKUckW0KREUWRnvT"
headers = {'Accept': 'application/json', 'Content-Type' : 'application/json','Authorization': 'Bearer BQBUXlwycB1ebzum_uqLdplaohXd0sqzqdPdPZULKl4_-4jKAIZFS7EuDZtkRmyPl2FwQcAuEU3HOsfKUDv_DS_k5H7gM6dgo5tQKRdy49C9VmZxrmLk7IYc-iqvDAZVc5NO4TFHPc0'}

# call api for top 100
req = requests.get(url3, headers=headers)
jreq = req.json()
print(jreq)

