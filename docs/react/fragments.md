## react

## fragments

section: 09
project: 03-user-input
file: App.js

-> cleaner code, less div

- JSX limitation
  - if we have adjacent root level elements we get an error
    -> option1: workaround is mapping it into a div or any element
        we can end up with div soup
    -> option2: use an array but this is getting other challanges       
        -> we need a key on all the element in a list of data
        -> we could use hardcoded keys
        -> we could use <> </> works if the project is setup 
    -> option 3: creating a wrapper component 9see (03-user-input)
- option 3 comes from react -> React.Fragment
  - see components/Helpers/Wrapper