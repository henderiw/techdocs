# Argocd Overview

## Overview

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.

## Installation

### install argo cd

create the argocd namespace

```
kubectl create namespace argocd
```

apply argocd manifest

```
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## Accessing the argocd server

By default, the Argo CD API server is not exposed with an external IP. To access the API server, i am using the loadbalancer method. 

Other methods could be used [argo cd getting started](https://argoproj.github.io/argo-cd/getting_started/)

First install the loadbalancer, afterwards connect the argocd server to the loadbalancer.

### install metallb

More details can be found here [metallb installation on kind](https://kind.sigs.k8s.io/docs/user/loadbalancer/)

create the metallb namespace

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/namespace.yaml
```

create the membership secret

```
kubectl create secret generic -n metallb-system memberlist --from-literal=secretkey="$(openssl rand -base64 128)" 
```

apply metallb manifest

```
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/master/manifests/metallb.yaml
```

wait for pods to come in status running

```
kubectl get pods -n metallb-system --watch
```

add loadbalancer 

To complete layer2 configuration, we need to provide metallb a range of IP addresses it controls. We want this range to be on the docker kind network.

edit metallb.yaml

```
apiVersion: v1
kind: ConfigMap
metadata:
  namespace: metallb-system
  name: config
data:
  config: |
    address-pools:
    - name: default
      protocol: layer2
      addresses:
      - 172.18.0.200-172.18.0.250
```

### Point the argocd server to the loadbalancer

```
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

the loadbalance should get an ip address assigned. In this example 172.18.0.200

```
kubectl get svc -n argocd
NAME                    TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)                      AGE
argocd-dex-server       ClusterIP      10.96.193.16    <none>         5556/TCP,5557/TCP,5558/TCP   41h
argocd-metrics          ClusterIP      10.96.167.204   <none>         8082/TCP                     41h
argocd-redis            ClusterIP      10.96.182.46    <none>         6379/TCP                     41h
argocd-repo-server      ClusterIP      10.96.222.173   <none>         8081/TCP,8084/TCP            41h
argocd-server           LoadBalancer   10.96.243.95    172.18.0.200   80:30865/TCP,443:32049/TCP   41h
argocd-server-metrics   ClusterIP      10.96.133.177   <none>         8083/TCP                     41h
```

### Add iptables to connect the cluster

The first rule provide a dnat from any traffic that enters on port 9443 to the loadbalancer. The second rule ensures the traffic is forwarded

```
sudo iptables -t nat -A DOCKER ! -i br-1f1c85a8b4c5 -p tcp -m tcp --dport 9443 -j DNAT --to-destination 172.18.0.200:443

sudo iptables -t filter -A DOCKER -d 172.18.0.0/24 ! -i br-1f1c85a8b4c5 -o br-1f1c85a8b4c5 -p tcp -m tcp --dport 443 -j ACCEPT
```

### Connecting to the argocd server via UI

We should now be able to connect to the argocd server

```
https://192.168.1.16:9443
```

login-user: admin
password: see next paragraph

```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d &&echo
```

### Connecting to the argocd server via cli

Install the argocd cli

```
brew install argocd
```

Set your cluster environment

```
export KUBECONFG=<kubeconfig file>
```

login to the cluster

```
argo-cd-example % argocd login 192.168.1.16:9443
```

update the password

```
argocd account update-password
```

## Register a cluster

First list all clusters contexts in your current kubeconfig

```
kubectl config get-contexts -o name
```

Choose a context name from the list and supply it to argocd server

```
argocd cluster add ndd-kind
```

## Create An Application From A Git Repository

Setup a repo on git .E.g.

```
https://github.com/nokia-paco-automation/argo-cd-example
```

Setup an app in the UI or via CLI

```
project: default
source:
  repoURL: 'https://github.com/nokia-paco-automation/argo-cd-example'
  path: 03cgservers/
  targetRevision: main
destination:
  namespace: default
  name: kind-ndd
```

