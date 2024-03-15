#Slut Subprocess
import requests
import time
from variable import auth_key, slut_channel
from datetime import datetime

while True:
    payload = {
        'content': '!slut'
    }
    header = {
        'authorization': auth_key
    }
    r = requests.post(slut_channel, data=payload, headers=header)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"!slut at : {current_time}")
    time.sleep(182)