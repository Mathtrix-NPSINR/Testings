#  Copyright (c) 2023 Harikeshav R
#  All rights reserved.

import csv
from pathlib import Path

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

consolidated_file = open(Path("/Users/hari/Downloads/registrations").joinpath("Consolidated.csv"), "w", newline='')

writer = csv.writer(consolidated_file)

for event_id, filename in enumerate(files, start=1):
    with open(
            Path("/Users/hari/Downloads/registrations/").joinpath(filename), "r"
    ) as file:
        writer.writerow([filename.replace(".csv", "")])

        reader = csv.reader(file)

        for record in reader:
            writer.writerow(record)

        writer.writerow([])
