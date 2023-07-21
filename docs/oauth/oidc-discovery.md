# oidc discovery

There are 2 phases in the discovery:
1. discover the issuers -> this part is not widely implemented
2. provide discovery information on the OP from the issues


based on [Webfinger RFC7033](https://www.rfc-editor.org/rfc/rfc7033.html)
-> uses web linking based on URI(s)

webfinger protocol:
- request info about an identity
    - identified by a query target: URI

```
GET /.well-known/webfinger?
    resource=http%3A%2F%2Fblog.example.com%2Farticle%2Fid%2F314
    HTTP/1.1
Host: blog.example.com
```

## Details:

OP DiscoveryEndpoint = "/.well-known/openid-configuration"

## Example:

discoveryConfiguration: {
  "issuer": "http://localhost:9998",
  "authorization_endpoint": "http://localhost:9998/auth",
  "token_endpoint": "http://localhost:9998/oauth/token",
  "introspection_endpoint": "http://localhost:9998/oauth/introspect",
  "userinfo_endpoint": "http://localhost:9998/userinfo",
  "revocation_endpoint": "http://localhost:9998/revoke",
  "end_session_endpoint": "http://localhost:9998/end_session",
  "jwks_uri": "http://localhost:9998/keys",
  "scopes_supported": [
    "openid",
    "profile",
    "email",
    "phone",
    "address",
    "offline_access"
  ],
  "response_types_supported": [
    "code",
    "id_token",
    "id_token token"
  ],
  "grant_types_supported": [
    "authorization_code",
    "implicit",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer"
  ],
  "subject_types_supported": [
    "public"
  ],
  "id_token_signing_alg_values_supported": [
    "RS256"
  ],
  "request_object_signing_alg_values_supported": [
    "RS256"
  ],
  "token_endpoint_auth_methods_supported": [
    "none",
    "client_secret_basic",
    "client_secret_post",
    "private_key_jwt"
  ],
  "token_endpoint_auth_signing_alg_values_supported": [
    "RS256"
  ],
  "revocation_endpoint_auth_methods_supported": [
    "none",
    "client_secret_basic",
    "client_secret_post",
    "private_key_jwt"
  ],
  "revocation_endpoint_auth_signing_alg_values_supported": [
    "RS256"
  ],
  "introspection_endpoint_auth_methods_supported": [
    "client_secret_basic",
    "private_key_jwt"
  ],
  "introspection_endpoint_auth_signing_alg_values_supported": [
    "RS256"
  ],
  "claims_supported": [
    "sub",
    "aud",
    "exp",
    "iat",
    "iss",
    "auth_time",
    "nonce",
    "acr",
    "amr",
    "c_hash",
    "at_hash",
    "act",
    "scopes",
    "client_id",
    "azp",
    "preferred_username",
    "name",
    "family_name",
    "given_name",
    "locale",
    "email",
    "email_verified",
    "phone_number",
    "phone_number_verified"
  ],
  "code_challenge_methods_supported": [
    "S256"
  ],
  "ui_locales_supported": [
    "en"
  ],
  "request_parameter_supported": true,
  "request_uri_parameter_supported": false
}