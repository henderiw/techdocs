# running wasmcloud in k8s

install NATS
install wadm
install operator -> creates a ns wasmcloud-operator
-> uses api aggregated server

create WASM cloud host

```yaml
apiVersion: k8s.wasmcloud.dev/v1alpha1
kind: WasmCloudHostConfig
metadata:
  name: wasmcloud-host
spec:
  lattice: defaualt # used to assign apps to a host
  version: "1.0.4"
natsAddress: nats://nats-clutsre.default.svc.cluster.local
```

this brings up a pod which hosts wasmcloud

install application -> this is a wrapped WADM file

port-forward NATS

```shell
kubectl port-forward svc/nats-cluster 4222:4222 4223:4223
```

wash app list