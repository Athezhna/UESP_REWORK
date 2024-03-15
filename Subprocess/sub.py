#Work Subprocess
import requests
import time
from variable import auth_key, work_channel
from datetime import datetime

while True:
    payload = {
        'content': '!work'
    }
    header = {
        'authorization': auth_key
    }
    r = requests.post(work_channel, data=payload, headers=header)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"!work at : {current_time}")
    time.sleep(32)