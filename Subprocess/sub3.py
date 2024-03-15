# Subprocess/sub.py

import requests
import time
from variable import auth_key, crime_channel
from datetime import datetime

while True:
    payload = {
        'content': '!crime'
    }
    header = {
        'authorization': auth_key
    }
    r = requests.post(crime_channel, data=payload, headers=header)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"!crime at : {current_time}")
    time.sleep(182)