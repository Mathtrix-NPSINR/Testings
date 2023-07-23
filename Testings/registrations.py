import random

import requests
from faker import Faker


API_URL = "http://20.219.141.225:8080/"
# API_URL = "http://0.0.0.0:8080/"


schools = ["NPS INR", "NPS KRM", "NPS HSR", "NAFL", "TISB"]

events = {
    "Agon": (2, "1C3nr44s7p3VNF_WHxWkKAaunQ1QvN-WcrwiKEYvUyNY"),
    "Apollo": (4, "10Fy406Lz0h7azBY3BYcKD82R2UnnxWCUjO4CvQwOl1k"),
    "Auctus": (2, "1utGuIQ8pyj9EYRmlNPl4q5xVgccCQEX94c_WJ9Gizzo"),
    "Enigmata": (2, "15qXV8Q-YLzfkWMOxbdKLkkHkEIyRJj0tpZQi8dvU3j8"),
    "Mask A Raid": (5, "1s7om5bwTshQWPsQE3f7OkDvXvAMOuvsM8jF1Xnp50YQ"),
    "Mercatus": (3, "1B5oP2MBaYZEjDPhw_IHroehbS7gV8hZhO79V-GaO0-Y"),
    "Nemesis": (3, "1GxPRC5T2npL-ablix1q8Dhi5Gy-3lXZelcNhsOplmDc"),
    "Saturn": (3, "1-Wo5IzWj26KzyQeZIR5511qELXnVw5ObJMJt8JXC1DU"),
    "Sonneto": (3, "19AiL7fX8DQBR4NaHoHARo0k40xeWSPeRUq1__HIoYM0"),
    "Sum it Up!": (4, "1ym1ce1LbFMHfFTiweFJWHd6dzc4-NMCUj-XNQLxtqOA"),
    "Breaking Barriers": (3, "1F3zPii3cI8_eJYC6-kkXmpQ4UPm2uv6cu9NAx7YbDRQ"),
    "Cognitoria": (2, "1369PReP12e8nXqP-VeOqs6V3BrwUTE1UfDoVU4UdTc0"),
    "Forum Infinitum": (3, "1tdmkxT4eqTqzMX03uvDCzbYP0iWbbN6oH-kn2ZyYQTM"),
    "Hacksquads": (1, "1gZTAg5N7GO1Ia6BAMPkyD9Kuxz59nQWKrF5Jf4WIiTA"),
    "Mathletics": (5, "1nAqaFo23NdtRS_HOWH0PVslkMo74JzU7dR3YkhgdvYg"),
    "Mathopoly": (2, "1mX-crEIcDtGcwnzmq-j1xAUVCysYl5s-nCon8Nuoirg"),
    "Mystifiezzera": (4, "1_0sFSIU1QEjHuKgtPGWBKn0wCS787Qq4IdsuyaHL4DI"),
    "Operation Breakout": (4, "1bQhHMnbJ3OjH2Rv_5GyWwmFYKAhud4Hz73ut0GNdZ5Y"),
    "Picstraction": (2, "1k2BH9lOvJwhFL63M-tLQDxDi--FkDAh898sdjhBKhco"),
    "Rhythmatics": (4, "1NiQ8pAxk-oFEp3otKuTT8oOj3IDrUcWeqTj7RrnL70k"),
}


fake = Faker()

for i in range(1000):
    event = random.choice(list(events.items()))
    data = {
        "form_id": event[1][1],
        "team_name": f"Team {fake.name()}",
        # "team_name": "hi",
        "school": random.choice(schools),
    }

    for i in range(1, event[1][0] + 1):
        fake_name = fake.name()
        data[f"name_{i}"] = fake_name
        data[f"email_{i}"] = ".".join(fake_name.strip().split()) + "@gmail.com"
        data[f"phone_number_{i}"] = str(random.randint(1000000000, 9999999999))

    print(requests.post(API_URL, json=data))
    print(data)
    print("-" * 100)
    print("\n")
