#!/usr/bin/python3
"""
query the reddit api
"""

from requests import get


def number_of_subscribers(subreddit):
    """subredit"""
    head = {'user-agent': 'Takudzwanashe ndaveni'}
    response = get(f"https://www.reddit.com/r/{subreddit}/about.json",headers=head)
    if response.status_code == 404:
        return 0
    else:
        return response.json().get("data").get("subscribers")
