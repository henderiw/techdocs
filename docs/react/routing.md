# react routing

section: 20
project: 
file: 

multiple pages into a single app

## what is routing

- the app has a single URL
- different visual elements with different URLs
- MPA: multi-page app
  - multiple html files/pages
  - rendered by the browser
- SPA:
  - when building complex user interfaces, we typically build SPA(s)
  - only one initial HTML req/resp
  - Page URK changes are then handled by client-side (react) code

## paackage react-router

client side routing [react-router](https://reactrouter.com/)

version 5 is mostly used, router 6

```
npm install
npm install react-router-dom@5
```

## how

in index.js:
- import BrowserRouter
- render the App withing BroweserRouter

```
import { BrowserRouter } from 'react-router-dom';

root.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>
);
```

in App.js
- import Route + app component
- In the JSX Route component - add path property wih the url extension from the main page -> link to the app component

```
import { Route } from 'react-router-dom';

import Welcome from './pages/Welcome';
import Products from './pages/Products'

function App() {
  return (
    <div>
      <Route path="/welcome">
        <Welcome />
      </Route>
      <Route path="/products">
        <Products />
      </Route>
    </div>
  );
}

export default App;


// our-domain.com/welcome => component Welcome
// our-domain.com/products => component Products
```

the special/page components should be stored in pages folder

```
const Products = () => {
    return <h1>The Products Page</h1>;
};

export default Products;
```

## url navigation is manual

see components/MainHeader.js
- using the Link component

using NavLink provides feedback on which link is active -> we can apply navigation to this
- NavLink iso Link
  
## dynamic path

```
return (
    <div>
      <MainHeader />
      <main>
        <Route path="/welcome">
          <Welcome />
        </Route>
        <Route path="/products">
          <Products />
        </Route>
        <Route path="/product-detail/:productId">
          <ProductDetail />
        </Route>
      </main>
    </div>
  );
```

useParams

```
import { useParams }  from 'react-router-dom'

const ProductDetail = () => {
    const params = useParams()
    return (
        <section>
            <h1>Product Detail</h1>
            <p>{params.productId}</p>
        </section>
    )
}
```

## Switch component of react router

takes the first match

options:
- change order
- exact prop allow to solve the orde

## nested routes

ROUTE can be added in other components so we can

- need to match the path so welcome need to be first

## redirecting the user

redirect to welcome page when hitting the / route

```
<Route path="/" exact>
    <Redirect to='welcome'/>
</Route>
```

## Page Not found

App.js

```
<Route path='*'>
          <NotFound />
        </Route>
```

## imperative navigation

pages/NewQuote.js

```
import {useHistory} from 'react-router-dom'


const NewQuote = () => {
    const history = useHistory()

    const addQuoteHandler = (quoteData) => {
        console.log(quoteData)

        // push a new page on the stack -> we can go back
        // replace => we cannot go back
        history.push('/quotes')

    }
    return (
        <QuoteForm onAddQuote={addQuoteHandler}/>
    )
}
```

## inform user on navigating away

quotes/QuoteForm.js

- onFocus prop with formFocusHandler
- onClick prop with finishEnteringHandler
- import { Prompt } from 'react-router-dom';

```
const QuoteForm = (props) => {
  const [isEntering, setIsEntering] = useState(false)
  const authorInputRef = useRef();
  const textInputRef = useRef();

  function submitFormHandler(event) {
    event.preventDefault();

    const enteredAuthor = authorInputRef.current.value;
    const enteredText = textInputRef.current.value;

    // optional: Could validate here

    props.onAddQuote({ author: enteredAuthor, text: enteredText });
  }

  const formFocusedHandler = () => {
    setIsEntering(true);
  }

  const finishEnteringHandler = () => {
    setIsEntering(false)
  }

  return (
    <Fragment>
      <Prompt when={isEntering} message={(location) => 'Are you sure you want to leave? All your data will be lost'}/>
      <Card>
        <form onFocus={formFocusedHandler} className={classes.form} onSubmit={submitFormHandler}>
          {props.isLoading && (
            <div className={classes.loading}>
              <LoadingSpinner />
            </div>
          )}

          <div className={classes.control}>
            <label htmlFor='author'>Author</label>
            <input type='text' id='author' ref={authorInputRef} />
          </div>
          <div className={classes.control}>
            <label htmlFor='text'>Text</label>
            <textarea id='text' rows='5' ref={textInputRef}></textarea>
          </div>
          <div className={classes.actions}>
            <button onClick={finishEnteringHandler} className='btn'>Add Quote</button>
          </div>
        </form>
      </Card>
    </Fragment>

  );
};
```

## query parameters

quotes/QuoteList.js
- ascending/descending

- import {useHistory, useLocation} from 'react-router-dom'
  - useLocation holds the query Parameters
- sorting logic with onClick

```
const QuoteList = (props) => {
  const history = useHistory();
  const location = useLocation();

  console.log(location)
  // defaul js class
  const queryParams = new URLSearchParams(location.search);
  const isSortingAscending = queryParams.get('sort') === 'asc';

  const sortedQuotes = sortQuotes(props.quotes, isSortingAscending)

  const changeSortingHandler = () => {
    // update the query parameters based on button
    history.push('/quotes?sort=' + (isSortingAscending ? 'desc' : 'asc'))
  }

  return (
    <Fragment>
      <div className={classes.sorting}>
        <button onClick={changeSortingHandler}>Sort {isSortingAscending ? 'Descending' : 'Ascending'}</button>
      </div>
      <ul className={classes.list}>
        {sortedQuotes.map((quote) => (
          <QuoteItem
            key={quote.id}
            id={quote.id}
            author={quote.author}
            text={quote.text}
          />
        ))}
      </ul>
    </Fragment>
  );
};
```

## optimized nesting definition


pages/QuoteDetail.js
- useRouteMatch import
  - import { useParams, Route, Link, useRouteMatch } from 'react-router-dom'
- const match = useRouteMatch();
- path={`${match.path}`}
- 

```
return (
		<Fragment>
			<HighlightedQuote text={quote.text} author={quote.author}/>
			<Route path={`${match.path}`} exect>
				<div className='centered'>
					<Link className='btn--flat' to={`${match.url}/comments`}>
						Load Comments
					</Link>
				</div>
			</Route>
			<Route path={`${match.path}/comments`}>
				<Comments />
			</Route>
		</Fragment>
	)
```

quotes/QuoteList.js

other format

 history.push({
      pathname: location.pathname,
      search: `?sort=${(isSortingAscending ? 'desc' : 'asc')}`
    })

## http interaction

pages/
    - NewQuote
    - AllQuotes
Components:
    - Comments.js
    - NewCommentsForm.js
http and app library

## version 6

- upgrading guide available
- npm install react-router-dom@6
- changes:
  - Switch component -> changed to Routes component
  - Route definition changed -> child component is no longer there, but element
    - <Route path='/welcome> element={<Welcome />} />
  - Internal logic for path evaluation changed
    - exact is gone
    - exct can still be used if defined as /products/*
    - order does not mater any longer
  - NavLink -> activeClassName is removed in v6 this needs to done manually
    - <NavLink className={(navData) => navData.isActive ? classes.active : ''}>
  - Redirect component changed to Navigate
    - also element as a child is required + replace prop
  - Nested routes syntax changed
    - wrap Route with Routes
    - element prop is required as well
    - parent route has to be /welcome/*
    - child route is relative to the parent path
    - Also Link would be a relative path
  - different approach for nested routes
    - Route can be nested in the App.js component
    - all route definitions in 1 place
    - with this definition you need to tell where this is to be added in the dom
      - -> Outlet component in the child component as a placeholder
  - imperative navigation
    - when an action finishes, button was clicked: in v5: useHistory hook
    - v6: 
      - useNavigate hook -> navigate function navigate('/welcome, {replace: true})
      - navigate(1) or navigate(-1)
  - Prompt component: prevent leaving a page when unchanged chnages
    - this does not exits -> you need to implement your own logic

[example1 v5](https://github.com/academind/react-router-v6-update/tree/base-example-v5)
[example1 v6](https://github.com/academind/react-router-v6-update/tree/base-example-v6)

[example2 v5](https://github.com/academind/react-router-v6-update/tree/second-example-v5)
[example2 v6](https://github.com/academind/react-router-v6-update/tree/second-example-v6)

[example3 v5](https://github.com/academind/react-router-v6-update/tree/final-example-v5)
[example3 v6](https://github.com/academind/react-router-v6-update/tree/final-example-v6)

[course content](https://github.com/academind/react-complete-guide-code/tree/20-building-mpas-with-react-router)