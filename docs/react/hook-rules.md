# react hooks


## examples

useState
useEffect
useReducer
useContext
there are more hooks

## rules

- rule1: must only call react hooks in react function
  - react component functions
  - custom hooks (covered later)
- rule2: only call them at top level
  - dont call it in a nested function
- rule3: for useEffect
  - always add everything you refer to in the useEffect fucntion, unless if there is a good reason to do so.