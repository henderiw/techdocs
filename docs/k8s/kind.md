## kind

cat kind-ndd-cluster.yaml:

```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
networking:
  apiServerAddress: "10.132.0.37"
  apiServerPort: 6443
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    listenAddress: "0.0.0.0" # Optional, defaults to "0.0.0.0"
    protocol: tcp # Optional, defaults to tcp
  - containerPort: 443
    hostPort: 443
    listenAddress: "0.0.0.0" # Optional, defaults to "0.0.0.0"
    protocol: tcp # Optional, defaults to tcp
  - containerPort: 7007
    hostPort: 7007
    listenAddress: "0.0.0.0" # Optional, defaults to "0.0.0.0"
    protocol: tcp # Optional, defaults to tcp
```

## getting access behind NAT

retrieve the current kubeadm file

```
kubectl -n kube-system get configmap kubeadm-config -o jsonpath='{.data.ClusterConfiguration}' > kubeadm.yaml
```

add the public IP in the certSANs section

```
apiServer:
  certSANs:
  - localhost
  - 10.132.0.37
  - 35.233.4.91
```

copt the modified kubeadm.yaml file in the docker image

```
docker cp kubeadm.yaml mgmt-control-plane:/root/kubeadm.yaml
```

in the docker image run

```
docker exec mgmt-control-plane kubeadm init phase certs apiserver --config /root/kubeadm.yaml
```

details:

[adding san to cert](https://blog.scottlowe.org/2019/07/30/adding-a-name-to-kubernetes-api-server-certificate/)