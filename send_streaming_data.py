import requests
import time
import random

url = "YOUR_POWER_BI_PUSH_URL"

while True:
    data = [{
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "value": random.randint(10, 100)
    }]
    requests.post(url, json=data)
    time.sleep(2)