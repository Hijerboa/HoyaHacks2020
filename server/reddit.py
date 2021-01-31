import requests
import json
import datetime
from dateutil import parser
import time

def poll_reddit_nums(start_timestamp, stop_timestamp, ticker, threshold = 50, interval = 3600, delay = 0.25):
    st = time.time()
    
    ticker_data = []

    complete = False
    section_start_timestamp = start_timestamp
    count_ticker = 0
    callnum = 1
    while(not complete):
        print(f"call {callnum} for pushshift api")
        p = {
            'subreddit' : 'wallstreetbets',
            'title' : 'GME',
            'fields' : ['created_utc', 'num_comments', 'score'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'num_comments' :  '>'+str(threshold)
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code) + " ...Passing"
            print(msg)
            time.sleep(0.1)
        else:
            json_result = json.loads(r.text)
            for x in json_result['data']:
                print(x)
                ticker_data.append(x)
            count_ticker += len(json_result['data'])
            if len(json_result['data']) == 100:
                section_start_timestamp = json_result['data'][-1]['created_utc']
                #print(section_start_timestamp)
                time.sleep(0.05)
            else:
                complete = True
        callnum += 1
    print(f'count_ticker = {count_ticker}')

    bucket_timestamps = range(int(start_timestamp), int(stop_timestamp) + int(interval), int(interval))
    ticker_buckets = {}
    for x in bucket_timestamps:
        #ticker
        ticker_buckets[x] = 0
        for y in ticker_data:
            if int(y['created_utc']) < x + interval:
                ticker_buckets[x] += 1
                ticker_data.remove(y)
            else:
                break

    ret = []
    for x in zip(bucket_timestamps, ticker_buckets.values()): 
        #print(x)
        ret.append({
            'x': int(x[0]),
            'y': float(x[1])
        })
    ed = time.time()
    delta = ed - st
    print(f'Executed in {delta} seconds.')
    return ret



def poll_reddit_data(start_timestamp, stop_timestamp, ticker, threshold = 50, interval = 3600, delay = 0.25):
    st = time.time()
    
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
            'fields' : ['created_utc', 'num_comments', 'score'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'num_comments' :  '>'+str(int(threshold))
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code)
            print(msg)
            time.sleep(0.1)
        else:
            json_result = json.loads(r.text)
            for x in json_result['data']:
                #print(x)
                noticker_data.append(x)
            count_noticker += len(json_result['data'])
            if len(json_result['data']) == 100:
                section_start_timestamp = json_result['data'][-1]['created_utc']
                #print(section_start_timestamp)
                time.sleep(0.05)
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
            'title' : ticker.upper(),
            'fields' : ['created_utc', 'num_comments', 'score'],
            'size' : 500,
            'sort' : 'asc',
            'sort_by' : 'created_utc',
            'after' : int(section_start_timestamp),
            'before' : int(stop_timestamp),
            'num_comments' :  '>'+str(int(threshold))
        }

        r = requests.get('https://api.pushshift.io/reddit/submission/search', params=p)
        if not r.status_code == 200:
            print(r)
            msg = "ERROR: API call to pushshift failed with status code " + str(r.status_code) + " ...Passing"
            print(msg)
            time.sleep(0.1)
        else:
            json_result = json.loads(r.text)
            for x in json_result['data']:
                #print(x)
                ticker_data.append(x)
            count_ticker += len(json_result['data'])
            if len(json_result['data']) == 100:
                section_start_timestamp = json_result['data'][-1]['created_utc']
                #print(section_start_timestamp)
                time.sleep(0.05)
            else:
                complete = True
        callnum += 1
    print(f'count_ticker = {count_ticker}')


    #print(len(ticker_data))
    #print(len(noticker_data))

    #Make them buckets
    bucket_timestamps = range(int(start_timestamp), int(stop_timestamp) + int(interval), int(interval))
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
    for x in zip(bucket_timestamps, ticker_buckets.values(), noticker_buckets.values()): 
        #print(x)
        ret.append({
            'x': int(x[0]),
            'y': float(x[1]) / float(x[2]) if not float(x[2]) == 0 else 0
        })
    ed = time.time()
    delta = ed - st
    print(f'Executed in {delta} seconds.')
    return ret

#ret = poll_reddit_data(parser.isoparse('2021-01-27').timestamp(), parser.isoparse('2021-01-28').timestamp(), 'GME', threshold = 50)
#for x in ret:
#    print(x)

