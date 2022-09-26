## create mgmt cluster

kind create cluster --name mgmt --config kind-ndd-cluster.yaml

## install mgmt server components

mkdir -p nephio-install-mgmt
cd nephio-install-mgmt


PORCH 
- fetch the package

```
kpt pkg get --for-deployment https://github.com/nephio-project/nephio-packages.git/nephio-system
kpt fn render nephio-system
```

apply the package

```
kpt live init nephio-system
kpt live apply nephio-system --reconcile-timeout=15m --output=table
```

CONFIGSYNC

export GITHUB_USERNAME=henderiw70
export GITHUB_TOKEN=
export GITHUB_ORGANIZATION=henderiw-nephio

```
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
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|mgmt-admin'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/henderiw-nephio/mgmt-admin
      branch: main
      auth: token
      secretRef:
        name: git-creds
EOF

cat <<EOF | kubectl apply -f -
  apiVersion: configsync.gke.io/v1beta1
  kind: RootSync
  metadata: # kpt-merge: config-management-system/mgmt-config-tenant1
    name: mgmt-config-tenant1-sync
    namespace: config-management-system
    annotations:
      config.kubernetes.io/depends-on: apiextensions.k8s.io/CustomResourceDefinition/rootsyncs.configsync.gke.io
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|mgmt-config-tenant1'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/henderiw-nephio/mgmt-config-tenant1
      branch: main
      auth: token
      secretRef:
        name: git-creds
EOF

## register repos

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
  https://github.com/yndd/packages.git

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/mgmt-admin

kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/mgmt-config-tenant1

## deploy packages

operator/crd package
- target deployment
- topology deployment
- admin deployment


```
kpt alpha rpkg clone yndd-packages-8d954957ad6934ff194e2afdcbd23058e3136cd4 yndd-packages/topology --repository mgmt-admin --revision v1 -n default

kpt alpha rpkg -n default propose mgmt-admin-50670e7b8659f41c5d8279e8681ede1a85a801bc

kpt alpha rpkg -n default approve mgmt-admin-50670e7b8659f41c5d8279e8681ede1a85a801bc
```

## deploy a tenant

admin config packages
- namespace tenant1
- tenant1

step1. create a directory

```
mkdir -p mgmt-admin
```

step2. initialize a package revision

```
kpt alpha rpkg init tenant1 --repository mgmt-admin --revision=v3 -n default
-> creates a branch in the repo
```
step3. initialize the package content

```
kpt pkg init tenant1
```

step4. update the package content -> new files or updated content

step5. push the updates upstream

```
kpt alpha rpkg push -n default mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa ./tenant1 
```

step6. propose/approve

```
kpt alpha rpkg -n default propose mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa

kpt alpha rpkg -n default approve mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa
```

## deploy a topo/fabric in a tenant

step1. create a directory

```
mkdir -p mgmt-config-tenant1
cd mgmt-config-tenant1
```

step2. initialize a package revision

```
kpt alpha rpkg init topology --repository mgmt-config-tenant1 --revision=v1 -n default
-> creates a branch in the repo
```
step3. initialize the package content

```
mkdir topologu
kpt pkg init topology
```

step4. update the package content -> new files or updated content

step5. push the updates upstream

```
kpt alpha rpkg push mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa ./tenant1 -n default
```

step6. propose/approve

```
kpt alpha rpkg -n default propose mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa

kpt alpha rpkg -n default approve mgmt-admin-bef2a672666d94580c33a20ab7fbf58bdd43d9fa
```