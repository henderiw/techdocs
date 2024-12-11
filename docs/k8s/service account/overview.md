# service account

## purpose

Identities for processes that run inside pods. They are used to authenticate API requests and manage permissions via Role-Based Access Control (RBAC).

## components

- SA resource -> attached to a namespace
    - creates a secret
- SA JWT Token
- RBAC Roles and Bindings -> associated with SA
- POD Spes -> associates the SA

```shell
kubectl create serviceaccount my-service-account
```

secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-service-account-token-abc123
  annotations:
    kubernetes.io/service-account.name: my-service-account
data:
  token: <base64-encoded-JWT>
  ca.crt: <base64-encoded-CA-certificate>
```

role

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
```

role binding

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: default
subjects:
- kind: ServiceAccount
  name: my-service-account
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

association to the pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: default
spec:
  serviceAccountName: my-service-account
  containers:
  - name: my-container
    image: nginx
```

token mounting by the kubelet

```shell
/var/run/secrets/kubernetes.io/serviceaccount.
```

```shell
curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
     -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
     https://kubernetes.default.svc/api/v1/namespaces/default/pods
```

RBAC validation

- API Server validates the token to authenticate the SA and check authorization
- Token can have a shortlived time