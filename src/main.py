import argparse

from src import mm_calls
from src.log import logging
import time 
import requests
import json
from urllib.parse import urljoin # You can use this to build the URL cleanly




if __name__ == '__main__':
    logging.info("testing MM api")

    mm_instance = mm_calls.MMInteractions()
    mm_instance.mm_login()
    mm_instance.get_balance()


    '''
    #print(mm_instance.mm_session['access_token'])


    BASE_URL = 'https://api-ss-sandbox.betprophet.co' 
    ENDPOINT = '/partner/mm/get_sport_events'

    # Get this from your successful mm_login call
    ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJjMmY1NWFlYi04NWRmLTQ3YjEtOGQ5MC1kOThmOTc5ZDI0MTYiLCJleHAiOjE3NjM2ODYwNDQsImlhdCI6MTc2MzY4NDg0NCwicGFydG5lclR5cGUiOiJtbWkiLCJwYXJ0bmVySUQiOiJkZGViZWIzMS1jYTE2LTRiNzMtOWI1ZC0xZjJmNzQ0ZGY2MzIiLCJ0eXBlIjoiYWNjZXNzIiwiYWNjZXNzS2V5IjoiOTBjOWNiNWQ0YTI1NTEzN2ZkNTI1MjEwYjdjOGQzYWQiLCJnZW9jb21wbHlWZXJpZmllZFRpbWVzdGFtcCI6IjIwMjUtMTEtMjBUMjE6MzE6MTkuMzU1WiJ9.BZrm08wCAOSj_b5-CiqZFJTei59OHSmLqqxP8d5P_uk' 
    TOURNAMENT_ID = 132

    # 1. Build the URL
    full_url = urljoin(BASE_URL, ENDPOINT)

    # 2. Define the Query Parameters
    query_params = {
        'tournament_id': TOURNAMENT_ID
    }

    # 3. Define the Authorization Header
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }

    # 4. Make the GET Request
    response = requests.get(full_url, params=query_params, headers=headers)

    if response.status_code == 200:
        print("Success! Sport Events:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Failed: Status Code {response.status_code}")
        print(response.text)
    '''