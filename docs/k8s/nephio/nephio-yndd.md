# install nephio ndd

GITHUB_USERNAME=henderiw70
GITHUB_TOKEN=
GITHUB_ORGANIZATION=henderiw-nephio

## create mgmt cluster

kind create cluster --name mgmt --config kind-ndd-cluster.yaml

## install mgmt server components

mkdir -p nephio-install-mgmt
cd nephio-install-mgmt


### porch 

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

### config sync

fetch the package

```
cat <<EOF | kubectl apply -f -
  apiVersion: configsync.gke.io/v1beta1
  kind: RootSync
  metadata: # kpt-merge: config-management-system/nephio-mgmt-cluster-sync
    name: nephio-mgmt-cluster-sync
    namespace: config-management-system
    annotations:
      config.kubernetes.io/depends-on: apiextensions.k8s.io/CustomResourceDefinition/rootsyncs.configsync.gke.io
      internal.kpt.dev/upstream-identifier: 'configsync.gke.io|RootSync|config-management-system|nephio-mgmt-cluster-sync'
  spec:
    sourceFormat: unstructured
    git:
      repo: https://github.com/henderiw-nephio/nephio-mgmt-sync
      branch: main
      auth: token
      secretRef:
        name: git-creds
EOF
```

## registering repositories

kubectl create secret generic git-creds \
  --namespace="config-management-system" \
  --from-literal=username=${GITHUB_USERNAME} \
  --from-literal=token=${GITHUB_TOKEN}

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
  https://github.com/${GITHUB_ORGANIZATION}/yndd-packages.git

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/yndd-admin

kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/yndd-config-tenant1


kpt alpha repo register \
  --deployment \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
https://github.com/${GITHUB_ORGANIZATION}/nephio-mgmt-sync




kpt alpha repo get
kpt alpha rpkg get

operator/crd package
- target deployment
- topology deployment
- admin deployment

admin config packages
- namespace tenant1
- tenant1

tenant1 config packages
- fabric1 topology

```
kpt alpha rpkg clone yndd-packages-eab26028b156b5aa2419e71bcebbac06d469825a yndd-packages/target --repository nephio-mgmt-sync -revision v1 -n default

kpt alpha rpkg propose nephio-mgmt-sync-806bfb766002c079922b5cc5b2bf9bb46f9754be -n default

kpt alpha rpkg approve nephio-mgmt-sync-806bfb766002c079922b5cc5b2bf9bb46f9754be -n default
```
