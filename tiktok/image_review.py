import base64
import os

import requests
from openai import OpenAI

from files import json_write_file

MODEL = "gpt-4o"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def review_instagram_images(instagram):
    for post in instagram["posts"]:
        if "image_summary" in post:
            continue

        if "url" not in post:
            continue
        response = requests.get(post["url"])

        encoded_string = base64.b64encode(response.content).decode("utf-8")

        post["image_summary"] = image_review(encoded_string)

    json_write_file(instagram["path"], instagram)

    return instagram


def image_review(image_bytes):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are an instagram post reviewer describe everything that is in the image"},
            {"role": "user", "content": [
                {"type": "text", "text": "Describe everything you see in the instagram image in one paragraph:"},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{image_bytes}"}
                }
            ]}
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content
