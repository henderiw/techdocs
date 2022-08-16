# react forms - user input



## why

complex -> multiple states
- one or more input are invalid
  - Action:
    - output input-specific error mesages & highlight problematic inputs
    - ensure form cant be submitted/saved
- all inputs are valid
  - Action:
    - allow form to be submitted/saved


When to Validate?
- when form is submitted 
  - pro: allows the user to enter a valid value before warning him/her
  - con: too late feedback
- when a input is losing focus
  - pro: allows the user to enter a valid value before warning him/her
    - very useful for untouched forms
  - con: too late
- on every keystroke?
  - con: warns to much/quickly
  - pro: if applied on invalid inputs, has the potential of providing more feedback

## fetching user input

2 options:
- listen on every keystroke -> use State 
- user a ref once the user is done

which to pick depends what you plan to do: see before

resetting user input 
-> better with the state
-> can be done using ref, but this is not a good practice

## validating user input

[hide js code](https://academind.com/tutorials/hide-javascript-code)

client side validation
- great for user experience, but server side is still required

validation provide feedback

## useReducer 

use reducer can also be used here
-> see example in the custom hook

## summary

[use form hook example](https://academind.com/tutorials/reactjs-a-custom-useform-hook)

3rd party library:
- formik

[code example](https://github.com/academind/react-complete-guide-code/tree/16-working-with-forms)