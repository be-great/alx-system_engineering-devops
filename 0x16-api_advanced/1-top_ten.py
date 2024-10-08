#!/usr/bin/python3
"""
Top Ten
function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""
import requests
import sys


def top_ten(subreddit):
    """return the top ten"""
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        data = resp.json()
        result = data['data']['children']
        i = 0
        for post in result:
            if i > 9:
                return
            print(result[i]['data']['title'])
            i += 1
    else:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
