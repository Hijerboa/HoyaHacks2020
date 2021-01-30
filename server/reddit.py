import requests
import json
import datetime
from dateutil import parser
import time


def poll_reddit_data(start_timestamp, stop_timestamp, ticker, threshold = 2, interval = 3600, delay = 0.25):
    ticker_data = []
    noticker_data = []

    complete = False
    section_start_timestamp = start_timestamp
    count_noticker = 0
    callnum = 1
    while(not complete):
        print(f"call {callnum} for pushshift api")
        p = {
            'subreddit' : 'wallstreetbets',
            'fields' : ['created_utc'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'score' :  '>'+str(int(threshold))
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code)
            print(msg)
            return 0
        json_result = json.loads(r.text)
        for x in json_result['data']:
            noticker_data.append(x)
        count_noticker += len(json_result['data'])
        if len(json_result['data']) == 100:
            section_start_timestamp = json_result['data'][-1]['created_utc']
            #print(section_start_timestamp)
            time.sleep(delay)
        else:
            complete = True
        callnum += 1
    print(f'count_noticker = {count_noticker}')


    complete = False
    section_start_timestamp = start_timestamp
    count_ticker = 0
    while(not complete):
        print(f"call {callnum} for pushshift api")
        p = {
            'subreddit' : 'wallstreetbets',
            'title' : 'GME',
            'fields' : ['created_utc'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'score' :  '>'+str(int(threshold))
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code)
            print(msg)
            return 0
        json_result = json.loads(r.text)
        for x in json_result['data']:
            ticker_data.append(x)
        count_ticker += len(json_result['data'])
        if len(json_result['data']) == 100:
            section_start_timestamp = json_result['data'][-1]['created_utc']
            #print(section_start_timestamp)
            time.sleep(delay)
        else:
            complete = True
        callnum += 1
    print(f'count_ticker = {count_ticker}')


    #print(len(ticker_data))
    #print(len(noticker_data))

    #Make them buckets
    bucket_timestamps = range(int(start_timestamp), int(stop_timestamp), int(interval))
    noticker_buckets = {}
    ticker_buckets = {}
    for x in bucket_timestamps:
        #noticker
        noticker_buckets[x] = 0
        for y in noticker_data:
            if int(y['created_utc']) < x + interval:
                noticker_buckets[x] += 1
                noticker_data.remove(y)
            else:
                break
        
        #ticker
        ticker_buckets[x] = 0
        for y in ticker_data:
            if int(y['created_utc']) < x + interval:
                ticker_buckets[x] += 1
                ticker_data.remove(y)
            else:
                break
    
    #print(len(ticker_data))
    #print(len(noticker_data))

    #print(ticker_buckets)
    #print(noticker_buckets)

    ret = []
    for x in zip(bucket_timestamps, ticker_buckets.values(), noticker_buckets.values()): #[0,1,2], [3,4,5], [6,7,8] => [0,3,6], [1,4,7], [2,5,8]
        #print(x)
        ret.append({
            'x': int(x[0]),
            'y': float(x[1]) / float(x[2]) if not float(x[2]) == 0 else 0
        })

    return ret


#print(poll_reddit_data(parser.isoparse('2021-01-28').timestamp(), parser.isoparse('2021-01-29').timestamp(), 'GME'))


    