# SSA server side apply

[kep-555](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/555-server-side-apply/README.md)

lists:
- atomic lists
    - can only be owned by 1 manager and can be replaced entirely
    - tags:
        - // +listType=atomic
    - openapi:
        - "x-kubenetes-list-type": "atomic"
- sets
    - an item can be owned by different managers
    - tags:
        - // +listType=set
    - openapi:
        - "x-kubenetes-list-type": "set"
- associatives lists
    - an item can be owned by different managers
    - tags:
        - // +listType=map
        - // +listMapKey=name
    - openapi:
        - "x-kubenetes-list-type": "map"
        - "x-kubernetes-list-map-keys": ["name"]"

maps/structs:
    - granular
        - tags:
            - // +mapType=granular
            - // +structType=granular
        - openapi:
            - "x-kubernetes-map-type": "granular"
    - atomic (all treated as 1 blob)
        - tags:
            - // +mapType=atomic 
            - // +structType=atomic
        - openapi:
            - "x-kubernetes-map-type": "atomic"

## implementation

- allows to create the object

## choreo SSA

2 scenario's
- child resources: list is used to delete the resources but not to compare/diff 
    - here we see that the createTimestamp is needed
- for resources: here you are presented with managedFields if this was the first object
    - we need to prune resourceversion