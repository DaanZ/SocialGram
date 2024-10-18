from files import json_write_file


def analyze_likes(instagram):
    total_likes = 0
    total_views = 0
    count_posts = len(instagram["posts"])

    for post in instagram["posts"]:
        total_likes += post["likes"] if post["likes"] else 0
        total_views += post["view_count"] if post["view_count"] else 0

    instagram["avg_likes"] = total_likes / count_posts
    instagram["avg_views"] = total_views / count_posts
    json_write_file(instagram["path"], instagram)
    return instagram


def sort_likes(instagram):
    instagram["posts"] = sorted(instagram["posts"], key=lambda x: x['likes'], reverse=True)
    json_write_file(instagram["path"], instagram)
    return instagram
