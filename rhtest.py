from utils import cred_handler as c
import requests, json, datetime
from dateutil import parser

est = datetime.timedelta(hours=-5)

p = {
    'access_key' : c.get_secret('quickstart_key'),
    'symbols' : 'GME',
    'date_from' : '2021-01-01',
    'date-to' : '2021-01-29',
    'interval' : '15min',
    'limit' : '1000'
}

r = requests.get('http://api.marketstack.com/v1/intraday', params=p)
print(r)
dat = json.loads(r.text)['data']
for d in sorted(dat, key= lambda x:(x['date'])):
    print(f"{d['symbol']}\t{parser.isoparse(d['date']).astimezone()}\t${d['open']:.2f}\t${d['high']:.2f}\t${d['low']:.2f}\t${d['close']:.2f}")