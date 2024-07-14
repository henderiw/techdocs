# custom API services

## why

crd limits:
- etcd storage
- no protobuf
- subresources limited to status, scale
- no gracefull deletion
- add k8s apiserver CPU load
- only standard CRUD for the API endpoints
- no support for cohabitation (webhook)

[pizza example](https://github.com/programming-kubernetes/pizza-apiserver/tree/master)

## kube-aggregator

api-proxy (api-aggregation) -> done by kube-aggregator
[kube-aggregator](https://github.com/kubernetes/kube-aggregator)
- allows to register API(s)
    - apigroup/version is registered using APIService (no notion of the resource behind the apiservice)
    - maps to a service
    - caBundle
    - groupPriorityMinimum
    - versionPriority
- summarize discovery info
- proxy client requests to individual servers

## custom apiServer

- same internal structure
- own handler chain (auth, authz, audit, imppersonization)
- own resource handler pipeline (decodong, conversion, admission)
- storage is flexible
- own scheme and registry implementation
- does auth again with the k8s apiServer (certificate or token based)
- does own auditing
- does authz again using SubjectAccessReview to the k8s api server

## delegated authenitication

same library -> can use client cert ot tokens to authenticate users
k8s API server authenticates the user already -> result is forwarded username and group memebership -> in HTTP request headers using X-Remote-User and X-Remote-group
-> can be configured with `requestheader-username-headers` and `requestheader-group-headers` flags

the aggegated apiserver has to know when to trust these headers. using configmap

```
k describe cm -n kube-system extension-apiserver-authentication
```

## delegated authorization

authorization absed on username and group list

The custom APIserver delegates authz to the k8s APIserver via SubjectAccessReviews.
The customer APIserver keeps a cache 1024 auth entries
- 5 min expiry for allowed requests
- 30 sec expiry for denied requests

```yaml
apiVersion: authorization.k8s.io/v1
kind: subjectAccessreview
spec: 
  resourceAttributes:
    group: apps
    resource: deployments
    verb: create
    namespace: default
    version: v1
    name: example
  user: michael
  groups:
  - system:authenticated
  - admins
  - authors


apiVersion: authorization.k8s.io/v1
kind: subjectAccessreview
status: 
  allowed: true
  denied: false
  reason: "ccccc
```



http://bit.ly/2x9C3gR