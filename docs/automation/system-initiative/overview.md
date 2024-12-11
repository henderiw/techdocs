# overview

database
- Head (in git this is main)
- Local workspaces that should get synced with head/main (automatic rebase)
    -> they propose changes -> should go in a branch/PR for someone to approve/merge
    -> actuator implements the change (replace all or update/delete)


## tutorial

- create a change set -> like a workspace
- add credentials and secrets
- add components -> these are resources in k8s
- configure components
    - add atrributes
- connect components
    - input and output sockets
- execute actions by applying the change set

## implementation

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
        - owner or admin (the creator of the workspace)
        - approver: 
        - collaborator
    - Asset or a model
        - Attribute Panel (attributes of the asset)
        - Arity: arguments taken by a fn (one or many)
        - Component: the desired state
            - Credential: type of component that stores secret data and has authentication function attaches
            - Input socket (lives on left hand side of the component)
            - Output socker (feeds data out of the component) (appears right)
        - Resource: the actual state
        - Qualification: check validity e.g. is the secret ok, is the ami name valid in the region
        - Schema
        - Secret is a credential component
    - THE Model: all assets, functions, components, resources that make up the hypergraph

## Asset schema

asset schema defines:
- component properties (desired state)
- resource properties (actual state)
- input and output sockers
- secrets the asset requires
- secrets the asset defines

builders:
- AssetBuilder
- PropBuilder -> define properties to an asset
- PropWidgetDefinitionBuilder -> widget define how properties are displayed


reflection:
- schema with properties
- distinguishes desire from state (component/resource)
- qualification functions -> can check through api(s) the validaty
- input sockets
    - per schema
- output socket
    - 