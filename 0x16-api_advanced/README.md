#!/usr/bin/python3
"""Queries and returns corresponding result from the Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Description:
    - queries and returns the number of subscibers
      (not active users, total subscribers) for a given subreddit.
    - returns 0 if an invalid subreddit is given
    """
    route = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    resp = requests.get(route, headers=headers)

    if resp.status_code != 200:
        return 0
    return resp.json()['data']['subscribers']
