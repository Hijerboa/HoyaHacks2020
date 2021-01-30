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
    <Container fluid="lg">
      <Row>
        <Col>1 of 1</Col>
          <Col>2 of 1 :^)</Col>
          <Col>3 of 1</Col>
      </Row>
    </Container>
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
