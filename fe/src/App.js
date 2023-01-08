import { useState } from 'react';
import axios from 'axios';
import { Container, Form, Row, Col, Button, Card } from 'react-bootstrap';
import ShowMoreText from "react-show-more-text";
import { Rating } from 'react-simple-star-rating'
import './App.css';

const MovieCard = ({ data }) => {
  return (
    <Card>
      <p>Movie: {data.name}</p>
      <p>Rating:   <Rating
        initialValue={data.rating}
        readonly
      /></p>
      <ShowMoreText>{data.description}</ShowMoreText>
      <p>
        Artist: {data.artist.name}
      </p>
      <p>Email: {data.artist.email}</p>
    </Card>
  )
}


function App() {
  const [loading, setLoading] = useState(false)
  const [search, setSearch] = useState("")
  const [data, setData] = useState([])

  const searchMovie = () => {
    if (search !== "") {
      setLoading(true)
      axios.get(`http://127.0.0.1:8000/api/movieElastic?search=${search}`).then(res => {
        setData(res.data)
      }).catch(e => console.log(e)).finally(e => setLoading(false))
    }
  }

  return (
    <div className="App">
      <Container className="mt-5">
        <Row className='mb-3'>
          <Col md={{ span: 4, offset: 4 }} className="d-flex">
            <Form.Control type="search" value={search} onChange={e => setSearch(e.target.value)} placeholder="search" size="lg" />
            <Button onClick={searchMovie}>Search</Button>
          </Col>
        </Row>
        <Row >
          {loading ? <Container >Loading....</Container> : data.length > 0 ? data.map((movie, index) => (
            <Col md={4} mt={2} key={index}>
              <MovieCard data={movie} />
            </Col>
          )) : "No data"}
        </Row>
      </Container>
    </div>
  );
}

export default App;
