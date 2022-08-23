# react

## what is it react.js

a js script library for building user interfaces
- smooth transition
- react fast
a client side js library
- modern

[compare js to react](https://github.com/academind/react-complete-guide-code/tree/01-getting-started/code/react-vs-vanilla-js-example)

js -> imperative coding
react -> declarative programing
    - component = building block -> maintainable code -> do 1 thing well
    - abstracted interface on top of javascript


building single page applcations
-> content is presented differently to the user w/o requesting new content
-> js/react can manipulate the DOM, without doing a new request

components are build using
- classes


## other frameworks

- angular
  - component focussed
  - ships with many builtin features
  - builtin typescript
- vue.js
  - mix angular and react
  - component based
  - lot of feature, lesser than angular
  - core features like routing

## main concepts

- components: the basis of react
  - functional components
    - modern way of using react
  - class-based components: older way (section 13)
    - no reactHooks
    - state is a single object
    - single context per component
- fragments: 
  - avoids the div soap, cleaner way to the DOM
- portals: 
  - move the react component to another place in the DOM
  -  used for overlays like ErrorModals to get cleaner code
- refs: 
  - useRef react hook
  - getting access to native DOM/HTML elements
  - can be used to read a value (user input), can be an alternative to state. See Add User example
  - uncontrolled input components
- effect/side effect
  - useEffect react hook
  - effect: everything to render UI and User input
  - side effect: anything else, code in response to another action
    - timers
    - sending http requests to backend servers
    - local storage in browser
    - checking form validaty when user enters data in the UI
  - use case douncing
- reducers:
  - useReduce react hook
  - alternative to useState hook
  - used when state has dependencies or state is more complex
- context: (alternative to props)
  - useContext react hook
  - data is passed along to a final component
  - when to use props and when to use context
    - props: use state
    - context: app or component wide state
- redux: (redux-toolkit)
  - context disadvantages:
    - can become complex -> depends on app we are building
      - deeply nested context provider
  - performance
- custom hooks:
  - used for reusable code e.g.
- Performance optimization for react
  - React.memo(DemoOutput): could optimize the react reevalution, by comparing props and see if there is a demo
  - useCallBack: used to store fn to stop reevaluation of component and optimzie react
  - useMemo: used to avoid reevaluation complex functions

## react behind the scenes

section 12

[code](https://github.com/academind/react-complete-guide-code/tree/12-a-look-behind-the-scenes)

- react works with components
  - props (data from parent component)
  - state (internal data in a component)
  - context (component wide data)
- reactDOM -> what the user sees

react uses a virtualDOM

-> react determines how the component tree currently looks like and what it should look like
-> reactDom receives the differences (i.e. required changes) on them and manipulates the real DOM

react reevalutes the components whenever prpos, state or ctx changes
-> react executes component functions
-> a parent reevaluation will also reevaluate all children -> is this not creating to much work
  ->  React.memo(DemoOutput) allows to skip component reevaluation that avoids react component reevaluation is props dont change
  -> this has a cost since now react has to store props -> so it depends on the component if this is usefull
  -> a function if defined it is recreated -> this reevaluates the component
    because react compares props, bool works, fn does not work
  -> solution: useCallback: the fn are stored a fn in react storage to allow the comparison to succeed
only if changes happens the realDOM will be updated

so it does virtual DOM diffing

- useState/useReducer
  - react manages state
  - react initializes the state with default value when component is first run
  - react updates the state when the component is reevaluated, unless the component is removed from the DOM
    - this state update is scheduled, so not immediately executed, so react could postpone the update, the order is guaranteed though
    - This is why we need to use the function in order to process the order

- React.memo optimization
  - useMemo hook
  - store any kind of data -> store

```
const { items} = props;

const sortedList = usememo(() => {
  return items.sort((a, b) => a-b)
}, [items])
```

[example code](https://github.com/academind/react-complete-guide-code/tree/18-diving-into-redux)

## eco-system

- gatsby.js
- preact: smaller footprint
- [react native: Android/IOS](https://acad.link/react-native)
- [mern](https://acad.link/mern)