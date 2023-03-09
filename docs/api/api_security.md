# api security

other books:
- Secure by Design by Dan Bergh Johnsson, Daniel Deogun, and Daniel Sawano (Manning, 2019).

- api need to identify the user/entity that interacts with it
- level of access/operations have different tradeoffs
- audit log records details of significant actions taken on a system -> allows to see who did what and when

## what is an api

API defines a set of operations that a caller is permitted to use
- boundary between a piece of SW
- handles requests from clients (web, mobile, iot ot other apis)
- an api can interact with backend apis

### api styles

- rpc: remote procedure calls (e.g. grpc) -> microservices
- rmi: remote method invocation (e.g. cobra) -> not very popular
- REST: REpresentational State Transfer)
- GRAPHQL: efficient quering of large datasets

## api security

- infosec: concerned with the protection of information over its full life cycle from creation, storage, transmission, backup, and eventual destruction.
    - define security goals and threats
    - protect the api using access controls
    - secure info using applied cryptography
- network security: protection of data flowing over a network and prevention of unauthorized access to the network itself
    - firwalls, loadbalancers, reverse proxies
    - https
- application security: ensures that software systems are designed and built to withstand attacks and misuse
    - coding
    - common sw vulnerabilities
    - how to store and manage system and user credentials to access the API(s)

## elements of api security

- assets: 
    - data: user info
    - server/OS on which the application runs
- security goals:
    - CIA triad:
        - confidentiality: Ensuring information can only be read by its intended audience
        - integrity: Preventing unauthorized creation, modification, or destruction of information
        - availability: Ensuring that the legitimate users of an API can access it when they need to and are not prevented from doing so
    - others:
        - accuntability: who did what
        - non-repudation: not being able to deny having performed an action
- environment and thread models
    - A threat is an event or set of circumstances that defeats the security goals of your API. For example, an attacker stealing names and address details from your customer database is a threat to confidentiality.
    - Threat modeling is the process of systematically identifying threats to a software system so that they can be recorded, tracked, and mitigated.
        STRIDE:
            - Spoofing: Pretending to be somebody else
            - Tampering: Altering data, messages, or settings you’re not supposed to alter
            - Repudation: Denying that you did something that you really did do
            - Information disclosure: Revealing information that should be kept private
            - Denial of service: Preventing others from accessing information and services
            - Elevation of privilege: Gaining access to functionality you’re not supposed to have access to

## security mechamisms

- Encryption: ensures that data can’t be read by unauthorized parties, either when it is being transmitted from the API to a client or at rest in a database or filesystem
- Authentication: ensuring that your users and clients are who they say they are
    authenitcation factors
        - something you know: a password
        - something you have: a key or a physical device
        - something you are: biometric, fingerprint, etc
- Authorization/access control: ensuring that every request made to your API is appropriately authorized.
    - identity based: access control based on who you are
    - capability baed
- audit logging: ensure that all operations are recorded to allow accountability and proper monitoring of the API
- rate limiting:  prevent any one user (or group of users) using all of the resources and preventing access for legitimate users

## chapter 2

[github book](https://github.com/NeilMadden/apisecurityinaction)

### general ways to deaal with security attacks

- injection attack
    - validate user input
    - SQL least privelidge
    - produce safe output
        - error code should not expose internal information
        - XSS attacks
        - headers:
            - X-XSS-Protection: Tells the browser whether to block/ignore suspected XSS attacks.
            - X-Content-Type-Options: Set to nosniff to prevent the browser guessing the correct Content-Type.
            - X-Frame-Options: Set to DENY to prevent your API responses being loaded in a frame or iframe.
            - Cache-Control and Expires: Controls whether browsers and proxies can cache content in the response and for how long.
            - Content-Security-Policy
    
- rate limiting (DDOS)
    - response header: retry-after
- authenitcation -> userDB
    - username/password: RFC 7617 -> use encryption
        uses base64 encoding
    - store users in a db:
        password is using a hashign algorithm
- HTTPS:
    - reponse header: Strict-Transport-Security
- audit logging -> audit DB
    - SIEM: Security Information and Event Management)
- access control
    - 401: Unauthorized -> means actually unauthenticated
    - 403: Forbidden -> credentials are ok but access was not granted
    - permissions table 
    - the code for access control should ideally be made independent

- token based access:
    - session cookie authentication
        scope:
            - avoid having to add username/password for every call
            - add a dedicated login endpoint
            - token is time bound
            - protect against: Cross-Site Request Forgery (CSRF) 
            - authentication of browser-based clients hosted on the same site as the API
        issue of http authentication
            - password is used everywhere and chances of it being exposed grows
            - password verification is expensive and should be avoided
            - the default basic authentication browser dialog box is not nice
            - you cannot ask the browser easily to forget the password
        stored in a shared db indexed by token id
        webbrowser clients store the token in:
            cookies -> first party clients
                header: Set-Cookie
                cookie attributes:
                    - Secure: https only -> always set
                    - httpOnly:  -> always set (cannot eb read by javascript)
                    - samesite: 
                    - domain: -> avoid setting it
                    - path -> 
                    - expires and max-age -> to be avoided as they are stored persistenly
            token store:
                token: 
                    - username, expiry time, metadata
                    - returns an ID
            CSRF:
                GET should never alter state
                SameSite cookie: avoid sending cookie when that originate from the same domain
                Double-Submit cookie:
                    X-CSRF-Token
    - cookies with html5 web storage and the standard bearer authentication
        context:
            - allow CORS: cross origin resource sharing
            


