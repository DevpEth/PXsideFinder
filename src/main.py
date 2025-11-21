import argparse
import requests
import json
from urllib.parse import urljoin 
from src.endpoints import get_sporting_events

from src import mm_calls
from src.log import logging

if __name__ == '__main__':
    logging.info("testing MM api")

    mm_instance = mm_calls.MMInteractions()
    mm_instance.mm_login()
    mm_instance.get_balance()
    
    access_token = mm_instance.mm_session["access_token"]

    sporting_events = get_sporting_events(132, access_token)

    if sporting_events:
        
        print(json.dumps(sporting_events, indent = 4))  
    else:
        logging.error("Failed to fetch sporting events")
    
    all_nba_games = []

    