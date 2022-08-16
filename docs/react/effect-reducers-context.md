# react

## effects

What is an effect?
- render the UI and reredener the UI based on changes -> event, user interface
- evaluate & render JSX
- manage state & props
- react to user events and input
- re-evaludate component upon State & prop changes

side effects is anything else
- timers
- sending http requests to backend servers
- store date in browser storage

the are done outside -> should not go into the component functions
 this is done using the useEffect Hook
 - 1st argument: a fn that shoudl be executed AFTER every component evaluation IF the specified dependencies changed
 - 2nd argument: dependencies (array)

see 04-effects -> login scenairio with local storage
App.js

steps:
- add useEffect in react import
- add the useEffect, which looks at the localstorage, to see what to do
- given we have no dependencies this only runs at startup but this is what we want

```
// only runs when dependencies change -> at strtup this will run
  // since we dont have dependencies -> this code runs only at startup
  useEffect(() => {
    const storedUserLoggedInInfo = localStorage.getItem('isLoggedIn');

    if (storedUserLoggedInInfo === '1') {
      setIsLoggedIn(true);
    }
  }, []);

  const loginHandler = (email, password) => {
    // We should of course check email and password
    // But it's just a dummy/ demo anyways
    localStorage.setItem('isLoggedIn', '1');
    setIsLoggedIn(true);
  };

  const logoutHandler = () => {
    localStorage.removeItem('isLoggedIn');
    setIsLoggedIn(false);
  };
```

### run effects with dependencies

see 04-effects -> login scenairio with local storage
login.js

```
  useEffect(() => {
    setFormIsValid(
      enteredEmail.target.value.includes('@') && enteredPassword.trim().length > 6
    );
  }, [enteredEmail, enteredPassword])
```

-> we rerun if a depencies change
-> how do we see the depencneis: see the logic in useEffect
    - enteredEmail, enteredPassword
    - alse the setFormIsValid fn but this is never used

MIGHT BE CONFUSING:
- here we dont do anything with http or local storage
- here it is a site effect of the user putting data in the UI
- useEffect is used as a site effect of the user inputting data

What to add & Not to add as Dependencies
In the previous lecture, we explored useEffect() dependencies.

You learned, that you should add "everything" you use in the effect function as a dependency - i.e. all state variables and functions you use in there.

That is correct, but there are a few exceptions you should be aware of:

You DON'T need to add state updating functions (as we did in the last lecture with setFormIsValid): React guarantees that those functions never change, hence you don't need to add them as dependencies (you could though)

You also DON'T need to add "built-in" APIs or functions like fetch(), localStorage etc (functions and features built-into the browser and hence available globally): These browser APIs / global functions are not related to the React component render cycle and they also never change

You also DON'T need to add variables or functions you might've defined OUTSIDE of your components (e.g. if you create a new helper function in a separate file): Such functions or variables also are not created inside of a component function and hence changing them won't affect your components (components won't be re-evaluated if such variables or functions change and vice-versa)

So long story short: You must add all "things" you use in your effect function if those "things" could change because your component (or some parent component) re-rendered. That's why variables or state defined in component functions, props or functions defined in component functions have to be added as dependencies!

Here's a made-up dummy example to further clarify the above-mentioned scenarios:

import { useEffect, useState } from 'react';
 
let myTimer;
 
const MyComponent = (props) => {
  const [timerIsActive, setTimerIsActive] = useState(false);
 
  const { timerDuration } = props; // using destructuring to pull out specific props values
 
  useEffect(() => {
    if (!timerIsActive) {
      setTimerIsActive(true);
      myTimer = setTimeout(() => {
        setTimerIsActive(false);
      }, timerDuration);
    }
  }, [timerIsActive, timerDuration]);
};
In this example:

timerIsActive is added as a dependency because it's component state that may change when the component changes (e.g. because the state was updated)

timerDuration is added as a dependency because it's a prop value of that component - so it may change if a parent component changes that value (causing this MyComponent component to re-render as well)

setTimerIsActive is NOT added as a dependency because it's that exception: State updating functions could be added but don't have to be added since React guarantees that the functions themselves never change

myTimer is NOT added as a dependency because it's not a component-internal variable (i.e. not some state or a prop value) - it's defined outside of the component and changing it (no matter where) wouldn't cause the component to be re-evaluated

setTimeout is NOT added as a dependency because it's a built-in API (built-into the browser) - it's independent from React and your components, it doesn't change

### effect for cleanup

