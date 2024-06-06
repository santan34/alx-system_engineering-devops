#!/usr/bin/python3
"""recursive API"""
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """recursive hot query"""
    head = {"user-agent": "Ndaveni Takudzwanashe"}
    try:
        if after:
            li = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            li = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in li.get('children')]
        if li.get('after'):
            return recurse(subreddit, hotlist, after=li.get('after'))
        return hotlist
    except BaseException:

        return None


if __name__ == "__main__":
    recurse(argv[1])
