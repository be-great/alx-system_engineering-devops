#!/usr/bin/python3
"""
How many subs
nd returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    return the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    result = 0
    if resp.status_code == 200:
        data = resp.json()
        result = data['data']['subscribers']

    return (result)
