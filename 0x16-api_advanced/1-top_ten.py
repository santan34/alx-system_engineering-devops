#!/usr/bin/python3
"""reddit tish"""
import requests


def top_ten(subreddit):
    """to 10"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "ndanda ndanda"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]