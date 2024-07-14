# k8s platform

- apiserver
- etcd: db/kv
- controller-manager: controller loop, using watch events (high level to low level)
- scheduler: distributes the low level objects accross the nodes
- kubelet: agent running on nodes, watches the apiserver for pods assigned to the nodes -> deploys the pods through the controller runtime
- kube proxy: watches apiserver for services and programs the network on each node

## openapi spec

since k8s 1.24 is v3 based
[openapi spec](https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec)
[openapi spec v3](https://github.com/kubernetes/kubernetes/tree/master/api/openapi-spec/v3)

[openapi](https://kubernetes.io/docs/reference/kubernetes-api/)

open api
- list of paths: URLs for the apis
- operations supported: GET, DELETE, POST, ...
- per operation the parameters and body fprmats are provided + possible response codes and associated body formats for the response
- list of definitions

```yaml
paths:
    /user/{userid}:
        get:
            parameters:
                userid: integer
            requestBody: {empty}
            responses:
                200:
                    User
        delete:
            parameters:
                userid: integer
            requestBody: {empty}
            responses:
                204:
                    {empty}
    /user:
        post:
            parameters: {empty}
            requestBody: User
            responses:
                200:
                    User
defintiions:
    User:
        ID: integer
        FirstName: string
        LastName: string
```

## verbs and kinds

Kubernetes API verb     HTTP verb
get                         GET
create                      POST
update                      PUT
patch                       PATCH
delete                      DELETE
list                        GET
watch                       GET
deletecollection            DELETE

## gvr: group version resource

REST API -> manages resources
Paths -> to manage these resources plural name are used (REST convention)

groups -> grouping of resources
version -> to manges changes

Core group -> omits the group
    nonNamespaces resources:
        - /api/<version>/<plural-resource-name> 
        - example: /api/v1/nodes
    namespaced resources
        - /api/<version>/namespaces/<ns>/<plural-resource-name> 
        - example: /api/v1/namespaces/default/pods

Regular group
    nonNamespaces resources:
        - /api/<group>/<version>/namespaces/<ns>/<plural-resource-name>
        - example: /apis/storage.k8s.io/v1/storageclasses
    namespaced resources
        - /api/<group>/<version>/namespaces/<ns>/<plural-resource-name>
        - example: /api/apps/v1/namespaces/default/deployments

### subresources

Core group -> omits the group
    nonNamespaces resources:
        - /api/<version>/<plural>/<res-name>/<sub-resource>
        - example: /api/v1/nodes/node1/status
    namespaced resources
        - /api/<version>/namespaces/<ns>/<plural>/<res-name>/<sub-resource> 
        - example: /api/v1/namespaces/default/pods/pod1/status

Regular group
    nonNamespaces resources:
        - /api/<group>/<version>/namespaces/<ns>/<plural>/<res-name>/<sub-resource>
        - example: /apis/storage.k8s.io/v1/storageclasses/sc1/status
    namespaced resources
        - /api/<group>/<version>/namespaces/<ns>/<plural>/<res-name>/<sub-resource>
        - example: /api/apps/v1/namespaces/default/deployments/dep1/status

the operations on status are: get, patch, update

other subresources: attach, binding, exec, proxy

## query parameters

dryRun, fieldManager, fieldValidation, pretty, etc etc

e.g. <path>?dryRun=All