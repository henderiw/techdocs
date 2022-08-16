# react backend

you never connect to the db, as you would expose the db credentials which is a big security issue

[why a backend](https://academind.com/tutorials/hide-javascript-code)
[swapi](https://swapi.dev/)
[rest/graphql api](https://www.youtube.com/watch?v=PeAOEAmR0D0)
- rest
  - multiple enpoints
  - JSON data
  - any server-side language
  - stateless
  - URL driven: multiple paths
    - HTTP-verb Path Body(optional)
    - POST /user {name: 'Max}
- graphQL
  - 1 endpoint
  - JSON data
  - any server-side language
  - stateless
  - Query-Lanaguage
    - POST /graphql {query: 'query...'}
    - the body is going to the graphQL backend using the query


## example:

section: 10
project: 14-connect-to-backend
file: all

```
function App() {
    const [movies, setMovies] = useState([]);
    async function fetchMoviesHandler() {
    const response = await fetch('https://swapi.dev/api/films/');
    const data = await response.json();
    const tranformedMovies = data.results.map(movieData => {
      return {
        id: movieData.episide_id,
        title: movieData.title,
        openingText: movieData.opening_crawl,
        releaseDate: movieData.release_date,
      };
    });
    setMovies(tranformedMovies);
  }

  return (
    <React.Fragment>
      <section>
        <button onClick={fetchMoviesHandler}>Fetch Movies</button>
      </section>
      <section>
        <MoviesList movies={movies} />
      </section>
    </React.Fragment>
  );
}

```

### give use feedback

see example

### http errors

[https response codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### fetch data when the component renders

useEffect and useCallback

### post data

use firebase google backend

```
https://react-http-demo-e7cd0-default-rtdb.europe-west1.firebasedatabase.app
```

### exmple code

[example code](https://github.com/academind/react-complete-guide-code/tree/14-sending-http-requests)