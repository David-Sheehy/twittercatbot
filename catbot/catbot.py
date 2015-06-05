#! /usr/bin/env python3
# config, the access key and secret, the computer key and secret, and the time
# between running.
from config import  ACCESS_KEY, ACCESS_SECRET,CONSUMER_KEY, CONSUMER_SECRET, TIME_DELAY
from twitter import *
import random

# various constants
PURR = "purr"
RESPONSES_GOOD = ['meow', 'Nya', 'MEOW', '=^.^=', PURR]
RESPONSES_BAD = ['HISS!', '*scratch*']

# open the account
t = Twitter(auth=OAuth(ACCESS_KEY,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET))

# get recent messages

# print a status message
t.statuses.update(status=random.choice(RESPONSES_GOOD))
# go back to sleep
