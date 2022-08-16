# react refs

section: 09
project: 03-user-input
files: 
- public/index.html
- components/Users/AddUser.js

## what

- get access to other dom elements and work with them
- e.g. curently in AddUSer we update the state with every key stroke is a bit to much
- with refs we can setup a conn between a html element and other js code
- called UNCONTROLLED component -> value of the input is not controlled by react

# how

- useRef hook
- useRef is only usable in components
- useRef:
  - takes a default value
  - returns a value/element nameInputRef/ageInputRef
- Connect to the html element using the ref prop:

```
<input
    id="username"
    type="text"
    ref={namedInputRef}
/>
```

- the first time react reaches the code -> the ref is set to the native html real dom element
- ref is an object, current is the actual value which is the real dom
- you can manipulate it but you should not manipulate it, readin is fine
- read current value
    - nameInputRef.current.value

# benefit

we can access to the value when the submit button is pressed, rather than using every keystroke

-> we no longer use the state to get the values
-> we can get rid of the states, state up dtaing functions

resetting is lost -> 2 options
- use state
- manipulate the dom() -> here it is ok but should not be used in general -> use it in rare cases

If you just need to read the a value, state is too much
