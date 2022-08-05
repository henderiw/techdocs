# Flux Overview

## Overview

- uses different controllers
	- source controller
		- used to identify the sources on which the git information is syned	
	- kustomize controller
		- uses kustomize as it generates a single manifest file and is used by flux to handle this in a single transaction.	
	- helm controller
	- image controller

## Installation

### prerequisites

export GITHUB_TOKEN=<your-token>
export GITHUB_USER=henderiw

### install flux cli

mac

```
brew install fluxcd/tap/flux
```

linux

```
curl -s https://toolkit.fluxcd.io/install.sh | sudo bash
```

### create kind cluster

```
flux check --pre
```

### bootstrap

The bootstrap command creates a repository if one doesn't exist, commits the manifests for the Flux components to the default branch at the specified path, and installs the Flux components. Then it configures the target cluster to synchronize with the specified path inside the repository.

#### github user repo

This is not used in the example

```
flux bootstrap github \
  --owner=$GITHUB_USER \
  --repository=fleet-infra \
  --branch=main \
  --path=./clusters/ndd-cluster \
  --personal
```

#### github organization

```
flux bootstrap github \
  --owner=nokia-paco-automation \
  --repository=flux-home-infra \
  --branch=main \
  --path=./clusters/ndd-kind
```

example output
-> create a repo with a flux-system directory that includes the information to deploy flux
-> create flux-system namespace in the k8s cluster with the 4 controllers: source/kustomize/helm/image

```
► connecting to github.com
✔ repository created
✔ repository cloned
✚ generating manifests
✔ components manifests pushed
► installing components in flux-system namespace
namespace/flux-system created
customresourcedefinition.apiextensions.k8s.io/alerts.notification.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/buckets.source.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/gitrepositories.source.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/helmcharts.source.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/helmreleases.helm.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/helmrepositories.source.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/kustomizations.kustomize.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/providers.notification.toolkit.fluxcd.io created
customresourcedefinition.apiextensions.k8s.io/receivers.notification.toolkit.fluxcd.io created
serviceaccount/helm-controller created
serviceaccount/kustomize-controller created
serviceaccount/notification-controller created
serviceaccount/source-controller created
clusterrole.rbac.authorization.k8s.io/crd-controller-flux-system created
clusterrolebinding.rbac.authorization.k8s.io/cluster-reconciler-flux-system created
clusterrolebinding.rbac.authorization.k8s.io/crd-controller-flux-system created
service/notification-controller created
service/source-controller created
service/webhook-receiver created
deployment.apps/helm-controller created
deployment.apps/kustomize-controller created
deployment.apps/notification-controller created
deployment.apps/source-controller created
networkpolicy.networking.k8s.io/allow-scraping created
networkpolicy.networking.k8s.io/allow-webhooks created
networkpolicy.networking.k8s.io/deny-ingress created
◎ verifying installation
✔ source-controller: deployment ready
✔ kustomize-controller: deployment ready
✔ helm-controller: deployment ready
✔ notification-controller: deployment ready
✔ install completed
► configuring deploy key
✔ deploy key configured
► generating sync manifests
✔ sync manifests pushed
► applying sync manifests
◎ waiting for cluster sync
✔ bootstrap finished
```

When we clone the repo we get the folowing output

```
henderiw@M-C02CL21DMD6T flux-home-infra % tree
.
├── README.md
└── clusters
    └── ndd-kind
        └── flux-system
            ├── gotk-components.yaml
            ├── gotk-sync.yaml
            └── kustomization.yaml

3 directories, 4 files
```

k8s cluster info: see flux-system namespace and controller

```
henderiw@nucx:~$ k get pods -A
NAMESPACE                 NAME                                                   READY   STATUS    RESTARTS   AGE
flux-system               helm-controller-5bbd94c75-jjz7l                        1/1     Running   0          9m59s
flux-system               kustomize-controller-6b7fc7677d-zpsrc                  1/1     Running   0          9m59s
flux-system               notification-controller-6b4db845c8-9vmfs               1/1     Running   0          9m59s
flux-system               source-controller-65bbc7f76b-xxscx                     1/1     Running   0          9m59s
kube-system               coredns-f9fd979d6-9l7mb                                1/1     Running   0          37h
kube-system               coredns-f9fd979d6-f5bmb                                1/1     Running   0          37h
kube-system               etcd-ndd-control-plane                                 1/1     Running   0          37h
kube-system               kindnet-r7qxn                                          1/1     Running   0          37h
kube-system               kube-apiserver-ndd-control-plane                       1/1     Running   0          37h
kube-system               kube-controller-manager-ndd-control-plane              1/1     Running   0          37h
kube-system               kube-proxy-qqsz7                                       1/1     Running   0          37h
kube-system               kube-scheduler-ndd-control-plane                       1/1     Running   0          37h
local-path-storage        local-path-provisioner-78776bfc44-dc7c2                1/1     Running   0          37h
nddriver-system           nddriver-controller-manager-5c9946596c-x8kgv           2/2     Running   0          37h
nddriver-system           nddriver-deployment-leaf1-68c6494486-nxkd4             1/1     Running   4          37h
nddriver-system           nddriver-deployment-leaf2-56d7b8c8f-tbkt8              1/1     Running   0          3h2m
srl-k8s-operator-system   srl-k8s-operator-controller-manager-64dd7c5978-6xmz8   2/2     Running   0          37h
```

