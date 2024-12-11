# apiserver

There is an ETCD shim
- k3s uses SQL light

Resources:
- Namespace
- ServiceAccount, Role, RoleBinding
- Secret, ConfigMap
- CustomResourceDefinitions
- Lease, Event

Coming: Validating, Mutating admission controller

## terminology

- logical cluster:
    - group, version, resource, logical cluster name
- workspace:
    - Models a set of user-facing APIs for CRUD
    - Each workspace is backed by a logical cluster -> exposed as a URL
    - Binds APIs and makes them accesible inside the logical cluster (constrained with resource quotas)
    - isolated api endpoint e.g. /clusters/root
- workspace Type:
    - hierarchical tree
    - root workspace (singleton) -> /clusters/root
        - Workspace CRD
        - WorkspaceType CRD
        - Shard CRD
        - Partition CRD
        - PartitionSet CRD
    - system workspace -> /clusters/system:<system-workspace-name> e.g. /clusters/system:admin
- virtual worksapce:
    - context that the user sees
- index (e.g. workspace index)
    - 
- shard:
- api binding:

## apis

- new concepts 
    - APIExport
    - APIExportEndpointSlice

## logical cluster

- added attribute gvr + logical cluster name + optional namespace/name
- logical cluster name is a global unique identifier


## workspace

- depends on logical cluster
- binds APIs and makes them acceible via the logical cluster (resource limits)
- own discovery, own openAPI spec, own CRDs (GVRs)
- hierarchical tree
    - root:a:b
- apis are exposed using api-bindings


## shards -> multi-cluster

root logical cluster 
    - shards (Shard object)
        - 

logical clusters - |1:N| -> shard