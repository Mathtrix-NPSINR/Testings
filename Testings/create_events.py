import requests

API_URL = "http://20.219.141.225:8000/api"
# API_URL = "http://0.0.0.0:8000/api"
api_key = input("API Key: ")

events = [
    "Agon",
    "Apollo",
    "Auctus",
    "Enigmata",
    "Mask A Raid",
    "Mercatus",
    "Nemesis",
    "Saturn",
    "Sonneto",
    "Sum it Up!",
    "Breaking Barriers",
    "Cognitoria",
    "Forum Infinitum",
    "Hacksquads",
    "Mathletics",
    "Mathopoly",
    "Mystifiezzera",
    "Operation Breakout",
    "Picstraction",
    "Rhythmatics",
]


for event in events:
    requests.post(
        f"{API_URL}/event/", params={"api-key": api_key}, json={"event_name": event}
    )
