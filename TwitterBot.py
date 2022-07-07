# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 10:58:43 2022

Twitter Bot

@author: Chris
"""

import tweepy

#API KEYS
consumer_key = []
consumer_secret = []
access_token = []
access_token_secret = []




#Import keys from file
storage = str()
toggle = 0

text = open('twitter_keys.txt', 'r')
for line in text.readlines():
    line = line.replace(" ",'')
        
    for letter in line:
        if toggle == 1:
            storage += letter
        elif letter == "=":
            toggle = 1
    toggle = 0        
    
for letter in storage:
    if letter == "\n":
        toggle += 1
    elif toggle == 0:
        consumer_key += letter
    elif toggle == 1:
        consumer_secret += letter
    elif toggle == 2:
        access_token += letter
    elif toggle == 3:
        access_token_secret += letter

consumer_key[:] = [''.join(consumer_key[1:-1])]
consumer_secret[:] = [''.join(consumer_secret[1:-1])]
access_token[:] = [''.join(access_token[1:-1])]
access_token_secret[:] = [''.join(access_token_secret[1:-1])]

text.close()




#API data
auth = tweepy.OAuthHandler(consumer_key[0], consumer_secret[0])
auth.set_access_token(access_token[0], access_token_secret[0])

# Create API object
api = tweepy.API(auth)


def authenticate():
    if not api.verify_credentials():
        print('Authentication: FAILED')
        return False
    else:
        print('Authentication: OK')
        return True


def tweet():
    # If authenticate returns true, execute the following
    if authenticate():
        # Calls the API to tweet the following
        api.update_status('Hello World!')
        print('Tweet has been sent!')
    # If authenticate returns false, print the following
    else:
        print('Tweet has not been sent.')

if __name__ == "__main__":
    tweet()


