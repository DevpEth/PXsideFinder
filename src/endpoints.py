import requests
import json
from urllib.parse import urljoin 

BASE_URL = 'https://api-ss-sandbox.betprophet.co' 

def get_sporting_events(game_id: int,access_token: str):

    ENDPOINT = '/partner/mm/get_sport_events'

    full_url = urljoin(BASE_URL, ENDPOINT)

    query_params = {
    'tournament_id': game_id
    }

    headers = {
    'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(full_url, params=query_params, headers=headers)

    if response.status_code == 200:
        print('Success! Sport Events:')
        return response.json()
    else:
        print(f'Failed: Status Code {response.status_code}')
        print(response.text)

def auth_refresh(refresh_token: str):
    
    ENDPOINT = '/partner/auth/refresh'

    full_url = urljoin(BASE_URL, ENDPOINT)

    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    body = {
        "refresh_token": refresh_token
    }
    
    response = requests.post(full_url, headers=headers, json=body)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Auth refresh failed: {response.status_code}")
        print(response.text)
        return None
