# gcp cluster api

[info](https://github.com/kubernetes-sigs/cluster-api-provider-gcp/blob/main/docs/book/src/topics/prerequisites.md)

export GCP_REGION=europe-west1
export GCP_PROJECT=srlinux
# Make sure to use same kubernetes version here as building the GCE image
export KUBERNETES_VERSION=1.23.12
export GCP_CONTROL_PLANE_MACHINE_TYPE=n1-standard-2
export GCP_NODE_MACHINE_TYPE=n1-standard-2
export GCP_NETWORK_NAME=default
export CLUSTER_NAME=capi-cluster

gcloud compute networks list --project="${GCP_PROJECT}"
gcloud compute networks describe "${GCP_NETWORK_NAME}" --project="${GCP_PROJECT}"
gcloud compute firewall-rules list --project "$GCP_PROJECT"
gcloud compute routers create "${CLUSTER_NAME}-myrouter" --project="${GCP_PROJECT}" --region="${GCP_REGION}" --network="default"
gcloud compute routers nats create "${CLUSTER_NAME}-mynat" --project="${GCP_PROJECT}" --router-region="${GCP_REGION}" --router="${CLUSTER_NAME}-myrouter" --nat-all-subnet-ip-ranges --auto-allocate-nat-external-ips

## build image


vi ~/.ssh/config

Host 127.0.0.1
  IPQoS 0x00
  HostKeyAlgorithms=+ssh-rsa
  PubkeyAcceptedKeyTypes=+ssh-rsa



# Export the GCP project id you want to build images in.
export GCP_PROJECT_ID=srlinux

# Export the path to the service account credentials created in the step above.
export GOOGLE_APPLICATION_CREDENTIALS="/Users/henderiw/Downloads/srlinux-a50051d117f3.json"

export GOOGLE_APPLICATION_CREDENTIALS=

# Clone the image builder repository if you haven't already.
git clone https://github.com/kubernetes-sigs/image-builder.git image-builder

# Change directory to images/capi within the image builder repository
cd image-builder/images/capi

# Run the Make target to generate GCE images.
make build-gce-ubuntu-2004

# Check that you can see the published images.
gcloud compute images list --project ${GCP_PROJECT_ID} --no-standard-images --filter="family:capi-ubuntu-1804-k8s"

# Export the IMAGE_ID from the above
export IMAGE_ID="projects/${GCP_PROJECT_ID}/global/images/<image-name>"

export IMAGE_ID="projects/${GCP_PROJECT_ID}/global/images/cluster-api-ubuntu-2004-v1-23-10-1670054207"

## install kind cluster

create kind cluster

clusterctl init -> adds cert-manager and capi bootstrap + control plane

export GCP_B64ENCODED_CREDENTIALS=$(cat /Users/henderiw/Downloads/srlinux-a50051d117f3.json | base64 | tr -d '\n')

clusterctl init --infrastructure gcp
Fetching providers
Skipping installing cert-manager as it is already installed
Installing Provider="infrastructure-gcp" Version="v1.2.1" TargetNamespace="capg-system"



## generate cluster
henderiw@henderiookpro16 techdocs % 


clusterctl generate cluster capi-cluster \
  --control-plane-machine-count=1 \
  --worker-machine-count=3 \
  > capi-quickstart.yaml

```
henderiw@henderiookpro16 techdocs % cat capi-quickstart.yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: capi-cluster
  namespace: default
spec:
  clusterNetwork:
    pods:
      cidrBlocks:
      - 192.168.0.0/16
  controlPlaneRef:
    apiVersion: controlplane.cluster.x-k8s.io/v1beta1
    kind: KubeadmControlPlane
    name: capi-cluster-control-plane
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: GCPCluster
    name: capi-cluster
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPCluster
metadata:
  name: capi-cluster
  namespace: default
spec:
  network:
    name: default
  project: srlinux
  region: europe-west1
---
apiVersion: controlplane.cluster.x-k8s.io/v1beta1
kind: KubeadmControlPlane
metadata:
  name: capi-cluster-control-plane
  namespace: default
spec:
  kubeadmConfigSpec:
    clusterConfiguration:
      apiServer:
        extraArgs:
          cloud-provider: gce
        timeoutForControlPlane: 20m
      controllerManager:
        extraArgs:
          allocate-node-cidrs: "false"
          cloud-provider: gce
    initConfiguration:
      nodeRegistration:
        kubeletExtraArgs:
          cloud-provider: gce
        name: '{{ ds.meta_data.local_hostname.split(".")[0] }}'
    joinConfiguration:
      nodeRegistration:
        kubeletExtraArgs:
          cloud-provider: gce
        name: '{{ ds.meta_data.local_hostname.split(".")[0] }}'
  machineTemplate:
    infrastructureRef:
      apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
      kind: GCPMachineTemplate
      name: capi-cluster-control-plane
  replicas: 1
  version: 1.23.12
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPMachineTemplate
metadata:
  name: capi-cluster-control-plane
  namespace: default
spec:
  template:
    spec:
      image: 'projects/srlinux/global/images/cluster-api-ubuntu-2004-v1-23-10-1670054207 '
      instanceType: n1-standard-2
---
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  name: capi-cluster-md-0
  namespace: default
spec:
  clusterName: capi-cluster
  replicas: 3
  selector:
    matchLabels: null
  template:
    spec:
      bootstrap:
        configRef:
          apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
          kind: KubeadmConfigTemplate
          name: capi-cluster-md-0
      clusterName: capi-cluster
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: GCPMachineTemplate
        name: capi-cluster-md-0
      version: 1.23.12
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPMachineTemplate
metadata:
  name: capi-cluster-md-0
  namespace: default
spec:
  template:
    spec:
      image: 'projects/srlinux/global/images/cluster-api-ubuntu-2004-v1-23-10-1670054207 '
      instanceType: n1-standard-2
---
apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
kind: KubeadmConfigTemplate
metadata:
  name: capi-cluster-md-0
  namespace: default
spec:
  template:
    spec:
      joinConfiguration:
        nodeRegistration:
          kubeletExtraArgs:
            cloud-provider: gce
          name: '{{ ds.meta_data.local_hostname.split(".")[0] }}'
```