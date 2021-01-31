# WallStreetBets Correlator
Authors: Nathan Dixon, Nick Cleary, Christen Ford, David Fu
## Description
WallStreetBets Correlator is an API and web front end that show the proportion of relevant posts (over 50 comments) on r/wallstreetbets that mention any given stock ticker, and displays the price of the stock at that point. The data for reddit posts is fetched from the pushshift.io API in hourly intervals, and the stock data is fetched from Marketstack's Stock API. The data from these two sources is then aggregated and sent to the ChartJS front end through a FastAPI framework on the back end. 


## API Endpoints
| Endpoint | Usage | Parameters |
| -------- | ----- | ---------- |
| /market | Returns the value of the given ticker at each applicable timestep | start_date, end_date, ticker |
| /reddit | Returns the ratio of posts with more than \<threshold\> comments mentioning the stock ticker on r/wallstreetbets at each applicable timestep | start_date, end_date, ticker, threshold |
