# react reducers

section: 10
project: 06-useredeucer-starting-project
file: Login.js

## what

sometimes you have more complex state
- multiple states, multiple ways of changing
- dependencnies to other states

UPDATE state that is dependent on another state

# how

- returns an array with 2 values
- 2 values
  - latest state snapshot
  - fn to update the state snapshot -> dispatches an action, will be consumed by the reducerFn (first argument)
    - reducerFn returns 

const [state, dispathFn] = useReducer(reducerFn, initialState, initFn);

- state: the state snapshot used in the component rerender/reevaluation cycle
- dispathFn: a fn that can be used to dispatch a new action (i.e. trigger an update of the state)
- reducerFn (prevState, action) -> newState
  - a fn that triggered automatically once an action is dispatched (via dispatchFn()) - it receives the latest state snapshot and should return the new, updated state
- intialState
- a function to set the initial state

## example enterEmail and emailIsValid belong together

combine enterEmail, emailIsValid

```
  // email state with useReucer -> manage 1 state
  // emailReducer -> reducerFn; data is coming outside so we can define this fn somewhere else
  // { value: '', isValid: false } -> initial value
  const [emailState, dispatchEmail] = useReducer(emailReducer, {
    value: '',
    isValid: false,
  });
```

reducer function can be external

```
const emailReducer = (state, action) => {
  // handle action
  if (action.type === 'USER_INPUT') {
    return { value: action.val, isValid: action.val.includes('@') };
  }
  if (action.type === 'INPUT_BLUR') {
    // value: state is the latest state
    return { value: state.value, isValid: state.value.includes('@') };
  }
  // return state as an Object
  return { value: '', isValid: false };
}
```
dispath action -> action is an Object

```
const emailChangeHandler = (event) => {
    // dispatches an action -> normally an Object
    dispatchEmail({ type: 'USER_INPUT', val: event.target.value });
  };
```

dispath action -> action is an Object (another action)

```
const validateEmailHandler = () => {
    // uses the reducedsiaptacherFn
    dispatchEmail({ type: 'INPUT_BLUR' });
  };
```

combined with useEffect _. looking at isValid

```
  // object destructuring with alias assignment
  // is here to avoid running the useEffect only when the input is valid
  const { isValid: emailIsValid } = emailState;
  const { isValid: passwordIsValid } = passwordState;


  useEffect(() => {
    const identifier = setTimeout(() => {
      console.log('Checking form validity!');
      // is here to avoid running the useEffect only when the input is valid
      setFormIsValid(emailIsValid && passwordIsValid);
    }, 500);

    return () => {
      console.log('CLEANUP');
      clearTimeout(identifier);
    };
  }, [emailIsValid, passwordIsValid]); // is here to avoid running the useEffect only when the input is valid

```

### when to use useState or useReducer

useReducer:
- state becomes cumbersome, state dependencies
  
useState:
- the main state management tool -> you start here
- great for simple use cases