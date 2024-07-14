# overview

## providers

infrastructure: capg (gcp), capa (aws), capz (azure)
- lifecycle mgmt VM(s), Loadbalancers, vpcs
bootstrap: cabpk (kubeadm), cabpm (microk8s), cabpt (Talos)
- lifecycle mgmt: certs, control plane, joining worker nodes to the control plane
control-plane: cacpk (kubeadm), cacpm (microk8s), cacppt (Talos)
- kube api-server, kube controller-manager, kube-scheduler
- defaults to kubeadm

# CRD(s)

- Machine: spec for infra backing the kubernetes node (i.e. VM)
- MachineSet: (similar to Replicaset)
- MachineDeployment: (similar to deployment)


## generate yaml

# Enable the experimental Cluster topology feature.
export CLUSTER_TOPOLOGY=true

# Enable the experimental Machine Pool feature
export EXP_MACHINE_POOL=true

# Initialize the management cluster
clusterctl generate provider --infrastructure docker > capd.yaml
clusterctl generate provider --core cluster-api > capi.yaml
clusterctl generate provider --bootstrap kubeadm > capi-bootstrap.yaml
clusterctl generate provider --control-plane kubeadm > capi-cp.yaml