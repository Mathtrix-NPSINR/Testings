import requests

API_URL = "http://20.219.141.225:8000/api"
api_key = input("API Key: ")


for i in range(1, 21):
    requests.delete(f"{API_URL}/event/", params={"event_id": i, "api-key": api_key})
