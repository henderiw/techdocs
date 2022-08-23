# react typescript

section 27

[course examples](https://github.com/academind/react-complete-guide-code/tree/27-react-typescript)

[react typescrpt](https://www.typescriptlang.org/docs/handbook/react.html)

## what is typescript

extends javascript

adds static typing to javascript -> to prevent errors
javascript is dynamically typed

DOES NOT RUN in the broser
-> we need to compile TS to JS to run in the browser

## install

npm install typescript

compile

npx tsc
-> requires a configuration file

npx tsc with-typescript.ts

## react project configured for typescript

```
npx create-react-app <my-app>  --template typescript
```

## tsconfig.json

- compiler configuration: see the official docuementation
  - target: the target js code -> es5 (broad browser support
    - there could be another step like using babel
  - libraries that are used
    - default dom types like HTMLInputElement
  - allowJs: allow plain js file for mixed project
  - strict: true -> sticted possible settings
  - jsx is supported