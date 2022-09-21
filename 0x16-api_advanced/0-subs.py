#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the num of subscribers
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """
    number of suscribers
    https://www.reddit.com/dev/api/#section_subreddits
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
