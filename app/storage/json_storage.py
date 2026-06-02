import json
from pathlib import Path


file_path = Path("data") / "activities.json"


def load_activities():

    with open(file_path, "r", encoding="utf-8") as file:
        activities = json.load(file)
    return activities


def save_activities(activities):

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(activities, file,ensure_ascii=False, indent=4)


def add_activity(activity):

    new_activities = load_activities()
    new_activities.append(activity)
    save_activities(new_activities)
