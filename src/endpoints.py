import requests
import json
from urllib.parse import urljoin 

def get_sporting_events(game_id: int,access_token: str):
    BASE_URL = 'https://api-ss-sandbox.betprophet.co' 
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
        print("Success! Sport Events:")
        return response.json()
    else:
        print(f"Failed: Status Code {response.status_code}")
        print(response.text)
