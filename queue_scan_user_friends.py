import requests
import os

URL = os.environ["AUTO_TWEET_API_URL"]
response = requests.get(URL + "/api/v1/queue_scan_user_friends")

print(f"RESPONSE: {response.status_code} | {response.text}")