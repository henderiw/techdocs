# react effect

section: 10
project: 04-effect -> login scenairio with local storage
file: App.js

## What is it

What is an effect?
- render the UI and reredener the UI based on changes -> event, user interface
- evaluate & render JSX
- manage state & props
- react to user events and input
- re-evaludate component upon State & prop changes

side effects is anything else
- prime focus is not to render UI
- timers
- sending http requests to backend servers
- store date in browser storage

the are done outside -> should not go into the component functions
 this is done using the useEffect Hook
 - 1st argument: a fn that shoudl be executed AFTER every component evaluation IF the specified dependencies changed
 - 2nd argument: dependencies (array)

## how

useEffect hook
- 1st argument: function that should be executed AFTER every component evaluation IF the specified dependencies changed 
  - at startup this fn will run
  - after they run when dependencie change
- 2nd argument: dependencies as an array

runs:
- every time the component runs if you have an empty array
- once at startup if depencies
- every time the dependencies change
- with cleanup, cleanup runs NOT before the first site effect execution

## example -> authenticated status is kept when the user login's again (no dependencies)

use browser local storage
- the data storage is not rendering the UI, the UI update is a side effect 

steps:
- add useEffect in react import
- add the useEffect, which looks at the localstorage, to see what to do
- given we have no dependencies this only runs at startup but this is what we want

```
// only runs when dependencies change -> at startup this will run
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

## Example run effects with dependencies

see 04-effects -> login scenario with local storage
login.js

useEffect to restructure the evaluation logic in email/password with 1 logic, and will be used when either one chnages

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

## what to add and not to add as dependencies

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

## example with cleanup

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