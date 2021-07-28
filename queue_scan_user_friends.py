import requests
import os

URL = os.environ["AUTO_TWEET_API_URL"]
internal_key = os.environ["INTERNAL_KEY"]
response = requests.get(URL + "/api/v1/queue_scan_user_friends", headers={"Authorization": internal_key})

print(f"RESPONSE: {response.status_code} | {response.text}")