#!/usr/bin/python3
"""
query the reddit api
"""

from requests import get


def number_of_subscribers(subreddit):
    """subredit"""
    head = {'user-agent': 'Takudzwanashe ndaveni'}
    try:
        subs = get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=head).json().get("data").get("subscribers")
        return (subs)
    except BaseException:
        return 0
