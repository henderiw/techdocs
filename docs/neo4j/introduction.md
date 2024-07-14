# neo4j

Graph: collection of nodes and relationships
- nodes
    - labels: person, building, vehilcle
- relationships
    - OWNS: direction is important
    - 1 direction
    - type of relationship: 
        - OWN, PURCHASED
        - Parket_AT
- properties:
    - key value pair on Node/Relationship
    - person properties: name, birthYear
    - building properties: location, gpsCoordinates
    - types:
        - boolean
        - text
        - numbers: integer, float
        - point: 2D, 3D, Lat, Lon, Height
        - Temporal: date, time, datetime, durations
        - Lists: must be of the same type
            -> list of strings
            -> list of booleans
            -> list of lists are not possible for properties
        - NO nested properties
    - schema's are optional
    Node proprerty uniqueness constraint
    Node properly

neo4j.com/docs/cypher-manual

Syntax:

```sqt
MATCH (m:Movie)-[:IN_GENRE]->(g:Genre)
WHERE g.name = 'Comedy' 
RETURN m.title
```

MATCH (m:Movie)
WHEN m.title = "What We Do in the Shadows"
RETURN m

MATCH (actor:Person)-[:ACTED_IN]->(m:Movie)
WHEN m.title = "What We Do in the Shadows"
RETURN actor, m

MATCH (p:PErson{name: "Taika Waititi"})-[:ACTED_IN]->(m:Movie)
RETURN m.title

MATCH (p:PErson{name: "Taika Waititi"})-[:ACTED_IN]->(m:Movie)<-[r:RATED]-(u:User)
RETURN m.title, properties(r)

## Editions

Community: GPLv3
- 34B nodes, 34B relationships, 
- 1 graphDB per installtion
- no RBAC

Neo4j Aura
- 34B nodes, 34B relationships, 
- cloud host version
- automated backups

Enterprise
- subscriptions

## Bloom

look at Neo4J data in usfull way -> NLP

