#!/usr/bin/python3
"""
Top Ten
function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """return the top ten"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    resp = requests.get(url, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        result = data['data']['children']
        for post in result:
            print(result)
    else:
        print(None)
