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
  - Components:
    - Authentication Components: identity management + (Database)
    - Consent Server: displays the scope of the info you want to expose
    - Token Management: (Database) -> to be requested for validation of revokation
  - Offers several endpoints:
    - /authorize (standardized)  GET -> authorization code (for authorization code grant) or aaccess token (for implicit grant)
    - /token (standardized) POST Authorization - Basic clientId:clientSecret
      - Acces token and refresh token (for authorization Code grant, client credentials and reosurce owner password credentials grant)
    - /verify (not standardized) only internally accessible by Resource Resource Server
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

## endpoints:

- Authorization Endpoint (authorization server)
  - /authorize (URL can be different) GET
    - Input Query Parameters:
      - state -> to correlate several requests from the client
      - scope -> opetional (type of resource requested by the client)
      - response_type -> mandatory (which type of response you want to have authorization code or access token)
      - client_id -> identification of the client (registered prior to any interaction)
      - redirect_uri -> redirect endpoint/URI of the client, who receives the output (Authorization Code or Access Token)
    - Output
      - Authorization Code(for authorization Code Grant)
      - Access Token (for implicit grant)
    - Delivered via query parameters in the redirect URI
- Token Endpoint (authorization server)
  - /token POST Authorization: Basic {clientID}:{client Secret}
  - Input Query Parameters:
    - grant_type -> dependends on the flow
    - code -> dependends on the flow
    - client_id (required)
    - redirect_uri (required)
  - Output:
    - Access Token and Refresh Token (for authorization Code grant, client credentials and reosurce owner password credentials grant)
  - (Implicit grant does not use the token endpoint)
- Redirect Endpoint (client)
  - Redirect URI, GET
  - Input Query Parameters
    - state
    - scopes
    - code
- Resource Endpoint (resource server)
  - /api Autorization: Bearer {AccessToken}
  - Access Token and Refresh Token (for authorization Code grant, client credentials and reosurce owner password credentials grant)


## OAUTH TOKEN

- Have a validity and are able to access a resource (see paris subway station)
- Holder of the token has the access rights -> we need to keep them confidential
  - use them with encryption
  - stored in the DBASE of the authorization provider
  - no encoded user data
- Types
  - Access Token (AT) -> Bearer Token
    - The identity is no longer validated by the ressource server
  - Refresh Token (RT) -> Validaty is > Access Token
    - allows to refresh access tokens
    - stored and send by the client to the token endpoint 
      - NEVER send to the resource server
      - only used between client and Auth server
  - Authorization Code (code)
    - provided by the Authorization server and send to the client
    - info about the successfull authentication (few minutes valid -> to allow to request for an access token)
    - NEVER send to the resource server

## credentials

- Resource Owner credentials
- Client Credentiaals: CLientID & CLient Secret
  - used in client registration
- Access token:
  - can be seen as a credential (to be kept secret in a secure )
- Refresh Token:
  - to be kept secret- to refresh access token
- Authorization Code:
  - to get an access token

## client registration

- register a client to the Oauth Provider
  - provide
    - redirect URI
    - required scopes
  - consumes:
    - client ID
    - client Secret

## Oauth flows

per flow there is a grant type

- authorization code grant (most secure)
  - client needs a secure storage for client ID and Client Key
  - Also called 3 legged because it checks the identity of 3 actors
    - Auth Server by client using CERT/URL
    - Resource Owner by Auth Server by username/password
    - Client by Auth Server using client SECRET/KEY using HTTP Authorization field
	- Used when secure storage be provided by the client, like a server side client app
		most secure:
		- identity of ressource owner/client/auth server can be guaranteed
		- convenience: longer refresh times
	- steps
  	- 1: get autorization code
  	- 2: get the token
  	- 3: use the token to access a resource
- implicit flow
  - client cannot store e.g. client side JAVASCRIPT
  - shorten token validaty (access token cannot be refreshed)
  - Usage: mobile apps
  - only access token, no refresh token; 
  - Does not access the token endpoint
  - reduced 
