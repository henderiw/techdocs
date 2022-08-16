# react redux

section: 18
project: 
file: 

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
- can become complex -> dependns on app we are building
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

