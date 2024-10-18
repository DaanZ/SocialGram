import json
import os

import rootpath

from analyzer import analyze_likes, sort_likes
from image_review import review_instagram_images
from learnings import review_improvements
from query_post import review_posts
from video_review import transcript_video_instagram


if __name__ == "__main__":

    url = "https://www.instagram.com/reset_energia"
    name = url.split("/")[-1]
    file_path = os.path.join(rootpath.detect(), "data", name + ".json")
    with open(file_path, 'r', encoding="utf-8") as file:
        instagram = json.loads(file.read())
    #instagram = scrape_instagram_posts(file_path, name)
    instagram = review_instagram_images(instagram)
    instagram = transcript_video_instagram(instagram)
    instagram = analyze_likes(instagram)
    instagram = sort_likes(instagram)
    instagram = review_posts(instagram)
    instagram = review_improvements(instagram)
