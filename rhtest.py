import requests
import json
import datetime
from dateutil import parser
import time

def poll_reddit_data(start_datetime, stop_datetime, ticker):
    complete = False
    section_start_timestamp = start_timestamp
    count_noticker = 0
    while(not complete):
        p = {
            'subreddit' : 'wallstreetbets',
            #'title' : 'GME',
            'fields' : ['created_utc'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'score' :  '>5'
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code)
            print(msg)
            break
        json_result = json.loads(r.text)
        for x in json_result['data']:
            #print(str(x))
            pass
        count_noticker += len(json_result['data'])
        if len(json_result['data']) == 100:
            section_start_timestamp = json_result['data'][-1]['created_utc']
            #print(section_start_timestamp)
            time.sleep(0.25)
        else:
            complete = True
    #print(count_noticker)


    complete = False
    section_start_timestamp = start_timestamp
    count_ticker = 0
    while(not complete):
        p = {
            'subreddit' : 'wallstreetbets',
            'title' : 'GME',
            'fields' : ['created_utc'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'score' :  '>5'
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code)
            print(msg)
            break
        json_result = json.loads(r.text)
        for x in json_result['data']:
            #print(str(x))
            pass
        count_ticker += len(json_result['data'])
        if len(json_result['data']) == 100:
            section_start_timestamp = json_result['data'][-1]['created_utc']
            #print(section_start_timestamp)
            time.sleep(0.25)
        else:
            complete = True
    #print(count_ticker)

    return count_ticker/count_noticker