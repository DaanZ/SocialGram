from llm import History, llm_chat
from files import json_write_file


def review_improvements(instagram):
    if "review" in instagram and "improvements" in instagram:
        return instagram

    post_reviews = []
    for post in instagram["posts"]:
        post_reviews.append(post["review"])
    instagram["review"] = get_review(post_reviews)

    post_improvements = []
    for post in instagram["posts"]:
        post_improvements.append(post["improvements"])
    instagram["improvements"] = get_improvements(post_improvements)
    json_write_file(instagram["path"], instagram)
    return instagram


def get_review(reviews):
    history = History()

    history.system("You are an instagram post reviewer describe in detail to summarize them")

    for review in reviews:
        history.system("Review: " + review)

    history.system(f"Summarize reviews from instagram posts above and find keypoints among all:")
    answer = llm_chat(history)
    return answer


def get_improvements(improvements):
    history = History()

    history.system("You are an instagram post improver describe in detail to summarize them")

    for review in improvements:
        history.system("Review: " + review)
    history.system(f"Summarize concrete and specific points for which improvements can be made with their instagram outreach with:")
    answer = llm_chat(history)
    return answer

