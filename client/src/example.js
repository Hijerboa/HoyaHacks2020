import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

// This site has 3 pages, all of which are rendered
// dynamically in the browser (not server rendered).
//
// Although the page does not ever refresh, notice how
// React Router keeps the URL up to date as you navigate
// through the site. This preserves the browser history,
// making sure things like the back button and bookmarks
// work properly.

export default function BasicExample() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
        </ul>

        <hr />

        {/*
          A <Switch> looks through all its children <Route>
          elements and renders the first one whose path
          matches the current URL. Use a <Switch> any time
          you have multiple routes, but you want only one
          of them to render at a time
        */}
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/dashboard">
            <Dashboard />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

// You can think of these components as "pages"
// in your app.

function Home() {
  return (
    <div>
      <h2>Home</h2>
    </div>
  );
}

function About() {
  return (
    <div>
      <h2>About</h2>
    </div>
  );
}

function Dashboard() {
  return (
    <div>
      <h2>Dashboard</h2>
    </div>
  );
}

function Chart() {
  return (
    <div id="stonkContainer" style="width: 100%; height: 100%;">
      <canvas id="stonkChart" width="400" height="400"></canvas>
      <script>
        var stonkCtx = document.getElementById('stonkChart').getContext('2d');
        var stonkChart = new Chart(stonkCtx, {
          // change the type of chart here
          type: "line",
          // setup the data options here
          data: {

          },
          // configure the chart here
          options: {

          }
        });
      </script>
    </div>
  );
}

/**
 * Requests data for the chart in an asynchrounous fashion.
 * Use the `await requestChartData().then(data => {});` pattern when calling this function.
 * :param ticker: The stock ticker to lookup.
 * :param start_date: The start date of the lookup window.
 * :param end_date: The end date of the lookup window.
 * Returns the JSON data for the stock ticker gathered by the API server.
 */
// ticker: str, start_date: str, stop_date: str
async function requestChartData(ticker, start_date, stop_date) {
  var api_str = "http://localhost:8000";
  var params = URLSearchParams();
  params.set('ticker', ticker);
  params.set('start_date', start_date);
  params.set('stop_date', stop_date);
  const response = await fetch(new URL(api_str + params.toString()), {
    method: 'GET',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin'
  });
  return response.json();
}
