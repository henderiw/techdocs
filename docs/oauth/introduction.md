# oauth

- how to allow 3rd party apps to access my resources
  - password anti-attern
  - oauth 2.0:
    - [RFC6749](http://tools.ietf.org/html/rfc6749) -> RFC for delegating authorization for accessing ressources via HTTP
    - delegating access to the mobile app by providing a token (limited/subset of data (scope), finite period of time)
    - to obtain the token -> you need to login to the authserver
    - advantages:
      - revoke the stored token on the authentication server
- overall info:
  - 3rd party: client
  - oauth is used for delegation
  - 

## actors

- OAuth provider/Server Authorization server
  - Authentication Components: identity management + Database
  - Consent Server: displays the scope of the info you want to expose
  - Token Management: database -> to be requested for validation of revokation
- Resource Provider:
  - Make a a protected resource available (web API), that offer protected data
    - Ensures only autenticated resource get exposed
    - oAUTH access token, checks the validaty of the access token
- Resource Owner: user
  - Owner of the protected resource: user of twitter/gmail
  - Delegates the access rights to the 3rd party
- Client or Cloud App/Mobile App:
  - Attempt to access a resource hosted on the Resource Provider
  - gets and holds access Token and refresh tokens (stores them)
  - should not hold the password of the resource owner -> PASSWORD ANTI-PATTERM