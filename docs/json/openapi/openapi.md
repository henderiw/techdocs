brew tap go-swagger/go-swagger
brew install go-swagger

# swagger/openapi

designed fr REST API
- REST: Representational state transfer

API definition: describe all the things you can do with an API
- design before implementing
- review
- test
- create code
- generate documentation

swagger is a collection of tools
- editor
- codegen
- UI
- Hub
OAI: OpenAOI initiative

## api definition

describes everything you can do with an API
- server location
- authorization/authentication: none, Basic Auth, API Key, Oauth
- available requests
- data you can send
- error codes

HTTP:
- method: what action you take (GET, POST, PUT, DELETE)
- URL: scheme, host, base path, path
    -> path will vary
- Query parameters
- headers
- Body

## oas

[oas 3.0 differences](https://blog.restcase.com/6-most-significant-changes-in-oas-3-0/)
[swagger editor](https://editor.swagger.io)

```yaml
swagger: '2.0'
info:
  version: "0.0.1"
  title: Example Photo Service
host: api.example.com
basePath: /photo
schemes:
  - https
# Endpoints
paths:
  # photo album
  /album
    # get one or more albums
    get:
      # Query parameters
      - name: start
        in: query # query parameter
        required: false
        type: string
      - name: end
        in: query
        required: false
        type: string
  /album/{id}:
    get:
      # query parameter
      parameters:
        # album id
        - name: id
          in: path # path parameter
          required: false
          type: integer
      
```

data types:
- boolean
- integer
- number
- string
- array

### schemas

request and response bodies
schema indicates the structure of the schema

[schema](http://json-schema.org/)

-> $ref is a special OAS key

```yaml
post:
    parameters:
        - name: album
          in: body
          required: true
          schema:
            $ref: '#/definitions/newAlbum'

```

request body

```yaml
definitions:
  newAlbum:
    properties:
      name:
        type: string
      date:
        type: string
      author:
        type: object
        properties:
          firstName:
            type: string
          LastName:
            type: string
      relatedAlbumIds:
        type: array
        items:
          type: string
```

### other

security -> auth/authz
- none
- api key
- basic auth
- oauth

```yaml
    security:
    - api_key: []


securityDefinitions:
  api_key:
    type: apiKey
    name: application-key
    in: header
securityDefinitions:
  api_key:
    type: apiKey
    name: token
    in: query
securityDefinitions:
  basic_auth:
    ...
```

errors -> different codes

content-type

```yaml
host:
consumes:
  application/json
produces:
  application/json
```