#!/usr/bin/python3
"""more recursion"""
import requests

def top_hot_subreddit(subreddit, word_list, count=0, after=None, words={}):
    """top 10 fix"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?\
limit=100&after={after}&count={count}"

    headers = {"User-Agent": "ndanda"}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return None

    res = req.json().get('data')
    title = res.get('children')
    after = res.get('after')
    count += res.get('dist')
    
    for title in title:
        title = (title.get('data').get('title')).lower().split()
        for word in title:
            if word in word_list:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

    if after:
        top_hot_subreddit(subreddit, word_list, count, after, words)

    return words


def counter(subreddit, word_list):
    '''Get the top 10 hot posts for a given subreddit'''
    word_list = [word.lower() for word in word_list]
    result = top_hot_subreddit(subreddit, word_list)
    if result:
        sorted_dict = sorted(result.items(), key=lambda item: item[1],
                             reverse=True)
        for key, val in sorted_dict:
            print(f"{key}: {val}")

    return None