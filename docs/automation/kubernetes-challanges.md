# kubernetes challenges

- Need for a k8s cluster
- The need for observed and desired state (as per terraform state file)
- Claim model
    - pods and pvc -> represent desired resource requests
    - nodes and pv -> represent available infra resources
- Lacks a clear preview/plan step
- Expensive for infrequent changes (if the API has no change notification)
- KRM uses cross references -> means we need to compute values
- No adequate orchestration (graph solution)
- Permissions and ownership


[KRM medium by brian grant](https://itnext.io/using-the-kubernetes-resource-model-for-declarative-configuration-q-a-b032e5d8ecf5)