the current example executes on every key stroke
-> we dont want to send http req on all of this
-> also here state updating all the time might be to much
-> we could wait for a timer or so
THIS IS CALLED DEBOUNCING

```
useEffect(() => {
    // allows to avoid running in all keystrokes
    const identifier = setTimeout(() => {
      console.log('checking for validaty!')
      setFormIsValid(
        enteredEmail.includes('@') && enteredPassword.trim().length > 6
      );
    }, 500);

    // use effect alaways to return a fn
    // this is like a cleanup fn
    // does NOT run before the first site effect execution
    return () => {
      console.log('CLEANUP!');
      // clear the last timer before the new one is run
      clearTimeout(identifier);
    };
  }, [enteredEmail, enteredPassword])
```

### effect/site-effect summary

- runs every time the component runs if you have an empty array
- runs once at startup if depencies
- runs every time the dependencies change
- with cleanup, cleanup runs NOT before the first site effect execution

## how to manage more complex state with reducers

Another react hook

sometimes you have more complex state - e.g. multiple states, multiple ways of changing it or depndencies to other states
-> more complex to use, so dont use it by default

in login we have some dependencies
e.g. enteredEmail and emailIsValid have dependencies so we might want to manage them together

UPDATE state that is dependent on another state

- returns an array with 2 values
- 2 values
  - latest state snapshot
  - fn to update the state snapshot -> dispatches an action, will be consumed by the reducerFn (first argument)
    - reducerFn returns 



const [state, dispathFn] = useReducer(reducerFn, initialState, initFn);

- state: the state snapshot used in the component rerender/reevaluation cycle
- dispathFn: a fn that can be used to dispatch a new action (i.e. trigger an update of the state)
- - reducerFn (prevState, action) -> newState
  - a fn that triggered automatically once an action is dispatched (via dispatchFn()) - it receives the latest state snapshot and should return the new, updated state
- intialState
- a funtin to set the initial state


Adding Nested Properties As Dependencies To useEffect
```
In the previous lecture, we used object destructuring to add object properties as dependencies to useEffect().

const { someProperty } = someObject;
useEffect(() => {
  // code that only uses someProperty ...
}, [someProperty]);
This is a very common pattern and approach, which is why I typically use it and why I show it here (I will keep on using it throughout the course).

I just want to point out, that they key thing is NOT that we use destructuring but that we pass specific properties instead of the entire object as a dependency.

We could also write this code and it would work in the same way.

useEffect(() => {
  // code that only uses someProperty ...
}, [someObject.someProperty]);
This works just fine as well!

But you should avoid this code:

useEffect(() => {
  // code that only uses someProperty ...
}, [someObject]);
Why?

Because now the effect function would re-run whenever ANY property of someObject changes - not just the one property (someProperty in the above example) our effect might depend on.
```

### when to use useState or useReducer

useReducer:
- state becomes cumbersome, state dependencies
  
useState:
- the main state management tool -> you start here
- great for simple use cases

## context -> making state sharing easier

passing a lot of data between lots of components using props

06-usereducer-starting
in Apps.js

the props isAuthenticated/onLogout are just forwarded to MainHandler
Mainhandler just forwards it to Navigation component
-> props chains

component wide state storage -> context
app or component wide state

- add a directory store
- add file auth-context.js
- add the logic
- provider
  - wrapper <AuthContext.Provider>  -> is a component
  - useContext hook


setup a dynamic context which also fwd functions

in most cases you use props
when you just fwd information -> you should consider context

### context limitation

- cannot be used for Button as it would limit it to only login/logout -> props is better here
- not optimized for high frequency changes: multiple per second
    -> redux could be used for this


example: Input component is reusable so props is to be used iso context


## react hooks

useState
useEffect
useReducer
useContext

rules for the hooks:
- must only call react hooks in react function
  - react component fucntions
  - custom hooks (covered later)
- only call them at top level
  - dont call it in a nested function
- for useEffect, always add evenrything in the useEffect fucntion

## calling a function inside a component -> fwd refs

Usefull for focus input to errored cases, like is it email or password. And focus the error to it

-> imperative way to interact with a component
-> used rarely

refs cannot be used

hook: useImperativeHandle

pass 2 parameters

```
// ref is enabled later
useImperativeHandle(ref, () => {
    return {
        // focus is used outside
        // activate is used inside the component
        focus: activate
    };
})
```

input of the components

```
// besides ref we can use a 2nd parameter
const Input = (props, ref) => {

}
```


export component with a special parameter
this allows to expose the ref

```
const Input = React.forwardRef((propos, ref) => {
    ...
});


