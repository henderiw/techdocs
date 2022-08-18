# react redux

section: 18/19
project: 
file: 

[example code](https://github.com/academind/react-complete-guide-code/tree/19-advanced-redux)
## what

A state management system for a cross-component or app-wide state

type of state:
- local state: 
  - belongs to a single component
  - e.g. listening to user input in a input field
  - useSttae, useReducer
- cross-component state:
  - state that affectss multiple components
  - open/closed state of a modal overla
  - prop chains/prop drilling
- app-wide state:
  - user authentication
  - prop chains/drilling


context or redux help cross-component state

## redux vs react context

context disadvantages:
- can become complex -> depends on app we are building
  - deeply nested context provider
- performance


context and redux can be used together in the same app

## how redux works

- 1 central data (state) store
  - authentication
  - theming
  - user input
- component subscription
  - component dont directly update the data in the store
- reducer function -> mutates (=changes) store data
- components function dispatch action -> forwarded to a reducer function

see project 18-redux-start

can be used outside of react, so any js project can use it

## steps

in store/index.js
- create a store
- create a reducer
- export store

provide store to the react app
- in src/index.js
  - import { Provider } from 'react-redux'
  - import store from './store/index'
  - root.render(<Provider store={store}><App /></Provider>);

using redux data in react components
- in src/components/Counter.js
  - import { useSelector } from 'react-redux';
    - useSelector is a custom redux hook
    - useStore also exists
  - consume useSelector
```
// param is a fn to retrieve the selected state
// useSelector automatically setup the subscription
const counter = useSelector(state => state.counter);
```

how can we change data -> dispatch actions
- in src/components/Counter.js
  - import { useSelector, useDispatcher } from 'react-redux';
  - consume useDispatcher:
    - const dispatch = useDispatch();
  - add the Handler that interact with the dispatcher fn and that will be wired to onClick actions

```
  const incrementHandler = () => {
    dispatch( { type: 'increment'})
  }

  const decrementHandler = () => {
    dispatch( { type: 'decrement'})
  }
```

## attaching payloads to Actions

action can contain data, just an extra property on action objects

## working with multiple state properties

toggle button, toggleCounterHandler

- add the extra data in
- in the component: useSelector can take 

## how to work with state

object returned in the reducer will not be merged but override the existing state

NEVER MUTATE the exisinting state => object or array are references
-> never change the existing state

## redux toolkit

see project 18-

```
npm install react-redux
npm install @reduxjs/toolkit
```

## redux side effects, async tasks

project: 19-redux-react-advanced-http-devtools

reducers must be pure, side effect free, synchronous functions
2 options:
-> use side effects in components
    option 1: in component create a new state object -> not good code so will not be used
        [option1 code](https://github.com/academind/react-complete-guide-code/tree/19-advanced-redux/code/zz-suboptimal-example-code)
        issue:
            - the logic is duplicated
            - the transformation of the data happens in the components
            - the reducers dont do anything
    option 2: use sideEffect in App.js
        - COMPONENT
-> inside the action creators
    - thunk: a function that delays an action until later
    - an action creator function that does NOT return the action itself but another function which eventually returns the action
    - COMPONENT IS LEAN -> the hard work is in the redux files

## redux dev tools

- add browser extension in chrome

### class based redux components

use connect of redux iso react-hooks as they are not available in class based components

```
import { Component } from 'react'
import classes from './Counter.module.css';
import { connect } from 'react-redux';

class Counter extends Component {
  incrementHandler() {
    this.props.increment();
  }

  decrementHandler() {
    this.props.decrement();
  }

  toggleCounterHandler() { }

  render() {
    return (
      <main className={classes.counter}>
        <h1>Redux Counter</h1>
        <div className={classes.value}>{this.props.counter}</div>
        <div>
          <button onClick={this.incrementHandler.bind(this)}>Increment</button>
          <button onClick={this.decrementHandler.bind(this)}>Decrement</button>
        </div>
        <button onClick={this.toggleCounterHandler.bind(this)}>Toggle Counter</button>
      </main>
    )
  }
}

// useSelector equivalent
const mapStateToProps = (state) => {
  return {
    // counter anme is up to the developper
    counter: state.counter
  }
}

// useDispatch equivalent
const mapDispathToProps = (dispatch) => {
  return {
    increment: () => dispatch({ type: 'increment' }),
    decrement: () => dispatch({ type: 'decrement' }),
  }
}

export default connect(mapStateToProps, mapDispathToProps)(Counter);
```

