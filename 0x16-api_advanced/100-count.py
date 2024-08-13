#!/usr/bin/python3
"""
Recurse it!

"""
import requests


def recursive_count(subreddit, word_list, after='', word_count=None):
    """Initialize word count"""
    if word_count is None:
        word_count = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'keyword counter'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params,
                                timeout=10)
        if response.status_code == 404:
            return
        data = response.json()
    except Exception:
        return

    for child in data['data']['children']:
        title = child['data']['title'].lower().split()
        for word in title:
            word = word.strip('.,!?()[]{}<>:"\'')
            if word in word_count:
                word_count[word] += 1

    after = data['data']['after']
    if after:
        return recursive_count(subreddit, word_list, after, word_count)
    return word_count


def count_words(subreddit, word_list):
    """Count words"""
    word_count = recursive_count(subreddit, word_list)
    if word_count is None:
        return

    sorted_word_count = sorted(
        [(word, count) for word, count in word_count.items() if count > 0],
        key=lambda x: (-x[1], x[0])
    )
    for word, count in sorted_word_count:
        print(f'{word}: {count}')
