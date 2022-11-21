# Nephio POC setup

## create kind cluster

```
kind create cluster --name mgmt 
```

## setup environment

GITHUB_USERNAME=henderiw70
GITHUB_TOKEN=
GITHUB_ORGANIZATION=henderiw-nephio 

## create github personal access token

```
cat <<EOF | kubectl create -f -
  apiVersion: v1
  kind: Secret
  metadata:
    name: github-personal-access-token
  data:
    password: 
    username: 
  type: kubernetes.io/basic-auth
EOF
```

## install nephio-system (porch, config-sync, ui, ipam, injector)

```
mkdir -p nephio-install-mgmt
cd nephio-install-mgmt
```

fetch the package

```
kpt pkg get --for-deployment https://github.com/nephio-project/nephio-packages.git/nephio-system
kpt fn render nephio-system
```

apply the package

```
kpt live init nephio-system
kpt live apply nephio-system --reconcile-timeout=15m --output=table
```

-> this should install porch, config-sync, ipam, nf-injector

### install ipam/injector individually

```
kpt pkg get https://github.com/henderiw-nephio/nf-injector-controller/blueprint/nf-injector


k create ns injector
kpt live init nf-injector
kpt live apply nf-injector
```

```
kpt pkg get https://github.com/nokia/k8s-ipam/blueprint/ipam

k create ns ipam
kpt live init ipam
kpt live apply ipam
```

## register repos

### nephio-packages repo

contain all the controllers

```
cat <<EOF | kubectl apply -f - 
  apiVersion: config.porch.kpt.dev/v1alpha1
  kind: Repository
  metadata:
    name: nephio-packages
    namespace: default
    labels:
      kpt.dev/repository-content: external-blueprints
  spec:
    content: Package
    deployment: false
    git:
      branch: main
      directory: /
      repo: https://github.com/nephio-project/nephio-packages.git
      secretRef:
        name: github-personal-access-token
    type: git
EOF
```


### free5g repo

Contains:
- clusterContext (needed for master interface and cniType)
- Imageconfig
- UPFDeployment: empty, will be augmented

```
cat <<EOF | kubectl apply -f - 
  apiVersion: config.porch.kpt.dev/v1alpha1
  kind: Repository
  metadata:
    name: free5gc-packages
    namespace: default
    labels:
      kpt.dev/repository-content: external-blueprints
  spec:
    content: Package
    deployment: false
    git:
      branch: main
      directory: /
      repo: https://github.com/nephio-project/free5gc-packages.git
      secretRef:
        name: github-personal-access-token
    type: git
EOF
```

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
  --name henderiw-free5gc-packages \
https://github.com/${GITHUB_ORGANIZATION}/free5gc-packages

### edge repo

Edge repo is created by the participant/user to store the final upfdeployment manifests

```
cat <<EOF | kubectl apply -f - 
  apiVersion: config.porch.kpt.dev/v1alpha1
  kind: Repository
  metadata:
    name: edge-1
    namespace: default
  spec:
    content: Package
    deployment: true
    git:
      branch: main
      createBranch: true
      directory: /
      repo: https://github.com/${GITHUB_ORGANIZATION}/participant-edge-1.git
      secretRef:
        name: github-personal-access-token
    type: git
EOF
```

### catalog repo

Catalog repo is created by the participant/user 

```
cat <<EOF | kubectl apply -f - 
  apiVersion: config.porch.kpt.dev/v1alpha1
  kind: Repository
  metadata:
    name: catalog
    namespace: default
    labels:
      kpt.dev/repository-content: organizational-blueprints
  spec:
    content: Package
    deployment: false
    git:
      branch: main
      createBranch: true
      directory: /
      repo: https://github.com/${GITHUB_ORGANIZATION}/participant-catalog.git
      secretRef:
        name: github-personal-access-token
    type: git
EOF
```

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
  --name catalog \
https://github.com/${GITHUB_ORGANIZATION}/participant-catalog.git


## create manifests to support the deployment

### cluster

Holds info on region, site-type and name

