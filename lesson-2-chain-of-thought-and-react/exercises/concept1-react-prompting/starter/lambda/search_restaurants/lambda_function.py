import json


RESTAURANTS = [
    {"id": "r1", "name": "Trattoria Bella", "cuisine": "Italian",  "rating": 4.6},
    {"id": "r2", "name": "Osteria Romana",  "cuisine": "Italian",  "rating": 4.4},
    {"id": "r3", "name": "Sakura Garden",   "cuisine": "Japanese", "rating": 4.7},
    {"id": "r4", "name": "Ramen Yuki",      "cuisine": "Japanese", "rating": 4.9},
    {"id": "r5", "name": "El Mercado",      "cuisine": "Mexican",  "rating": 4.3},
    {"id": "r6", "name": "Spice Route",     "cuisine": "Indian",   "rating": 4.6},
    {"id": "r7", "name": "Le Bistro",       "cuisine": "French",   "rating": 4.8},
    {"id": "r8", "name": "The Grill House", "cuisine": "American", "rating": 4.2},
]


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event, default=str))
    parameters = {p["name"]: p["value"] for p in event.get("parameters", [])}
    cuisine = parameters.get("cuisine", "").lower()

    if cuisine:
        restaurants = [r for r in RESTAURANTS if r["cuisine"].lower() == cuisine]
        if not restaurants:
            result = {"error": f"No {cuisine.title()} restaurants found."}
        else:
            result = {"restaurants": restaurants}
    else:
        result = {"restaurants": RESTAURANTS}

    return result
