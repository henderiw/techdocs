# install nephio ndd

## create a repo that will be used as a deployment repo

This repo will be used to deploy the NF packages that will be rendered in the mgmt cluster. E.g UPF and SMF will be deployed here afaiu.

you can select 
- private or public repos 
- a dedicated github organization can be used

### public repo

create a public git repo using your username or a dedicated organization

GITHUB_USERNAME=<your user name>
GITHUB_ORGANIZATION=<your organization if you use a dedicatd organization, optional>

### private repo

GITHUB_USERNAME=<your user name>
GITHUB_TOKEN=<your private token>
GITHUB_ORGANIZATION=<your organization if you use a dedicatd organization, optional>

e.g. https://github.com/henderiw-nephio/mgmt-admin.git

## create mgmt cluster

kind create cluster --name mgmt 

## install mgmt server components

install proch and confg sync

### porch 

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

now 

### config sync

#### public deployment repo

this is the step you use when you decided on a public repo in step1. 

```
cat <<EOF | kubectl apply -f -
  apiVersion: configsync.gke.io/v1beta1
  kind: RootSync
  metadata: # kpt-merge: config-management-system/nephio-mgmt-cluster-sync
    name: mgmt-admin-sync
    namespace: config-management-system
    annotations:
      config.kubernetes.io/depends-on: apiextensions.k8s.io/CustomResourceDefinition/rootsyncs.configsync.gke.io
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|nephio-mgmt-cluster-sync'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/henderiw-nephio/mgmt-admin.git
      branch: main
EOF
```

#### private deployment repo

this is needed if you use a private repo

kubectl create secret generic git-creds \
  --namespace="config-management-system" \
  --from-literal=username=${GITHUB_USERNAME} \
  --from-literal=token=${GITHUB_TOKEN}

```
cat <<EOF | kubectl apply -f -
  apiVersion: configsync.gke.io/v1beta1
  kind: RootSync
  metadata: # kpt-merge: config-management-system/nephio-mgmt-cluster-sync
    name: mgmt-admin-sync
    namespace: config-management-system
    annotations:
      config.kubernetes.io/depends-on: apiextensions.k8s.io/CustomResourceDefinition/rootsyncs.configsync.gke.io
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|nephio-mgmt-cluster-sync'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/henderiw-nephio/mgmt-admin.git
      branch: main
      auth: token
      secretRef:
        name: git-creds
EOF
```

## registering repositories

### public repo

when a dedicated git organization is used for the repo

kpt alpha repo register \
  --deployment \
  --namespace default \
https://github.com/${GITHUB_ORGANIZATION}/nephio-mgmt-sync

without a dedicated organization

kpt alpha repo register \
  --deployment \
  --namespace default \
https://github.com/${GITHUB_USERNAME}/nephio-mgmt-sync

### preivate repo

when a dedicated git organization is used for the repo

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/nephio-mgmt-sync

otherwise

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_USERNAME}/nephio-mgmt-sync


## additional stuff

GITHUB_USERNAME=henderiw70
GITHUB_TOKEN=
GITHUB_ORGANIZATION=henderiw-nephio 

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/nephio-test-catalog-01

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/nephio-edge-cluster-01

cat <<EOF | kubectl apply -f -
  apiVersion: configsync.gke.io/v1beta1
  kind: RootSync
  metadata: # kpt-merge: config-management-system/nephio-mgmt-cluster-sync
    name: mgmt-nephio-catalog-sync
    namespace: config-management-system
    annotations:
      config.kubernetes.io/depends-on: apiextensions.k8s.io/CustomResourceDefinition/rootsyncs.configsync.gke.io
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|nephio-mgmt-cluster-sync'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/${GITHUB_ORGANIZATION}/nephio-test-catalog-01
      branch: main
      auth: token
      secretRef:
        name: git-creds
EOF



add the repos to the nephio-test-catalog-01

```yaml
cat <<EOF | kubectl apply -f -
apiVersion: baseconfig.nephio.io/v1alpha1
kind: RepoConfig
metadata:
  name: repo
spec:
  catalogrepo: nephio-test-catalog-01
  mgmtrepo: nephio-test-catalog-01
  deployrepos:
    nephio-edge-1: nephio-edge-cluster-01
  catalogbasepkgs:
    nephio-upf-common: nephio-test-catalog-01-f805c3eb18886846a3a0c41fcd7216cafd13a17a
    nephio-free5gc-upf: nephio-test-catalog-01-b8dbe25dfcb2a70ed67feaf9e2d3dc07958f1523
  deploybasepkgs:
    nephio-upf: nephio-edge-cluster-01-9a0d71e2c65183751008f4b0a7807cb9f54be903
EOF
```

```
cat <<EOF | kubectl apply -f -
apiVersion: networkfunction.nephio.io/v1alpha1
kind: UpfClass
metadata:
  name: upf-class-1
spec:
  uplinkThroughput: "1Gb/s"
  downlinkThroughput: "5Gb/s"
  n3endpoints: 1
  n4endpoints: 1
  n6endpoints: 1
  n9endpoints: 0
  dnn:
  - internet
EOF
```

run the controllers

```
make run
```

```
cat <<EOF | kubectl apply -f -
apiVersion: networkfunction.nephio.io/v1alpha1
kind: NfDeployment
metadata:
  name: 5gc-deploy-test
spec:
  sites:
    - id: free5gc-upf-1
      locationName: somewhere
      clusterName: nephio-edge-1
      nfKind: upf
      nfClassName: upf-class-1
      nfVendor: free5gc
      nfVersion: v3.1.1
      nfNamespace: upf-1
EOF
```

-> deployes 2 packages in the catalog repo

=> here there is an issue with syncing to the mgmt cluster

```
cat <<EOF | kubectl apply -f -
apiVersion: networkfunction.nephio.io/v1alpha1
kind: NfResource
metadata:
  name: free5gc-upf-1
  namespace: default
spec:
  namespace: upf-1
  clustername: nephio-edge-1
  upfnad:
    n3cni: macvlan
    n3master: ens4
    n3gw: 10.10.5.1
    n4cni: macvlan
    n4master: ens4
    n4gw: 192.168.100.1
    n6cni: macvlan
    n6master: ens4
    n6gw: 10.20.3.1
EOF
```

```
cat <<EOF | kubectl apply -f -
apiVersion: networkfunction.nephio.io/v1alpha1
kind: Upf
metadata:
  name: free5gc-upf-1
  namespace: default
spec:
  parent: upf-class-1
  namespace: upf-1
  clustername: nephio-edge-1
  n3:
    endpoints:
    - ipv4Addr:
      - "10.10.5.3/24"
      gwv4addr: "10.10.5.1"
  n4:
    endpoints:
    - ipv4Addr:
      - "192.168.100.3/24"
      gwv4addr: "192.168.100.1"
  n6:
    endpoints:
      internet:
        ipendpoints:
          ipv4Addr:
          - "10.20.3.3/24"
          gwv4addr: "10.20.3.1"
        ipaddrpool: "10.20.3.0/24"
EOF
```