```
cat <<EOF | kubectl apply -f -
  apiVersion: infra.nephio.org/v1alpha1
  kind: Cluster
  metadata:
    name: edge-1
    labels:
      nephio.org/region: us-central1
      nephio.org/site-type: edge
      nephio.org/site: edge-1
  repositoryRef:
    name: edge-1
EOF
```

### ClusterContext

Holds info per edge-1 regarding node information

```
cat <<EOF | kubectl apply -f -
  apiVersion: infra.nephio.org/v1alpha1
  kind: ClusterContext
  metadata:
    name: edge-1
  spec:
    siteCode: edge-1
    cniConfig:
      cniType: macvlan
      masterInterface: ens1
EOF
```

### ClusterScaleProfile

Holds info per edge on scale

```
cat <<EOF | kubectl apply -f -
  apiVersion: infra.nephio.org/v1alpha1
  kind: ClusterScaleProfile
  metadata:
    name: edge-1
  spec:
    autoscaling: false
    nodeMax: 6
    siteDensity: low
EOF
```

### UPFClass

Holds info on the endpoints and package reference

```
cat <<EOF | kubectl apply -f - 
  apiVersion: nf.nephio.org/v1alpha1
  kind: UPFClass
  metadata:
    name: free5gc-upf
  spec:
    packageRef:
      repository: free5gc-packages
      packageName: free5gc-upf
      revision: v1
    n3EndpointCount: 1
    n4EndpointCount: 1
    n6EndpointCount: 1
    n9EndpointCount: 0
    dnns:
    - internet
EOF
```

### FiveGCoreTopology

Holds the topology information 


```
cat <<EOF | kubectl apply -f - 
  apiVersion: nf.nephio.org/v1alpha1
  kind: FiveGCoreTopology
  metadata:
    name: fivegcoretopology-sample
  spec:
    upfs:
      - name: "agg-layer"
        selector:
          matchLabels:
            nephio.org/region: us-central1
            nephio.org/site-type: edge
        namespace: "upf"
        upf:
          upfClassName: "free5gc-upf"
          capacity:
            uplinkThroughput: "1G"
            downlinkThroughput: "10G"
          n3:
            - networkInstance: "sample-vpc"
              networkName: "sample-n3-net"
          n4:
            - networkInstance: "sample-vpc"
              networkName: "sample-n4-net"
          n6:
            - dnn: "internet"
              uePool:
                networkInstance: "sample-vpc"
                networkName: "ue-net"
                prefixSize: "16"
              endpoint:
                networkInstance: "sample-vpc"
                networkName: "sample-n6-net"
EOF
```

### IPAM

```
cat <<EOF | kubectl apply -f - 
  apiVersion: ipam.nephio.org/v1alpha1
  kind: NetworkInstance
  metadata:
    name: sample-vpc
  spec:
---
  apiVersion: ipam.nephio.org/v1alpha1
  kind: IPPrefix
  metadata:
    name: aggregate0
  spec:
    kind: aggregate
    prefix: 10.0.0.0/8
    networkInstance: sample-vpc
---
  apiVersion: ipam.nephio.org/v1alpha1
  kind: IPPrefix
  metadata:
    name: sample-n3-net-prefix1
    labels:
      nephio.org/gateway: "true"
  spec:
    prefix: 10.0.0.1/24
    network: sample-n3-net
    networkInstance: sample-vpc
---
  apiVersion: ipam.nephio.org/v1alpha1
  kind: IPPrefix
  metadata:
    name: sample-n4-net-prefix1
    labels:
      nephio.org/gateway: "true"
  spec:
    prefix: 192.168.1.1/24
    network: sample-n4-net
    networkInstance: sample-vpc
---
  apiVersion: ipam.nephio.org/v1alpha1
  kind: IPPrefix
  metadata:
    name: sample-n6-net-prefix1
    labels:
      nephio.org/gateway: "true"
  spec:
    prefix: 172.0.0.1/24
    network: sample-n6-net
    networkInstance: sample-vpc
EOF
```

