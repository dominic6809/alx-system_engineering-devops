#!/usr/bin/python3
"""
modules to import
"""
import requests


def top_ten(subreddit):
    """
    function that prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                     subreddit=subreddit)

    user_agent = {'User-Agent': 'Python/requests'}

    payload = {'limit': '10'}

    res = requests.get(api_uri, headers=user_agent,
                            params=payload, allow_redirects=False)

    if res.status_code in [302, 404]:
        print('None')
    else:
        response_json = res.json()

        if response_json.get('data') and response_json.get('data').get('children'):
            hot_posts = response_json.get('data').get('children')

            for post in hot_posts:
                if post.get('data') and post.get('data').get('title'):
                    print(post.get('data').get('title'))
