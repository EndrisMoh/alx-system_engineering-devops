#!/usr/bin/python3
""" A function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """returns first 10 hot posts"""
    header = {"User-Agent": "ALX"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10"
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        for i in r.json().get("data", None).get("children", None):
            print(i.get("data", None).get("title", None))
    else:
        print(None)


if __name__ == "__main__":
    pass
