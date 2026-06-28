import os
import json
import time
import requests

CONFIG_FILE = "config.json"

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

ACCESS_TOKEN = config["access_token"]
INSTAGRAM_BUSINESS_ID = config["instagram_business_id"]

PHOTOS_FOLDER = config["photos_folder"]
POSTED_FOLDER = config["posted_folder"]
LOG_FOLDER = config["log_folder"]

CAPTION = config["caption_template"]

print("Instagram Auto Uploader Started")

os.makedirs(PHOTOS_FOLDER, exist_ok=True)
os.makedirs(POSTED_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)
def create_container(image_path):
    url = f"https://graph.facebook.com/v25.0/{INSTAGRAM_BUSINESS_ID}/media"

    data = {
        "image_url": image_path,
        "caption": CAPTION,
        "access_token": ACCESS_TOKEN,
    }

    r = requests.post(url, data=data)
    print(r.text)
    return r.json().get("id")


def publish(container_id):
    url = f"https://graph.facebook.com/v25.0/{INSTAGRAM_BUSINESS_ID}/media_publish"

    data = {
        "creation_id": container_id,
        "access_token": ACCESS_TOKEN,
    }

    r = requests.post(url, data=data)
    print(r.text)