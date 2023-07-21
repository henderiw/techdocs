# oidc registrattion

- client registration endpoint
- client configuration endpoint (obtained via client information respone)
- registration access token
- initial access token

## client metadata

used in registration requests and responses

- redirect_uris (mandatory)
- response_types (optional) - default: code (code, token, token_id)
- grant_types (optional) - default: authorization_code (authotization_code, implicit)
- application_type (optional) - default web (web, native)
  - web:
    - redirect_uri: MUST https
  - native:
    - redirect_uri: MUST http + localhost
- contacts (optional) [](emails)
- client_name (optional) 
- logo_uri (optional)
- client_uri (optional)
- policy_uri (optional)
- tos_uri (optional) - terms of service
- jwks_uri (optional) 
- jwks (optional)
- sector_identifier_uri (otional)
- subject_type (optional) - (pairwise, public)
- id_token_signed_response_alg (optional) - default RS256 -> JWS alg
- id_token_encrypted_response_alg (optional) - JWE alg
- id_token_encrypted_response_enc (optional) - JWE enc
- userinfo_signed_response_alg (optional) - JWE alg
- userinfo_encrypted_response_enc (optional) - JWE enc
- request_object_signing_alg (optional) - JWS alg
- request_object_encryption_alg (optional) - JWE alg
- request_object_encryption_enc (optional) - JWE enc - default:  A128CBC-HS256
- token_endpoint_auth_method (optional) - default: client_secret_basic (client_secret_post, client_secret_basic, client_secret_jwt, private_key_jwt, and none)
- token_endpoint_auth_signing_alg (optional) RS256
- default_max_age (optional) 
- require_auth_time (optional)
- default_acr_values (optional) ACR (Authentication Context Class)
- initiate_login_uri
- reauest_uris

## response type relation to grant types

- code: authorization_code
- id_token: implicit
- token, id_token: implicit
- code, id_token: authorization_code, implicit
- code, token: authorization_code, implicit
- code, token, token_id: authorization_code, implicit

## other

- TLS is a MUST
- Security check: policy_uri, logo_uri and redirect_uri should have the same host
- 

## example registration

an access token would be obtained out of band

client (RP) -> POST (Registration Request) -> OP (authorization server)

```curl
POST /connect/register HTTP/1.1
Content-Type: application/json
Accept: application/json
Host: server.example.com
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJ ...

{
  "application_type": "web",
  "redirect_uris":
    ["https://client.example.org/callback",
    "https://client.example.org/callback2"],
  "client_name": "My Example",
  "client_name#ja-Jpan-JP":
    "クライアント名",
  "logo_uri": "https://client.example.org/logo.png",
  "subject_type": "pairwise",
  "sector_identifier_uri":
    "https://other.example.net/file_of_redirect_uris.json",
  "token_endpoint_auth_method": "client_secret_basic",
  "jwks_uri": "https://client.example.org/my_public_keys.jwks",
  "userinfo_encrypted_response_alg": "RSA1_5",
  "userinfo_encrypted_response_enc": "A128CBC-HS256",
  "contacts": ["ve7jtb@example.org", "mary@example.org"],
  "request_uris":
    ["https://client.example.org/rf.txt
      #qpXaRLh_n93TTR9F252ValdatUQvQiJi5BDub2BeznA"]
}
```

client (RP) <- 201 (Registration Response) <- OP (authorization server)
- client_id (required)
- client secret for confidential clients
- client_secret_expires_at (required)

```curl
HTTP/1.1 201 Created
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache

{
  "client_id": "s6BhdRkqt3",
  "client_secret":
    "ZJYCqe3GGRvdrudKyZS0XhGv_Z45DuKhCUk0gBR1vZk",
  "client_secret_expires_at": 1577858400,
  "registration_access_token":
    "this.is.an.access.token.value.ffx83",
  "registration_client_uri":
    "https://server.example.com/connect/register?client_id=s6BhdRkqt3",
  "token_endpoint_auth_method":
    "client_secret_basic",
  "application_type": "web",
  "redirect_uris":
    ["https://client.example.org/callback",
    "https://client.example.org/callback2"],
  "client_name": "My Example",
  "client_name#ja-Jpan-JP":
    "クライアント名",
  "logo_uri": "https://client.example.org/logo.png",
  "subject_type": "pairwise",
  "sector_identifier_uri":
    "https://other.example.net/file_of_redirect_uris.json",
  "jwks_uri": "https://client.example.org/my_public_keys.jwks",
  "userinfo_encrypted_response_alg": "RSA1_5",
  "userinfo_encrypted_response_enc": "A128CBC-HS256",
  "contacts": ["ve7jtb@example.org", "mary@example.org"],
  "request_uris":
    ["https://client.example.org/rf.txt
      #qpXaRLh_n93TTR9F252ValdatUQvQiJi5BDub2BeznA"]
}
```

client (RP) <- 201 (Registration Error Response) <- OP (authorization server)
- 400 Bad Request

```
HTTP/1.1 400 Bad Request
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache

{
  "error": "invalid_redirect_uri",
  "error_description": "One or more redirect_uri values are invalid"
}
```

## example registration read

Client Red Request

```
GET /connect/register?client_id=s6BhdRkqt3 HTTP/1.1
  Accept: application/json
  Host: server.example.com
  Authorization: Bearer this.is.an.access.token.value.ffx83
```

```
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache
{
  "client_id": "s6BhdRkqt3",
  "client_secret":
    "OylyaC56ijpAQ7G5ZZGL7MMQ6Ap6mEeuhSTFVps2N4Q",
  "client_secret_expires_at": 17514165600,
  "registration_client_uri":
    "https://server.example.com/connect/register?client_id=s6BhdRkqt3",
  "token_endpoint_auth_method":
    "client_secret_basic",
  "application_type": "web",
  "redirect_uris":
    ["https://client.example.org/callback",
    "https://client.example.org/callback2"],
  "client_name": "My Example",
  "client_name#ja-Jpan-JP":
    "クライアント名",
  "logo_uri": "https://client.example.org/logo.png",
  "subject_type": "pairwise",
  "sector_identifier_uri":
    "https://other.example.net/file_of_redirect_uris.json",
  "jwks_uri": "https://client.example.org/my_public_keys.jwks",
  "userinfo_encrypted_response_alg": "RSA1_5",
  "userinfo_encrypted_response_enc": "A128CBC-HS256",
  "contacts": ["ve7jtb@example.org", "mary@example.org"],
  "request_uris":
    ["https://client.example.org/rf.txt
      #qpXaRLh_n93TTR9F252ValdatUQvQiJi5BDub2BeznA"]
}
```
