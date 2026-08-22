import json


DESCRIPTIONS = {
    "r1": "A cozy family-run trattoria with hand-rolled pasta and a wood-fired oven.",
    "r2": "Classic Roman cooking in a candlelit dining room, known for cacio e pepe.",
    "r3": "Serene sushi counter with a seasonal omakase and a quiet garden terrace.",
    "r4": "Bustling ramen bar famous for its 12-hour tonkotsu broth and short queue.",
    "r5": "Lively taqueria with street-style tacos, fresh salsas, and 40 mezcals.",
    "r6": "Fragrant North Indian curries, clay-oven breads, and a deep vegetarian menu.",
    "r7": "Intimate French bistro serving duck confit and a well-chosen Burgundy list.",
    "r8": "Casual American grill house with dry-aged steaks and generous shared sides.",
}


def lambda_handler(event, context):
    print("EVENT:", json.dumps(event, default=str))
    restaurant_id = event.get("restaurant_id", "")

    description = DESCRIPTIONS.get(restaurant_id)
    if description is None:
        result = {"error": f"No restaurant with id {restaurant_id}."}
    else:
        result = {
            "restaurant_id": restaurant_id,
            "description": description,
        }

    return result
