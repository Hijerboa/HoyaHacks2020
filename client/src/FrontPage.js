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
import {Grid, Row, Col, InputGroup, FormControl} from 'react-bootstrap';
import Navbar from 'react-bootstrap/Navbar'
import Nav from "react-bootstrap/Nav";
import './frontpage.css';
import Brand from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav"
import Canvas from "Canvas"

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
            <Link to="/"><Navbar.Brand>WSB Correlator</Navbar.Brand></Link>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link><Link to="/about">About</Link></Nav.Link>
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

function Home() {
  return (
    <Container fluid>
        <Row>
            <Col xs={12} md={6}>
                <Row>
                    <Col>
                        <div>
                            <InputGroup className="mb-3">
                                <InputGroup.Prepend>
                                    <InputGroup.Text id="tickerTitle">$</InputGroup.Text>
                                </InputGroup.Prepend>
                                <FormControl
                                    placeholder="Ticker"
                                    aria-lable="Ticker"
                                    aria-descibedby="tickerTitle"
                                />
                            </InputGroup>
                        </div>
                    </Col>
                </Row>
            </Col>
            <Col xs={12} md={6}>
                <Row>
                    <Col xs={4} md={4}>
                        <Button className="buttonboi" varient="primary" block>Hour</Button>
                    </Col>
                    <Col xs={4} md={4}>
                        <Button className="buttonboi" variant="success" block>Day</Button>
                    </Col>
                    <Col xs={4} md={4}>
                        <Button className="buttonboi" variant="info" block>Week</Button>
                    </Col>
                </Row>
            </Col>
        </Row>
        <Row>
            <CanvasComponent />
        </Row>
    </Container>
  );
}

function About() {
  return (
    <div>
      <h2>About</h2>
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
async function requestChartData(ticker, start_date, stop_date, interval) {
    var api_str = "http://localhost:8000/data";
    var params = URLSearchParams();
    params.set('ticker', ticker);
    params.set('start_date', start_date);
    params.set('stop_date', stop_date);
    params.set('interval', interval);
    const response = await fetch(new URL(api_str + params.toString()), {
        method: 'GET',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin'
    });
    return response.json();
}

// You should be able to just create an instance of this component to create
//  the stonk chart
class CanvasComponent extends React.Component {
  componentDidMount() {
    this.updateCanvas();
  }
  updateCanvas() {
    // TODO: Necessary data can be grabbed from the UI elements through the DOM
    //  It still needs to be passed to the requestChartData function
    requestChartData().then(stonkData => {
      // TODO: Draw the data on the chart
      const ctx = this.refs.stonkCanvas.getContext('2d');
      // create the chart instance
      const stonkChart = new Chart(ctx, {
        type: "line",
        data: {
          // TODO: Update the indices here for stonkData once they've been finalized at server.
          datasets: [
            {
              // TODO: Come up with a label
              label: "",
              data: stonkData['']
            },
            {
              // TODO: Come up with a label
              label: "",
              data: stonkData['']
            }
          ]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });
    });
  }
  // Question: Can the render function accept arguments? If not, is there a way to 
  //  programatically determine the width and height below?
  render() {
    return (
      <canvas ref="stonkCanvas" width={400} height={400}/>
    );
  }
}
ReactDOM.render(<CanvasComponent/>, document.getElementById('stonkContainer'));