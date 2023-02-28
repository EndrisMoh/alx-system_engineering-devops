#!/usr/bin/python3
"""A  recursive function that queries the Reddit API and returns a list
   containing the titles of all hot articles for a given subreddit"""
import requests


after = ""


def recurse(subreddit, hot_list=[]):
    """returns list with titles and articles"""
    global after
    header = {"User-Agent": "ALX"}
    url = "https://www.reddit.com/r/" + subreddit + "/hot.json"
    if after:
        url = url + "?after=" + after
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code != 200:
        return None
    after = r.json().get("after", "")
    for i in r.json().get("data", None).get("children", None):
        hot_list.append(i.get("data", None).get("title", None))
    if after:
        return recurse(subreddit, hot_list)
    return hot_list


if __name__ == "__main__":
    pass
