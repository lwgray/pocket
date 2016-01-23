# Author: Lawrence Gray <lwgray at gmail.com>
# License: BSD 3 clause
# Python 2.7 
'''
Gets DATA from pocket
Requires pocket ('https://github.com/tapanpandita/pocket/')
Python 2.7 

Usage: python get_pocket_data.py
Output: 'training_data.p' - pickle file containing list of dicts

You must have access to Pocket API (getpocket.com/developers)
'''

from pocket import Pocket
import os
import pickle


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')  # Provided by POCKET(see above)
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')  # Generate an access key for yourself
TRAINING = []
TEST = []

# Access pocket DATA and define the type of DATA to return
USER_DATA = Pocket(CONSUMER_KEY, ACCESS_TOKEN)
ARTICLES = USER_DATA.get(state=all, contentType='article', detailType='simple')

# split DATA into TRAINING and TEST sets
DATA = [{key: value} for key, value in ARTICLES[0]['list'].items()]
SIZE = len(DATA)

for index, value in enumerate(DATA):
    if index < (SIZE * 0.60):  # 60% of DATA to be used for TRAINING
        TRAINING.append(value)
    else:
        TEST.append(value)  # 40% of DATA to be used for TEST

# save data to pickle files - Pickle files should not be used in production code
with open('training_data.p', 'wb') as data:
    pickle.dump(TRAINING, data)

with open('testing_data.p', 'wb') as data:
    pickle.dump(TEST, data)

