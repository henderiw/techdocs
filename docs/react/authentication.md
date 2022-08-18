# react authentication

[firbase api](https://firebase.google.com/docs/reference/rest/auth)

## why

- authentication is needed if content should be protected

example:
- certain pages should not be accessabile to users who ar enot logged in
- db protection
- api endpoints

2 step:
- get access/ permission (email/passwrd -> check DB; server creates a permission token
- send request to protected resource with permission attached

response from server to client must
- server side sessions
  - works well when front-end and backend are tightly coupled
- authentication tokens
  - server should be stateless
    - get access/ permission (email/passwrd -> check DB; server creates a permission token (specific algorithm with a key only known by the server)
    - client can use the token to attach to future requests -> the server can verify it created it

[jwt](https://jwt.io)

## practial steps

store/auth-context.js
Auth/AuthForm.js
Layout/MainNavifation.js

- create user -> submithandler
  - get userinput through ref or state (key stroke)
  - validation user input
  - logic
    - login/logout
    - http
- user login
  - http, but similar logic
- context
- change user password
- redirect after login and password change -> usehistory
- logout
- avoid getting access/visit the pages if not loggedIn (navifation guards)
  - dynamic change routes based on login/logout -> CONDITIONAL ROUTES
- making the persistence
  - token will expire after every hour
  - we need to store it somehwere -> cookies or local storage
    - local storage is bad with cross side attacks
    - when logged in we also store the token in local storage (auth-context.js)
    - if logged in we need to check if the token exists
- auto-loggout
  - use expirationTime
  - store the expiration timer


[local storage versus cookies](https://academind.com/tutorials/localstorage-vs-cookies-xss)

[example code](https://github.com/academind/react-complete-guide-code/tree/22-authentication)