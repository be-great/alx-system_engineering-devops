#!/usr/bin/python3
"""
Recurse it!

"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """top host list in subreddit"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100, 'after': after}
    response = requests.get(url,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    data = response.json()
    # Extract the list of posts
    children = data['data']['children']
    if not children:
        return hot_list
    # Append the titles to the hot_list
    hot_list.extend([post['data']['title'] for post in children])
    # Check if there's a next page (pagination)
    after = data['data']['after']
    if after:
        # Recursive call to get the next page
        return recurse(subreddit, hot_list, after)
    return (hot_list)
