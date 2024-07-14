##

## pkg/object

depndson:
- comma separated list of dependcySet
    - clusterScope example: rbac.authorization.k8s.io/ClusterRole/my-cluster-role-name
    - NamespaceScope: apps/namespaces/my-namespace/Deployment/my-deployment-name

graph

mutation
- resourceRef: kind, apiVersion, group, name, namespace
- field substitution:
    - sourceRef, sourcePath, TargetPath, Token
- Annotation = "config.kubernetes.io/apply-time-mutation"

validation
- seems to only check group, kind, name and namespaces

## inventory

Storage interface
- Load()
- Store
- GetObject
- Apply
- ApplyWithPrune