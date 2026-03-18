import requests
import time

def fetch_api_data(url, headers=None, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            time.sleep(2)
    raise Exception("API failed after retries")
