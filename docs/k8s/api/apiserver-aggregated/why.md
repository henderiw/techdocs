# why

- crd(s) have only 2 subresources for now: scale and status
- etcd is the backend for crd
- cohabitation: v1.beta -> v1 needs a webhook for conversion
- grace period: not supported using crd(s)
- load on api-server

-> custom validation is flexible

auth
authz
kubeaggregator (go to main apiserver or aggregated apiserver)
    - checks if the req is to handled by a custom api server or a different one
    - register an APIService (similar to validating/mutating webhook)


regular apiserver
- mux -> decoding -> req conversion and defaulting -> admission (mutation/validation) -> REST Logic (storage conversion & defaulting) -> result conversion -> encoding

custom apiserver (no kube aggregator)
- req timeout -> auth - audot - impersonation - max-inflight-authz ->
- mux - decosing (schema) - conversion & defaulting (schema) - admission (mutation/validation) - rest logic/storage

Authentication
-> x-remote-user and x-remote-group -> extra configmap is used to authenticate the client (token review is another option for client authentication)
    - TLS
    - mTLS (SAN validation)
    flow
        client <-> kube-apiserver <-> (APIServer ca bundle + cm for mTLS) aggregated apiserver
        client can also access direct using mTLS or 
-> k get cm -n kube-system extension-apiserver-authentication -o yaml
-> client CA review / token review

Authorization
-> request is sent to the main apiserver to check the authorization for the operations
-> Subject access resource review API for authorization

API priority and faireness
- 

request:

```yaml
apiVersion: authorization.k8s.io/v1
Kind: SubjectAccessreview
spec:
    resourceAtributes:
    ...
```

response

```yaml
apiVersion: authorization.k8s.io/v1
Kind: SubjectAccessreview
spec:
    allowed: true
    ...
```


group priority and minimum


programming kubernetes:
