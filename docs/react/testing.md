# react testing

section 26

## tool

- jest
- react testing library

## unit tests

- App.test.js

[course examples](https://github.com/academind/react-complete-guide-code/tree/26-testing)

## run

npm test

## tests

3 a's:
- arrange: setup
- act -> do the thing
- assert -> look at the output

## test suite

## Mocks

- we dont want to send the data to the server
- we miight insert data into a db, etc

option 1: dont send a request
    - override fetch with a dummy function
    - also required for local storage
option 2: add a dummy server

[jest](https://jestjs.io)
[test library](https://testing-library.com/docs/react-testing-library/api)

[role](https://www.w3.org/TR/html-aria/#docconformance)