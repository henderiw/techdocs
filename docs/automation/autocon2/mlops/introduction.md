- SQL
- GraphQL
- Neo4J

in -> service def - generate in mem - gen config
in - gen all technical spec - technical spec - gen config

schema: definition
- tradeoffs:
    - integrity
    - accessibility
    - flexibility
    - consistence
    - change mgmt
    - performance
    - availability

relationship:
- One to One
- One to Many (device - Site)
- Manay to Many (Device - tag)

constraints


SQL:
- data is organized in Tables
- additional features: permissions, transactions
- Pro: support for ACID
JSON schema:
- 2010-2013
- Pro: 
    - nested data using $ref (libraries)
    - oneOf, allOf, heterogenous (polymorphism)
    - Also YAML, TOML
GraphQL:
- 2015
- schema and query lanaguage
- alternative to REST
- we use type -> tells if the parameter is required/optional
- query - very nested query -> query nested data structures
- mutations
- no storage builtin -> resolver that match the database you want to use
    -> you only get what you query
    -> support inheritenace
    -> native support for subscriptions
YANG:
- 
InfraHub:
- schema, query and storage out of the box similar to SQL
- differences
    - domain specific schema
    - capture how to store, query and represent data
    - natively support inheritance/polymorphism
    - support hierarchical nodes & IPAM

```yaml
nodes:
    - name: Device
      namespace:
      inherit_from:
      atrributes:
      relationships:
      - kind:
        generic:
        attribute:
        parent:
        component:
```

polymorphism
- the schema deals with multiple implementation w/o having the application deal with this
- important about the extendability of the model
- e.g. Physical and Logical interface

supported by
- SQL
- JSON schema
- GraphQL
- YANG
- Infrahub: yes through Generic

store the data:
- relational database
- key value database
- document database
- graph database
- time series database

CYPHER & CQL
- MATCH (a:Person) - [:

model vs schema
- 

Service/Intent: 
Technical layer: relationship
Component layer

- Service/Intent: I want LDAP from server hosting app YY to communicate with all domain controllers
- Firewall rull, ALLOW port 389 from IP of server 1/2 to server 8 and 10
- Component Layer: 


Business and Operational context
- Interface/Link Status/Role/Status
    - Role: what it is
    - Status: state in the lifecycle of your object
    - Kind: implementation differences
    