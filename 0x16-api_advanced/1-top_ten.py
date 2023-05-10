#!/usr/bin/python3
"""Prints titles of first 10 hot posts listed for a given subreddit."""
from requests import get


def top_ten(subreddit):
    """Description:
        - queries Reddit API to print first 10 host posts
    Output:
        - Success: prints first 10 host posts listed for a given subreddit
        - Failure: print None
    """
    route = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'limit': 10}
    resp = get(route, headers=headers, allow_redirects=False, params=params)

    if resp.status_code != 200:
        print(None)
        return

    top_10 = resp.json()['data']['children']
    [print(post['data']['title']) for post in top_10]
