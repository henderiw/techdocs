

cat kind-ndd-cluster.yaml:
```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  apiServerAddress: "192.168.1.16"
  apiServerPort: 6443
```