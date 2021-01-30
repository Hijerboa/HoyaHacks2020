from fastapi import FastAPI
import json, requests, datetime
import cred_handler
from dateutil import parser

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "HELLO YOU FUCKERS"}

@app.get("/tickers")
async def get_tickers(ticker_start: str):
    """
    Return the top 5 tickers starting with the string `ticker_start` from the list of valid ticker symbols.
    """
    # TODO: This. It's low priority.
    return {"message" : "dummy return message"}

@app.get("/data")
async def get_plot_data(ticker: str, start_date: str, stop_date: str, interval: str):
    """
    Return the reddit and stock market data for the desired ticker, interval and time period.
    """
    
    offset = 0
    target = 0
    market_data = []

    #Get our sweet sweet data
    while  offset <= target:
        # Set up request for marketstack API
        p = {
        'access_key' : cred_handler.get_secret('quickstart_key'),
        'symbols' : ticker,
        'date_from' : start_date,
        'date-to' : stop_date,
        'interval' : '1h',
        'limit' : '1000',
        'offset' : str(offset)
        }

        r = requests.get('http://api.marketstack.com/v1/intraday', params=p)
        if not r.status_code == 200:
            msg = "ERROR: API call to Marketstack failed with status code " + str(r.status_code)
            print(msg)
            print(p)
            return {"message" : msg}
        
        json_result = json.loads(r.text)

        ##update our target number and increment our offset
        target = int(json_result['pagination']['total'])
        offset += 1000

        #add result to current collected market data
        for x in json_result['data']:
            market_data.append(x)
        print(market_data)
        market_data = sorted(market_data, key= lambda x:(x['date']))
        print('got through one iteration')

    # Format data as a list of prices at timestep
    return_market_data = []
    for point in market_data:
        posix_stamp = parser.isoparse(point['date']).timestamp()
        return_market_data.append({'x': posix_stamp, 'y': (float(point['open']) + float(point['close'])) / 2.0})

    return return_market_data


@app.get("/FUCK")
async def fuck():
    """
    This says fuck
    """
    return {"message" : "haha our repo says fuck :^)"}