#Deposit Subprocess
import requests
import random
import time
from variable import auth_key, dep_channel
from datetime import datetime

while True:
    payload = {
        'content': '!dep all'
    }
    header = {
        'authorization': auth_key
    }
    r = requests.post(dep_channel, data=payload, headers=header)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"!dep at : {current_time}")
    time.sleep(random.randrange(600, 800))