import os

from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()


def download_posts(username: str, amount_posts: int = 10):
    cl = Client()
    cl.login(os.environ["INSTAGRAM_USERNAME"], os.environ["INSTAGRAM_PASSWORD"])

    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, amount_posts)

    posts = []
    for media in medias:
        print(media)
        if media.thumbnail_url:
            data = {"title": media.title,
                    "caption": media.caption_text,
                    "likes": media.like_count,
                    "view_count": media.view_count,
                    "comments_count": media.comment_count,

                    "url": str(media.thumbnail_url) if media.thumbnail_url else "",
                    "description": "",
                    "video": str(media.video_url) if media.video_url else "",
                    "transcript": "",

                    "date": media.taken_at}
            posts.append(data)

    return posts


if __name__ == "__main__":
    username = "reset_energia"
    print(download_posts(username, 1))
