#!/usr/bin/env python3
"""
Module that makes use of the Spotify Web API to retrieve pseudo-random songs based
or not on a given exiting Spotify genre (look at genres.json, filled with info
scrapped from http://everynoise.com/everynoise1d.cgi?scope=all&vector=popularity)
"""

import sys
import json
import re
import requests
import base64
import urllib
import random
import time



# Spotify API URIs

SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)





def request_valid_song(access_token, genre=None):
    # Wildcards for random search
    randomSongsArray = ['%25a%25', 'a%25', '%25a',
                        '%25e%25', 'e%25', '%25e',
                        '%25i%25', 'i%25', '%25i',
                        '%25o%25', 'o%25', '%25o',
                        '%25u%25', 'u%25', '%25u']
    randomSongs = random.choice(randomSongsArray)
    # Genre filter definition
    if genre:
        genreSearchString = " genre:'{}'".format(genre)
    else:
        genreSearchString = ""
    # Upper limit for random search
    maxLimit = 2000


    randomOffset = random.randint(1, maxLimit)
    authorization_header = {
                "Authorization": "Bearer {}".format(access_token)
            }
    song_request = requests.get(
                "{}/search?query={}&offset={}&limit=1&type=track".format(
                    SPOTIFY_API_URL,
                    randomSongs + genreSearchString,
                    randomOffset
                ),
                headers=authorization_header
            )
    time.sleep(1)
    jreq = song_request.json()
    song_info = json.loads(song_request.text)['tracks']['items'][0]
    #artist = song_info['artists'][0]['name']
    song = song_info['name']
    id = song_info['id']
    return {song : id}







def main():
    args = sys.argv[1:]
    n_args = len(args)
    songs = []
    for i in range(100):
        if n_args > 1:
            print('usage: py ./random_song.py [genre]')
            sys.exit(1)
        else:
            access_token = 'BQA__orK1HthsKeGOOIVYIxwME7mts-fxkwybd2PvR7tl8x5VXTcEDqZZzD-umCnZVVFQdiKJmIveB3A9_dMbIq9u-ftRa9vdz1Yf0SXBKhdSB-LDZzQnMzWNZF6ro65YrEuipyDi6s'

            if n_args == 0:
                result = request_valid_song(access_token)
            else:
                selected_genre = (re.sub('[^a-zA-Z0-9]', '', args[0])).lower()
                # Fix for 'Trap' genre based on some suggestions
                if (selected_genre == 'trap'):
                    selected_genre = 'traplatino'
                try:
                    with open('genres.json', 'r') as infile:
                        valid_genres = json.load(infile)
                except FileNotFoundError:
                    print("Couldn't find genres file!")
                    sys.exit(1)

                if selected_genre in valid_genres:
                    result = request_valid_song(access_token, genre=selected_genre)
                else:
                    result = request_valid_song(access_token)

            songs.append(result)

    print(songs)

if __name__ == '__main__':
    main()
