# api security

## terminologies/concepts

API versus UI -> API machines; UI for humans
API styles: GRPC (microservices), REST (web), GRAPHQL (lookup speed)
NetworkSecurity/AppSecurity/InfoSecurity
Confidentiality (who can access)/Integrity (data is ok)/Availablity (ddos, etc)
Trust Boundaries -> STRIDE:
    - Spoofing: Pretending to be somebody else
    - Tampering: Altering data, messages, or settings you’re not supposed to alter
    - Repudation: Denying that you did something that you really did do
    - Information disclosure: Revealing information that should be kept private
    - Denial of service: Preventing others from accessing information and services
    - Elevation of privilege: Gaining access to functionality you’re not supposed to have access 
encryption
ddos
authentication factors
    - something you know: a password
    - something you have: a key or a physical device
    - something you are: biometric, fingerprint, etc
access control:
    - identity based
    - capability based
audit log


## attacks/concepts:

- SQL injeciton attack
    - what: if the data you get from the web is used without proper evaluation, the sql commands can do wrong things
    - prevention: evaluate the parameters you use to access the DB -> validate (prevent spaecial characters)

- POLA principle of least authorithy/priviledge
    - what: all users and processes in a system should be given only those permissions that they need to do their job
    - prevention: provide users that access the DB

- XSS: reflected corss-site scripting
    - what: script that is used as output and used by an attacker
    - prevention: output parameter evaluation
        - enforce: application/json
        - evaluate output
        - use proper Content-Type header and never assume the default settings
    - header responses:
        - X-XSS-Protection: whether to block or ignore suspected XSS attacks
        - X-Content-Type-Options: 
        - X-Frame-Options: Set to DENY to prevent your API responses being loaded in a frame or iframe.
        - Cache-Control and Expires: Controls whether browsers and proxies can cache content in the response and for how long.

- SOP: same origin policy
    - what: web borser can read cookies when accessign resources from the same origin/site

- Session fixation attack
    - what: login and use the session token of another user to get access to the victom
    - prevention: create a new session upon login

- Cross-Site Forgery attacks
    - what: if cookies are set they are also set on a link when clicking on them
    - prevention:
        - Content-type: application/json -> ensure javascript -> triggers same site policy protection
        - never alter state on GET request, etc
        - Set SameSite=lax or strict
        - hash based double-submit cookies: 
            - Set-Cookie: csrfToken without httpOnly set -> send back in X-CSRF-Token header
            - server checks if both token are equal
        - other option is generate a hash based on a key the server only knows but using timing 

- Cross-origin resource sharing (CORS) allows some cross-origin requests to be permitted

## web concepts

- HTTP basic Authentication:
    - password db: can also use LDAP
        - use a hash with a salt/random key
    - request header:
        - Authorization: base64 encoding
    - response header:
        - Strict-Transport-Security
        - max-age
    - needs HTTPS
    - issues:
        - password can leak
        - password verification is expensive
        - user experience with default login is not great
        - browsers rememeber the passwords