- client credentials grant (2 legged oauth)
  - client is also the resource owner
  - Only uses the token endpoint
  - Used when: 
    - client uses secure storage for client ID and client STORAGE
  - offers:
    - token renewal
- resource owner password credential 
  - resource owner cannot trust the password to the client
  - client can use the username and password of the resource owner
  - LIKE the PASSWORD ANTI-PATTERN
  - client does not store the username and password, just use it initially
  - offers:
    - token renewal
    - simple
    - reduced security
    - 

## Open ID connect vs OAUTH

OAuth: no unintended leakage of information about the resource owner to the app

OpenID Connect:
- standardizes how apps can access the attributes of the resource owner via a token and via a RESTful API and how this data is structured and organized. 
- Extends the authorization code flow, introduces new tokens and standardizes some endpoints. OpenID Connect is a solution that can be applied in many environments, on many devices, and with many different products. 
- OpenID Connect is realized as an extension of OAuth, as a so-called OAuth profile


## Facebook worksheet

- client registration

https://www.developers.facebook.com
-> create an app
-> register a product: facebook login, redirect URI needs to end with a /
-> URL encode redirect URI
https%3A%2F%2Fsrldocs.henderiw.be%2F
-> required to get the code query parameter from the URL

- authorization Endpoint

https://www.facebook.com/v8.0/dialog/oauth?client_id=478104333841770&redirect_uri=https%3A%2F%2Fsrldocs.henderiw.be%2F&state=19283746567445

state -> needs to be unique in the app

response:

https://srldocs.henderiw.be/?code=AQBNj1uGzXGFdPiYOH160milCz2NN4E9Ii4yM2mmOgW7XA2B1-X2p14rmtylFdPlxhKBD-Y-Yo6clSgOWWrUhp_8fJA1rQsV_nqyJBZceAkmZPROVAMHnZvByR9Mvs4l93un9fhf-DvgX1K1KwTazQXx6H61b_zPTl6oMDDnRKLi7QpM72CF05tkjOzU6rT7j2pBeK6DV0mbVd-exwZE7SyveCUg612phm9evaKKWXu8fADoclj6GuxtgZxtbEgc_3jr1-evCq3PiH-5ALFdPvEPxbTaoJtJzDuFVmddO6BQUUYbLga7NqkBsp2h5hATZpBn8yEUPl_023GsBPTXxKzuA3J2iNbhoTPkOuYEGWyXmsH9v_SV7TdCg6BBTFYusGY&state=19283746567445#_=_

- token Endpoint

facebook does a GET iso a POST

curl -ik "https://graph.facebook.com/v8.0/oauth/access_token?redirect_uri=https%3A%2F%2Ftest.henderiw.be%2F&client_id=478104333841770&client_secret=d23caf8f9076d7d0e066536c4e3cdbd8&code=AQBNj1uGzXGFdPiYOH160milCz2NN4E9Ii4yM2mmOgW7XA2B1-X2p14rmtylFdPlxhKBD-Y-Yo6clSgOWWrUhp_8fJA1rQsV_nqyJBZceAkmZPROVAMHnZvByR9Mvs4l93un9fhf-DvgX1K1KwTazQXx6H61b_zPTl6oMDDnRKLi7QpM72CF05tkjOzU6rT7j2pBeK6DV0mbVd-exwZE7SyveCUg612phm9evaKKWXu8fADoclj6GuxtgZxtbEgc_3jr1-evCq3PiH-5ALFdPvEPxbTaoJtJzDuFVmddO6BQUUYbLga7NqkBsp2h5hATZpBn8yEUPl_023GsBPTXxKzuA3J2iNbhoTPkOuYEGWyXmsH9v_SV7TdCg6BBTFYusGY&state=19283746567445#_=_"

- resource access:

curl =H "Accept: application/json" -H "Authorization: Bearer <access token>" "https://graph.facebook.com/me"

## linkedin

see worksheet

## google

