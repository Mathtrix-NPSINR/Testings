import csv
from pathlib import Path

import requests

API_URL = "http://20.219.141.225:8000/api"

files = [
    "Agon.csv",
    "Apollo.csv",
    "Auctus.csv",
    "Enigmata.csv",
    "Mask A Raid.csv",
    "Mercatus.csv",
    "Nemesis.csv",
    "Saturn.csv",
    "Sonneto.csv",
    "Sum it Up!.csv",
    "Breaking Barriers.csv",
    "Cognitoria.csv",
    "Forum Infinitum.csv",
    "Hacksquads.csv",
    "Mathletics.csv",
    "Mathopoly.csv",
    "Mystifiezzeria.csv",
    "Operation Breakout.csv",
    "Picstraction.csv",
    "Rhythmatics.csv",
]


api_key = input("API KEY: ")


for event_id, filename in enumerate(files, start=1):
    print(f"{event_id}: {filename}\n\n")

    with open(
        Path("/Users/hari/Downloads/registrations/").joinpath(filename), "r"
    ) as file:
        reader = csv.reader(file)
        header = next(reader)

        for team in reader:
            if team is None:
                continue

            print(team[1])

            team_data = {
                "team_school": team[1],
                "team_event": Path(filename).stem,
                "event_id": event_id,
            }
            team_id = requests.post(
                f"{API_URL}/team", params={"api-key": api_key}, json=team_data
            ).json()["id"]

            participants = [
                j
                for j in [
                    list(filter(None, team[2:]))[i : i + 3]
                    for i in range(0, len(team[2:]), 3)
                ]
                if j
            ]

            for participant in participants:
                print(
                    requests.post(
                        f"{API_URL}/user/",
                        params={"api-key": api_key},
                        json={
                            "user_name": participant[0],
                            "user_email": participant[1],
                            "user_phone": participant[2],
                            "user_school": team[1],
                            "team_id": team_id,
                        },
                    ).json()
                )

            print()