- Token based authentication:
    - UI:
        - json request can only be made using javascript
        - browsers use SOP (so single site policy logic)
        - form can pop up based on 401 unauthorized status
        - browsers remember username/password for the same site and resend them
    - dedicated login endpoint with username/password for now
    - session token: short-lived token that is intended to authenticate a user while they are directly authenticating with a site
    - token is stored in a db, storage options
    - Option1: user controlller for basic authentication (password db) followed by login endpoint/token controller (token store)
        - statefull
        - session cookies with Set-Cookie header
            - associated with a domain
            - Cookie attributes
                - Secuure: use https only
                - httpOnly: cannot be read by Javascript -> always set this
                - SameSite
                - Domain:
                - Path:
                - Expires and Max age: if set we call them persistent cookies as they will be stored based on these parameters; session cookies dont set this, so they will not be stored
        - validating session cookies
            - protect agains CSRF attacks
        - implement logout
    - Option 2: modern token based authentication 9HTML5 web storage and bearer authenitcation
        - allows CORS: cross-origin resource sharing
        - preflight request HTTP OPTIONS
        - response headers:
            - Access-Control-Allow-Origin: (regular/preflight)
            - Access-Control-Allow-Headers: (preflight) -> Content-Type, Authorization, X-CSRF-Token
            - Access-Control-Allow-Methods: (preflight) -> GET, POST, DELETE
            - Access-Control-Allow-Credentials: (regular/preflight) -> true
            - Access-Control-Max-Age: (preflight)
            - Access-Control-Expose-Headers: actual
        - don't use cookies -> use sameSite for cookies but only on single site apps
            - WWW-Authenticate is used in response header
        - use a tokenID with entropy/random nbr generation
        - deleting tokens from the DB using expiry time
        - UI storage for webtokens
            - LocalStorage and sessionStorage (not shared between browser tabs and windows -> different tab/window is relogin)
        - Need to add additional measures in the UI for protection against XSS
        - Protect the DB
            - avoid direct access by external clients
            - hash tokens
            - authenticate tokens using HMAC -> appended to the token but not stored in the DB (recomputed)
            - store the HMAC key in a keystore
            - encrypt sensitive data
    - Option 3: self-contained tokens and JWTs
        - store the token in the client -> stateless tokens; the api server decodes the token and parse the JSON to recover the session attributes
        - protecting JSON tokens using HMAC
        - JWT became a standard in IETF RFC7519, RFC7515/7516/7517/7518
        - JOSE: JSON Object signing and Encryption
            - Headers
                - alg
                - key
            - Claims
                - iss: Issuer
                - aud: Audience
                - iat: Issued-At
                - nbf: Not-Before
                - exp: Expiry
                - sub: Subject
                - jti: JWT ID
            - HMAC tag
            - Issues with JSE:
                - remove the Header: headless JWT -> calculate on the server
                - store the algorithms as metadata associated with a key
        - alternative to JOSE is PASETO
        - Validating a signed JWT:
        - Encrypted JWT:
            - header.<encrypted- key>.init-vector.ciphertext.auth-tag
        - revoke the token
            - add minimal state in a DB (no longer stateless)
            - reauthenticate regularly
- OAuth/OIDC:
    - allows the application to request the scopes they require and then the API can ask the user if they consent
    - see outh2 info
    - callback uri:
        [android app redirect](https://developer.android.com/training/app-links)
        [ios app redirect](https://developer.apple.com/ios/universal-links)
    - refresh token:
        - allows for short lived sessions - configure the AS to ensure this is only used once
    - validating an access token
        - token introspection: use the introspection endpoint og the AS server
            can be cached but security is worse and revokation will take longer
            comon LDAP DB
        - use HTTPS
        - token revokation
        - JWT access tokens
            - use JWK over HTTPS between the AS and RS to retrieve the crypto info
            - decoding is independent, jsut crypto is exchanged
        - encrypted JWT access token
        - decrypt token in AS
- SSO: have a single auth server for various applications
    - common session cookie accross applications
    - warning: it is tempting to reuse a single access token to provide many different API(s)
- OIDC
    - Oauth primary focus: delegated third party access to API(s) rather then user identity and session management
    - OIDC extends OAUTH:
        - retrieve identity: email, name, etc
        - ask for a client if they are authenticated 
        - allows to user to logout of all sessions at once
    - OIDC combines AS and RS for user info
    - ID token: only for identity, not for scope
        - ID token is a signed and optionally encrypted JWT that contains identity and authentication claims about a user
    - Dont use ID tokens to access an API

- origin URL: combination of protocol, host and port -> no port is used 80 for http and 443 for https

- RBAC:
    - user
    - role: static or dynamic (during working hours)
    - permissions -> operations


## key design aspects

- ratelimiting/ddos -> prevented before the app (apiserver, ddos, etc), but per user ratelimiting can be added in the app
- input validation -> injection attacks, buffer overflows, regex attacks etc
- provide least privelidge access to resources (e.g. dedicated user for db) -> POLA
- produce safe outputs (application/json)-> provide info on technology used, prevents XSS
- authentication -> coordinate with an auth server (AS in oauth2)
- audit logging right after authentication
- access control -> 403 (access forbidden)
    - permission: mandatory access control
    - scopes: delegated access control


## clients

browser
desktop app
mobile app
cli tool
app api (internal/microservice)
app api (external)
iot