### Source

The create source git command generates a GitRepository resource and waits for it to sync. For Git over SSH, host and SSH keys are automatically generated and stored in a Kubernetes secre

Execute in the cloned repo

```
flux create source git pacosrl \
  --url=https://github.com/nokia-paco-automation/flux-paco-srl-switch\
  --branch=main \
  --interval=30s \
  --export > ./clusters/ndd-kind/pacosrl-source.yaml
```

this creates the following file

```
henderiw@M-C02CL21DMD6T flux-home-infra % cat clusters/ndd-kind/pacosrl-source.yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: GitRepository
metadata:
  name: pacosrl
  namespace: flux-system
spec:
  interval: 30s
  ref:
    branch: master
  url: https://github.com/nokia-paco-automation/flux-paco-srl-switch
```

push the file to the repo

```
git add -A && git commit -m "Add pacosrl GitRepository"
git push
```

### kustomization

Create the yaml file

```
flux create kustomization pacosrl \
  --source=pacosrl \
  --path="./kustomize/base" \
  --prune=true \
  --validation=client \
  --interval=5m \
  --export > ./clusters/ndd-kind/pacosrl-kustomization.yaml
```

generates the following file in the flux repo

```
henderiw@M-C02CL21DMD6T flux-home-infra % cat clusters/ndd-kind/pacosrl-kustomization.yaml
---
apiVersion: kustomize.toolkit.fluxcd.io/v1beta1
kind: Kustomization
metadata:
  name: pacosrl
  namespace: flux-system
spec:
  interval: 5m0s
  path: ./kustomize/base
  prune: true
  sourceRef:
    kind: GitRepository
    name: pacosrl
  validation: client

```

push the file to the repo

```
git add -A && git commit -m "Add pacosrl Kustomization"
git push
```

git structure in the flux repo

```
henderiw@M-C02CL21DMD6T flux-home-infra % tree
.
├── README.md
└── clusters
    └── ndd-kind
        ├── flux-system
        │   ├── gotk-components.yaml
        │   ├── gotk-sync.yaml
        │   └── kustomization.yaml
        ├── pacosrl-kustomization.yaml
        └── pacosrl-source.yaml

3 directories, 6 files

```

### Input and result in SRL

Input yaml file we added to the system

```
apiVersion: srlinux.henderiw.be/v1alpha1
kind: K8sSrlNokiaInterfacesInterface
metadata:
  name: interface-paco-infra
  labels:
    target: leaf-grp1
spec:
  interface:
  - name: irb0
    admin-state: enable
    description: "paco-irb0"
  - name: system0
    admin-state: enable
    description: "paco-system0"
  - name: lo0
    admin-state: enable
    description: "paco-lo0"
  - name: ethernet-1/49
    admin-state: enable
    description: "paco-infra-e1-49"
    vlan-tagging: false
```

Result on SRL leaf1

```
A:leaf1# show interface
====================================================================
ethernet-1/49 is up, speed 100G, type None
--------------------------------------------------------------------
irb0 is up, speed None, type None
--------------------------------------------------------------------
lo0 is up, speed None, type None
--------------------------------------------------------------------
mgmt0 is up, speed 10G, type None
  mgmt0.0 is up
    Encapsulation: null
    Type         : None
    IPv4 addr    : 172.20.20.6/24 (dhcp, preferred)
    IPv6 addr    : 2001:172:20:20::6/80 (dhcp, preferred)
    IPv6 addr    : fe80::42:acff:fe14:1406/64 (link-layer, preferred)
--------------------------------------------------------------------
system0 is up, speed None, type None
--------------------------------------------------------------------
====================================================================
Summary
  1 loopback interfaces configured
  3 ethernet interfaces are up
  1 management interfaces are up
  1 subinterfaces are up
====================================================================
--{ + running }--[  ]--
```

Result on SRL leaf2

```
A:leaf2# show interface
========================================================
ethernet-1/49 is up, speed 100G, type None
--------------------------------------------------------
irb0 is up, speed None, type None
--------------------------------------------------------
lo0 is up, speed None, type None
--------------------------------------------------------
mgmt0 is up, speed 10G, type None
  mgmt0.0 is up
    Encapsulation: null
    Type         : None
    IPv4 addr    : 172.20.20.7/24 (dhcp, preferred)
    IPv6 addr    : 2001:172:20:20::7/80 (dhcp, preferred)
    IPv6 addr    : fe80::42:acff:fe14:1407/64 (link-layer, preferred)
--------------------------------------------------------
system0 is up, speed None, type None
--------------------------------------------------------
========================================================
Summary
  1 loopback interfaces configured
  3 ethernet interfaces are up
  1 management interfaces are up
  1 subinterfaces are up
========================================================
--{ + running }--[  ]-
```