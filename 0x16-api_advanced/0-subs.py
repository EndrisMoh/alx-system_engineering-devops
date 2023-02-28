#!/usr/bin/python3
"""A function that queries the Reddit API and
 returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns total subscribers"""
    header = {"User-Agent": "ALX"}
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        return r.json().get("data", None).get("subscribers", None)
    else:
        return 0

if __name__ == "__main__":
    pass
