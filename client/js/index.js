/**
 * Requests data for the chart in an asynchrounous fashion.
 * Use the `await requestChartData().then(data => {});` pattern when calling this function.
 * :param ticker: The stock ticker to lookup.
 * :param start_date: The start date of the lookup window.
 * :param end_date: The end date of the lookup window.
 * Returns the JSON data for the stock ticker gathered by the API server.
 */
// ticker: str, start_date: str, stop_date: str
async function requestChartData(ticker, start_date, stop_date, threshold) {
    var api_str = "http://stonksgoto.space:8000";
    
    var params = new URLSearchParams();
    params.set('ticker', ticker);
    params.set('start_date', start_date);
    params.set('stop_date', stop_date);
    params.set('thresh', threshold);
    const redditData = await fetch(new URL(api_str + "/reddit?" + params.toString()), {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin'
    });

    var params = new URLSearchParams();
    params.set('ticker', ticker);
    params.set('start_date', start_date);
    params.set('stop_date', stop_date);
    const marketData = await fetch(new URL(api_str + "/market?" + params.toString()), {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin'
    });

    return Promise.all([redditData.json(), marketData.json()]);
}