# did


did stands for decentralized identifiers
did enabled decentralized verifiable identifiers

## why

today identities are centrally managed
federated identities give power to the google's of this world


## terminology

- subject: did refers to a subject e.g. a person, thing, org, abstract identity
- did resolver
- did controller: allows to update the did doc
- did: are URI that assocoate a did subject with a did doc
- did doc: can express
  - 

## did URI

<did>:<did method>:<did method specific id>

e.g.

```
did:example:123456789abcdefghi
```

did: scheme
example: did method
123456789abcdefghi: did method specific identifier

did doc

```
{
  "@Context": [
    "https://www.w3.ord/ns/did/v1
  ]
  "id": "did:example:123456789abcdefghi",
  "autheitication": [{
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "",
    "controller": "",
    "publicKeyMultibase": ""
  }]
}
```

did method: way to resolve did to a doc for more info
