# oidc

oidc 1.0 is a simple identity layer on top of Oauth 2.0.
Enables clients:
- to verify the identity of the End-User based on authentication performaned by an authorization server

End User = RO (resource Owner)
RP (Relying Party) =  App/CLient
OP (OpenID Provider) = AS (Authorization server)

## specification

- [rfc6749 oauth2](https://www.rfc-editor.org/rfc/rfc6749.html)
- [rfc6750 oauth2 bearer token usage](https://www.rfc-editor.org/rfc/rfc6750.html)


scope = openid in authorization request
id token = JWT
RP obtains information about the OpenID Provider: (normally based on discovery information)
    - Authorizatopn endpoint
    - Token Endpoint
RP has obtained sufficient credentials and provided information needed to use the OpenID Provider (normmally based on dynaic client registration)

## ID token

claims in IDToken

- iss (required): issuer identifier (Url)
- sub (required): subject identifier -> unique id of the user within the issuer (256 ASCII chars)
- aud (required): audience (oauth2.0 client id identifier)
- exp (required): expiration time of the ID token
- iat (required): time when the JWT was issued
- auth_time: time when end- user authentication occured
- nonce: mitigate against a replay attack
- acr (optional) authentication context class reference
- amr (optional) authentication methods references
- azp (optional) authorized party

there can be other claims

-> signed using JWS
-> signed and encrypted using JWS and JWE (optional)

example

```
{
   "iss": "https://server.example.com",
   "sub": "24400320",
   "aud": "s6BhdRkqt3",
   "nonce": "n-0S6_WzA2Mj",
   "exp": 1311281970,
   "iat": 1311280970,
   "auth_time": 1311280969,
   "acr": "urn:mace:incommon:iap:silver"
}
```