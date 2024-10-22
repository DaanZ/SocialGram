
from files import json_write_file
from llm import History, llm_chat


def review_posts(instagram):
    for post in instagram["posts"]:
        if "review" in post and "improvements" in post:
            continue
        post["review"], post["improvements"] = post_review(post, instagram)

    json_write_file(instagram["path"], instagram)
    return instagram


def post_review(post, instagram):
    history = History()
    history.system("You are an instagram post reviewer")
    history.system("Current Trends: " + instagram["research"])
    history.system(f"Current Post likes: {post['likes']} and Account average likes: {instagram['avg_likes']}")
    history.system(f"Image description: {post['image_summary']}")
    history.system(f"Post Caption: {post['caption']}")
    history.system(f"Transcription: {post['transcript']}")

    history.system("Describe in detail the performance of this post and why you came to that conclusion in one paragraph")
    review = llm_chat(history)
    history.assistant(review)

    history.system("Describe the improvements that could be made to make this post perform better in one paragraph.")
    improvements = llm_chat(history)
    history.assistant(improvements)

    return review, improvements

