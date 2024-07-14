## annotations

cli-utils.sigs.k8s.io/inventory-hash:
# to keep a resource -> OnRemoveAnnotation
# only 1 value right now : keep
cli-utils.sigs.k8s.io/on-remove: keep
# to keep a resource -> lifecycleDeleteAnnotation
# only 1 value right now : detach
client.lifecycle.config.k8s.io/deletion: detach

config.kubernetes.io/depends-on: xxx

use in inventory as metadata.labels in inventory and annotation in child objects
- config.k8s.io/owning-inventory: 50043bf8-66f8-45b9-b3e3-e5238a544907


k get cm -n test-namespace inventory-82570863 -o yaml
labels:
  - config.k8s.io/owning-inventory: 50043bf8-66f8-45b9-b3e3-e5238a544907
annotations:
  - config.kubernetes.io/index: "0"
  - config.kubernetes.io/path: inventory-template.yaml
  - internal.config.kubernetes.io/path: inventory-template.yaml
```yaml
apiVersion: v1
data:
  _test-namespace__Namespace: ""
  test-namespace_cm-a__ConfigMap: ""
kind: ConfigMap
metadata:
  annotations:
    config.kubernetes.io/index: "0"
    config.kubernetes.io/path: inventory-template.yaml
    internal.config.kubernetes.io/path: inventory-template.yaml
  creationTimestamp: "2024-03-20T00:12:31Z"
  labels:
    cli-utils.sigs.k8s.io/inventory-id: 50043bf8-66f8-45b9-b3e3-e5238a544907
  name: inventory-82570863
  namespace: test-namespace
  resourceVersion: "188438"
  uid: b7958f4e-67b4-43bc-8d7e-9f304a738435
```


k get ns test-namespace -o yaml
- annotations set:
    config.k8s.io/owning-inventory: 50043bf8-66f8-45b9-b3e3-e5238a544907
```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    config.k8s.io/owning-inventory: 50043bf8-66f8-45b9-b3e3-e5238a544907
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","kind":"Namespace","metadata":{"annotations":{"config.k8s.io/owning-inventory":"50043bf8-66f8-45b9-b3e3-e5238a544907"},"name":"test-namespace"}}
  creationTimestamp: "2024-03-20T00:12:30Z"
  labels:
    kubernetes.io/metadata.name: test-namespace
  name: test-namespace
  resourceVersion: "188437"
  uid: 0d8d8038-b7ab-4bc9-a4df-c06573b0c753
spec:
  finalizers:
  - kubernetes
status:
  phase: Active
```