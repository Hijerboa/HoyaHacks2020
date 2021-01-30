import React, {useState} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Alert from 'react-bootstrap/Alert';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar'
import Brand from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav"

// This site has 3 pages, all of which are rendered
// dynamically in the browser (not server rendered).
//
// Although the page does not ever refresh, notice how
// React Router keeps the URL up to date as you navigate
// through the site. This preserves the browser history,
// making sure things like the back button and bookmarks
// work properly.

export default function FrontPage() {
  return (
    <Router>
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Link to="/"><Navbar.Brand Link to="/">WSB Correlator</Navbar.Brand></Link>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Link to="/about"><Nav.Link>About</Nav.Link></Link>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
      <hr />
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route exact path="/about">
          <About />
        </Route>
      </Switch>
    </Router>
  );
}

// You can think of these components as "pages"
// in your app.

function Home() {
  return (
    <div>
      <h2>Home</h2>
      <Alert dismissible variant="success">
        <Alert.Heading>Oh no what are you doing step-code?</Alert.Heading>
        <p>OwO whats this?</p>
      </Alert>
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

function Owogenerator(){
  const [show, setShow] = useState(true);

  return(
    <>
      <Alert show={show} varient="danger">
        <Alert.Heading>
          OwO whats this?
        </Alert.Heading>
        <p>
          Uh oh! It looks like we made a fucky-wucky! Click the unfucky wucky button fix it!
        </p>
        <hr />
        <div className="d-flex justify-content-end">
          <Button onClick={() => setShow(false)} variant="outline-danger">
            Fix it Daddy!
          </Button>
        </div>
      </Alert>

      {!show && <Button onClick={() => setShow(true)}>Show the fucky wucky! ;-;</Button>}
    </>
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
