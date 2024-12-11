# choreo design principles

## workspace

- isolation: 
- contextualization:
    - a dedicated environment
- access control:
    - role based and user specific permissions to manage access to a workspace
- collaboration:
- customization:


definition:
- A dedicated environment with defined scope, resources, and configurations that facilitates task execution, collaboration, and management for individuals or teams in a structured and isolated manner.

components
- resources
    - api(s)
    - code
    - configuration


Workspace (HEAD/main)
    - Team with roles and permissions
        - consumers: 
            - people that change the data (input)
            - users:
                - regular user
                - admin user (can approve changes)
        - producer of self service: 
            - api and business logic -> provide an abstact interface for self service
            - user:
                - regular
                - admin user (can approve changes)
        - producer of providers:
            - apis and api providers (to connect to external world)
            - user:
                - regular
                - admin user (can approve changes)
    - Attached to a life environment (can also be simulation, like containerlab) -> this is main source where changes are synced from
    - 


## implementation

APIServer with workspace
- workspace has a dedicated version controlled backend
    - HEAD is like main -> attached to the running environment or real world
        - can be altered by:
            - refreshing resources
            - applying change sets/ actions
    - ChangeSet or Branch -> context to change the real world (should automatically rebase)
        - Create -> clone HEAD
        - Propose -> create a PR
        - Apply -> merge to main directly w/o a PR ????
        - Delete -> remove the branch
    - Roles:
        - consumer/consumer approver (self service)
            - can DO CRUD on resources
            - can NOT DO CRUD on reconcilers/libraries/apis(crds) -> read only access
        - producer of self service
            - can DO CRUD on resources
            - can DO CRUD on reconcilers/libraries/apis(crds)
        - producer of provider
            - can DO CRUD on resources
            - can DO CRUD on reconcilers/libraries/apis(crds)/providers
    - Assets
        - Resource/API/CRD
        - Resource Library
        - Reconciler
        - Provider

Option1:
- Dedicated API server per workspace - backed by Git
- Roles define access rights (this should be stored in etcd/postgres)
    - on workspace
    - we do not take special care of access rights of reconcilers, except for remote access credentials
- Secrets should have its own KMS storage
- K8s APIServer
    - Roles, Users in ETCD/POSTGRES
    - Embedded API Server -> Dynamic loader of API/Reconciler/Libraries/etc

Option2:
- APIserver with workspace knowledge
- Workspace is a dedicated endpoint
    - dedicated api per workspace /workspace/<workspace-name>
- APIServer
    - 

Running the reconcilers distributed -> need a way to group tham



Workspace
    - Parameters
        - URL of the repo
    - Collaborators: admin, consumer, producer service, producer provider
    - Verbs:
        - Create (admin), Get()

Branch
    - Parameters
        - associated with the workspace
    - Verbs:
        - Create, Delete, Get, List, Validate, Propose, Approve

Resources
    - Special Once (they can also be external datasources, where you access them via credentials)
        - Secret/COnfigMap -> persisted/encryped storage
        - IPAM, AS, VLAN, EXTCOMM, GENID -> persisted storage
        - TOPOLOGY -> persisted storage
    - 

