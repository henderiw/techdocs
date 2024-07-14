# api resource in go

[api machinery library](https://github.com/kubernetes/kubernetes/tree/master/staging/src/k8s.io/apimachinery)
[api library](https://github.com/kubernetes/kubernetes/tree/master/staging/src/k8s.io/api)
-> access via resource/version

Schema:
- maps GVR to/from GVK 

TypeMeta:
- apiVersion
- kind

ObjectMeta:
- name:
- namespace:
- uid: set during the create and never changed
- resourceVersion: used for optimistic concurrency (updating resources)
- generation: used to indicate the version of the spec (desired state) -> updated if the spec changes
    -> can be used with `ObservedGeneration` in status
- labels: constraint to 64 chars
- Annotations: bigger in size
- Ownereferences: uses the garbage collector
    - Controller: used by replicaset to adopt a pod that matches the selection if not owned by another controller
    - BlockOwnerDeletion: 
        - orphan: not deleted by the garbage collector
        - background: return from delete immedicately and not wait for owned resources to be deleted
        - foreground: return from delete after


## apimachinery

- scheme
    - register the API objects as GVK
    - convert between API object of different versions
    - serialize and deserialize objects
- a RESTMapper based on GVK and GVR


### scheme

AddKnownTypes -> GV + types
    -> register GVK
    -> registers a deepcopy selfgeneration function
Conversion: register conversion functions
    - AddGeneratedConversionFunc
    - AddConversionFunc
Serialization

