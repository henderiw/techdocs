```
cat <<EOF | kubectl apply -f -
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: configsync.gke.io:ns-reconciler
    labels:
      configmanagement.gke.io/system: "true"
      configmanagement.gke.io/arch: "csmr"
  rules:
  - apiGroups: ["configsync.gke.io"]
    resources: ["reposyncs"]
    verbs: ["get"]
  - apiGroups: ["configsync.gke.io"]
    resources: ["reposyncs/status"]
    verbs: ["get","list","update"]
  - apiGroups: ["kpt.dev"]
    resources: ["resourcegroups"]
    verbs: ["*"]
  - apiGroups: ["kpt.dev"]
    resources: ["resourcegroups/status"]
    verbs: ["*"]
  - apiGroups:
    - policy
    resources:
    - podsecuritypolicies
    resourceNames:
    - acm-psp
    verbs:
    - use
EOF
```

## read-only access to git repo

### grant access with ssh-key

```
ssh-keygen -t rsa -b 4096 \
-C "henderiw70" \
-N '' \
-f ~/.ssh/henderiw70
```

```
kubectl create ns config-management-system && \
kubectl create secret generic git-creds \
 --namespace=config-management-system \
 --from-file=ssh=~/.ssh/henderiw70
```

### grant access to git with token (personal access token)

create a peronal access token

```
kubectl create ns config-management-system && \
kubectl create secret generic git-creds \
  --namespace="config-management-system" \
  --from-literal=username=henderiw70 \
  --from-literal=token=TOKEN
```

### configure the operator

```
cat <<EOF | kubectl apply -f -
apiVersion: configsync.gke.io/v1beta1
kind: RootSync
metadata:
  name: root-sync
  namespace: config-management-system
spec:
  sourceType: git
  sourceFormat: unstructured
  git:
    repo: https://github.com/henderiw-nephio/repo-configsync-root
    ##revision: ROOT_REVISION
    branch: main
    ##dir: ROOT_DIRECTORY
    auth: token
    ##gcpServiceAccountEmail: ROOT_EMAIL
    secretRef:
      name: git-creds
    ##noSSLVerify: ROOT_NO_SSL_VERIFY
EOF
```

### namespace repository

```
kubectl create ns ndd-group1 && \
kubectl create secret generic git-creds \
  --namespace=ndd-group1 \
  --from-literal=username=henderiw70 \
  --from-literal=token=TOKEN
```

in namespace repo
/root repo -> namespaces/ndd-group1/reposync.yaml

```
apiVersion: configsync.gke.io/v1beta1
kind: RepoSync
metadata:
  name: group1
  namespace: ndd-group1
spec:
  # Since this is for a namespace repository, the format should be unstructured
  sourceFormat: unstructured
  git:
   repo: https://github.com/henderiw-nephio/repo-configsync-group1
   ##revision: NAMESPACE_REVISION
   branch: main
   ##dir: "NAMESPACE_DIRECTORY"
   auth: token
   ##gcpServiceAccountEmail: NAMESPACE_EMAIL
   secretRef:
     name: git-creds
   ##noSSLVerify: NAMESPACE_NO_SSL_VERIFY
```

in namespace repo
/root repo -> namespaces/ndd-group1/reposync.yaml

```
 kind: RoleBinding
 apiVersion: rbac.authorization.k8s.io/v1
 metadata:
   name: syncs-repo
   namespace: ndd-group1
 subjects:
 - kind: ServiceAccount
   name: ns-reconciler-ndd-group1
   namespace: config-management-system
 roleRef:
   kind: ClusterRole
   name: admin
   apiGroup: rbac.authorization.k8s.io
```


## TEST

```
cat <<EOF | kubectl apply -f -
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: topology-definition-editor-role
  rules:
  - apiGroups:
    - topo.yndd.io
    resources:
    - definitions
    verbs:
    - create
    - delete
    - get
    - list
    - patch
    - update
    - watch
  - apiGroups:
    - topo.yndd.io
    resources:
    - definitions/status
    verbs:
    - get
    - patch
    - update
EOF
```

```
cat <<EOF | kubectl apply -f -
  apiVersion: rbac.authorization.k8s.io/v1
  kind: ClusterRole
  metadata:
    name: topology-template-editor-role
  rules:
  - apiGroups:
    - topo.yndd.io
    resources:
    - templates
    verbs:
    - create
    - delete
    - get
    - list
    - patch
    - update
    - watch
  - apiGroups:
    - topo.yndd.io
    resources:
    - templates/status
    verbs:
    - get
    - patch
    - update
EOF
```

```
cat <<EOF | kubectl apply -f -
  kind: RoleBinding
  apiVersion: rbac.authorization.k8s.io/v1
  metadata:
    name: edit-topology-definitions
    namespace: ndd-group1
  subjects:
  - kind: ServiceAccount
    name: ns-reconciler-ndd-group1
    namespace: config-management-system
  roleRef:
    kind: ClusterRole
    name: topology-definition-editor-role
    apiGroup: rbac.authorization.k8s.io
EOF
```

```
cat <<EOF | kubectl apply -f -
  kind: RoleBinding
  apiVersion: rbac.authorization.k8s.io/v1
  metadata:
    name: edit-topology-templates
    namespace: ndd-group1
  subjects:
  - kind: ServiceAccount
    name: ns-reconciler-ndd-group1
    namespace: config-management-system
  roleRef:
    kind: ClusterRole
    name: topology-template-editor-role
    apiGroup: rbac.authorization.k8s.io
EOF
```