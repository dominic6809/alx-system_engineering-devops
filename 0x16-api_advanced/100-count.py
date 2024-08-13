#!/usr/bin/python3
"""
counts no of time a keyword appears in hot titles
"""
import requests


def count_words(subreddit, word_list, count_dict=None, after=None):
    """counts the no of times a word appears in hot titles
        subreddit: the name of the subreddit to query
        word_list: a list of keywords to count
        count_dict: a dictionary to store the counts of each keyword
        after: the ID of the last post in the current batch
    """
    if count_dict is None:
        count_dict = {}
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{subreddit}/hot/.json'
    # set limit and after params for API request
    try:
        params = {'limit': 100}
        if after:
            params['after'] = after
            # HTTP Request
            response = requests.get(url, headers=headers)
            if response == 200:
                data = response.json()
                for post in data['data']['children']:
                    title = post['data']['children'].lower()
                    # split words and strip punctuations
                    words = [w.strip('.,/!?:;"\'(){}[]')for w in title.split()]
                    for word in word_list:
                        for c in word:
                            if word.lower() in words and not any(c.isalpha())                            count_dict[word.lower()] = count_dict.get(
                                word.lower(), 0) + words.count(word.lower())
                        # Recursively call the function with the after
                        # parameter to get the next page of results
                if 'after' in data['data']:
                    count_words(subreddit, word_list, count_dict,
                                data['data']['after'])
        # Catch any exceptions that occur during the API request
        except Exception as e:
            print(e)
        if not after:
            # Sort the count dictionary by count (desc) and word (asc)
            count_list = [(k, v) for k, v in count_dict.items()
                          if k.lower() in word_list]
        count_list.sort(key=lambda x: (-x[1], x[0]))
        for k, v in count_list:
            print(f"{k}: {v}")
