# Key automation topics

- order: 
    - some elements like the ipam, identities need order for restoration
- restore:
    - is there a dependency
- immutability:
    - required delete/create iso update -> how do we know
- dependencies
    - ownerreferences
    - implicit verus explicit
- multi-tenancy
    - adds complexity
- references: immutable external data

## decomposition of the system

Challenge:
- change is inevitable: sw patches, new node, upgrades
    - imperative versus declarative
    - imperative: push x then y, etc

- consumer -> product/service (what) - control plane - providers

product/service: (think them as a catalog)
- what you offer
- decompose it into smaller building blocks that compose the service
    - vendor agnostic
    - network internal
        - instantiate on nodes and links
            - ports: ip addresses/vlans
            - protocol
            - system parameters
            - security
        - route reflector
    - network external
        - nodes and links
            - attachements: ip, vlan
            - protocol
            - security
    - service -> service model (specific context) -> provider
        - N2 issue -> providers (you cannot chnage this)
        - asset: reusable building block
control plane: (actuator)
- provider specific
- human or machines
- deals with change management
- what actuates the building blocks into the runtime
- multiple providers
- components:
    - jobs: similar tasks like -> replicaset
    - tasks: a job instance -> pod


ProdSpec:
- datamodel
    - assets/resosurces
    - partition/administrative domain
    - incarnations: snapshot of partition at a given moment in time
        - immutable: data consistency
        - concistency: dont deal with broken assumptions
- pipeline: to generate the content
    - SOT(s) -> generate -> assets -> incarnation -> Validation - Serving Store
    - changes to SOT reruns the pipeline
- a service infrastructure
