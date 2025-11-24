import time
import argparse
import requests
import json
from urllib.parse import urljoin 
from src.endpoints import get_sporting_events, auth_refresh

from src import mm_calls
from src.log import logging

if __name__ == '__main__':
    logging.info("testing MM api")

    mm_instance = mm_calls.MMInteractions()
    mm_instance.mm_login()
    mm_instance.get_balance()

    NBA_ID = 132
    
    access_token = mm_instance.mm_session["access_token"]
    refresh_token = mm_instance.mm_session["refresh_token"]


# ... inside your script ...

    refresh_response = auth_refresh(refresh_token)

    if refresh_response:
        new_access_token = refresh_response["data"]["access_token"]
        new_expire_time = refresh_response["data"]["access_expire_time"]
        
        # 1. Update your instance/session with the new token and time
        mm_instance.mm_session["access_token"] = new_access_token 
        mm_instance.mm_session["access_expire_time"] = new_expire_time

       
        print("Access token refreshed!")

    # get all nba games 
    sporting_events = get_sporting_events(NBA_ID, new_access_token)

    if sporting_events:
        
        print(json.dumps(sporting_events, indent = 4))  
    else:
        logging.error("Failed to fetch sporting events")

    print(new_access_token)

    