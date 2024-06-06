#!/usr/bin/python3
"""advanced subs"""
from requests import get
from sys import argv

li_hot = []
after = None


def count_all(li_hot, words):
    count_dic = {word.lower(): 0 for word in words}
    for title in li_hot:
        words = title.split(' ')
        for word in words:
            if count_dic.get(word) is not None:
                count_dic[word] += 1

    for key in sorted(count_dic, key=count_dic.get, reverse=True):
        if count_dic.get(key):
            for thing in words:
                if key == thing.lower():
                    print("{}: {}".format(thing, count_dic[key]))


def count_words(subreddit, words):
    global li_hot
    global after
    """subs"""
    head = {'User-Agent': 'Ndaveni Takudzwanashe'}
    if after:
        count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after), headers=head).json().get('data')
    else:
        count = get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=head).json().get('data')
    li_hot += [dic.get('data').get('title').lower()
                for dic in count.get('children')]
    after = count.get('after')
    if after:
        return count_words(subreddit, words)
    return count_all(li_hot, words)


if __name__ == "__main__":
    count_words(argv[1], argv[2].split(' '))