# hubble

- agent -> besides cilium there is hubble agent code (hubble server)
  -> this is why we have to restart it
  -> Observer service:
    - TCP socket or unix socket
    - GetFlows -> via ring buffer
    - GetNodes
    - ServerStatus
  -> Peer service
    - TCP socket and unix socket and kubernetes service (hubble-peer)
    - Notify
- hubble relay: collect the information in the cluster
  -> deployed as a pod
- hubble ui

L4
L7 -> using envoy proxy for DNS and HTTP info

Flow information

```
time
verdict (forward, drop, etc)
ethernet
ip
L4
source (id, identity, namespace, labels, name)
destination (id, identity, namespace, labels, nanme)
type
node-name
event-type
traffic direction
traffic observation: to-stack
is reply: false
```

## hubble relay config

```
henderiw@ctf:~$ ks describe cm hubble-relay-config
Name:         hubble-relay-config
Namespace:    kube-system
Labels:       <none>
Annotations:  <none>

Data
====
config.yaml:
----
cluster-name: default
peer-service: "hubble-peer.kube-system.svc.cluster.local:443"
listen-address: :4245
dial-timeout:
retry-timeout:
sort-buffer-len-max:
sort-buffer-drain-timeout:
tls-client-cert-file: /var/lib/hubble-relay/tls/client.crt
tls-client-key-file: /var/lib/hubble-relay/tls/client.key
tls-hubble-server-ca-files: /var/lib/hubble-relay/tls/hubble-server-ca.crt
disable-server-tls: true

BinaryData
====

Events:  <none>
```

cilium agent

```
henderiw@ctf:~$ ks describe pods hubble-relay-768858c54c-2b5kk
Name:         hubble-relay-768858c54c-2b5kk
Namespace:    kube-system
Priority:     0
Node:         ctf/10.132.0.40
Start Time:   Fri, 30 Sep 2022 16:17:43 +0000
Labels:       k8s-app=hubble-relay
              pod-template-hash=768858c54c
Annotations:  <none>
Status:       Running
IP:           10.0.0.28
IPs:
  IP:           10.0.0.28
Controlled By:  ReplicaSet/hubble-relay-768858c54c
Containers:
  hubble-relay:
    Container ID:  containerd://48614b372270f8f9c1f62d6de9264a04d7e3b7fc9a8c576879a219415318544d
    Image:         quay.io/cilium/hubble-relay:v1.12.2@sha256:6f3496c28f23542f2645d614c0a9e79e3b0ae2732080da794db41c33e4379e5c
    Image ID:      quay.io/cilium/hubble-relay@sha256:6f3496c28f23542f2645d614c0a9e79e3b0ae2732080da794db41c33e4379e5c
    Port:          4245/TCP
    Host Port:     0/TCP
    Command:
      hubble-relay
    Args:
      serve
    State:          Running
      Started:      Fri, 30 Sep 2022 16:18:56 +0000
    Ready:          True
    Restart Count:  0
    Liveness:       tcp-socket :grpc delay=0s timeout=1s period=10s #success=1 #failure=3
    Readiness:      tcp-socket :grpc delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /etc/hubble-relay from config (ro)
      /var/lib/hubble-relay/tls from tls (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  config:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      hubble-relay-config
    Optional:  false
  tls:
    Type:                Projected (a volume that contains injected data from multiple sources)
    SecretName:          hubble-relay-client-certs
    SecretOptionalName:  <nil>
QoS Class:               BestEffort
Node-Selectors:          kubernetes.io/os=linux
Tolerations:             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                         node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  5m43s  default-scheduler  Successfully assigned kube-system/hubble-relay-768858c54c-2b5kk to ctf
  Normal  Pulling    4m36s  kubelet            Pulling image "quay.io/cilium/hubble-relay:v1.12.2@sha256:6f3496c28f23542f2645d614c0a9e79e3b0ae2732080da794db41c33e4379e5c"
  Normal  Pulled     4m31s  kubelet            Successfully pulled image "quay.io/cilium/hubble-relay:v1.12.2@sha256:6f3496c28f23542f2645d614c0a9e79e3b0ae2732080da794db41c33e4379e5c" in 4.927916727s
  Normal  Created    4m31s  kubelet            Created container hubble-relay
  Normal  Started    4m31s  kubelet            Started container hubble-relay
```

```
henderiw@ctf:~$ ks describe pod cilium-56frp
Name:                 cilium-56frp
Namespace:            kube-system
Priority:             2000001000
Priority Class Name:  system-node-critical
Node:                 ctf/10.132.0.40
Start Time:           Fri, 30 Sep 2022 16:16:30 +0000
Labels:               controller-revision-hash=5d5cc79b6d
                      k8s-app=cilium
                      pod-template-generation=1
Annotations:          container.apparmor.security.beta.kubernetes.io/apply-sysctl-overwrites: unconfined
                      container.apparmor.security.beta.kubernetes.io/cilium-agent: unconfined
                      container.apparmor.security.beta.kubernetes.io/clean-cilium-state: unconfined
                      container.apparmor.security.beta.kubernetes.io/mount-cgroup: unconfined
Status:               Running
IP:                   10.132.0.40
IPs:
  IP:           10.132.0.40
Controlled By:  DaemonSet/cilium
Init Containers:
  mount-cgroup:
    Container ID:  containerd://a1f77df991f26282b97458412845b7dcd1f3d8dee9eb6df6ea5056936b43bac6
    Image:         quay.io/cilium/cilium:v1.12.2@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Image ID:      quay.io/cilium/cilium@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -ec
      cp /usr/bin/cilium-mount /hostbin/cilium-mount;
      nsenter --cgroup=/hostproc/1/ns/cgroup --mount=/hostproc/1/ns/mnt "${BIN_PATH}/cilium-mount" $CGROUP_ROOT;
      rm /hostbin/cilium-mount

    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 30 Sep 2022 16:16:33 +0000
      Finished:     Fri, 30 Sep 2022 16:16:33 +0000
    Ready:          True
    Restart Count:  0
    Environment:
      CGROUP_ROOT:  /run/cilium/cgroupv2
      BIN_PATH:     /opt/cni/bin
    Mounts:
      /hostbin from cni-path (rw)
      /hostproc from hostproc (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5v99z (ro)
  apply-sysctl-overwrites:
    Container ID:  containerd://49276d1366c7c4dab6be510d1f3474ddfd287b5d30feb505d4e59f6e1e65acc4
    Image:         quay.io/cilium/cilium:v1.12.2@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Image ID:      quay.io/cilium/cilium@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -ec
      cp /usr/bin/cilium-sysctlfix /hostbin/cilium-sysctlfix;
      nsenter --mount=/hostproc/1/ns/mnt "${BIN_PATH}/cilium-sysctlfix";
      rm /hostbin/cilium-sysctlfix

    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 30 Sep 2022 16:16:34 +0000
      Finished:     Fri, 30 Sep 2022 16:16:34 +0000
    Ready:          True
    Restart Count:  0
    Environment:
      BIN_PATH:  /opt/cni/bin
    Mounts:
      /hostbin from cni-path (rw)
      /hostproc from hostproc (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5v99z (ro)
  mount-bpf-fs:
    Container ID:  containerd://28c125cba378938c7b0811fda8b18ad6786cc2b05196a1cc9fed3a2ba648e153
    Image:         quay.io/cilium/cilium:v1.12.2@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Image ID:      quay.io/cilium/cilium@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Port:          <none>
    Host Port:     <none>
    Command:
      /bin/bash
      -c
      --
    Args:
      mount | grep "/sys/fs/bpf type bpf" || mount -t bpf bpf /sys/fs/bpf
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 30 Sep 2022 16:16:35 +0000
      Finished:     Fri, 30 Sep 2022 16:16:35 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /sys/fs/bpf from bpf-maps (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5v99z (ro)
  clean-cilium-state:
    Container ID:  containerd://840ce4715fd5183dab31cac7a1a1bbe78aa32758dd07504dd2ebe0ae6a44edaf
    Image:         quay.io/cilium/cilium:v1.12.2@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Image ID:      quay.io/cilium/cilium@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Port:          <none>
    Host Port:     <none>
    Command:
      /init-container.sh
    State:          Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 30 Sep 2022 16:16:36 +0000
      Finished:     Fri, 30 Sep 2022 16:16:36 +0000
    Ready:          True
    Restart Count:  0
    Requests:
      cpu:     100m
      memory:  100Mi
    Environment:
      CILIUM_ALL_STATE:         <set to the key 'clean-cilium-state' of config map 'cilium-config'>      Optional: true
      CILIUM_BPF_STATE:         <set to the key 'clean-cilium-bpf-state' of config map 'cilium-config'>  Optional: true
      KUBERNETES_SERVICE_HOST:  127.0.0.1
      KUBERNETES_SERVICE_PORT:  6443
    Mounts:
      /run/cilium/cgroupv2 from cilium-cgroup (rw)
      /sys/fs/bpf from bpf-maps (rw)
      /var/run/cilium from cilium-run (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5v99z (ro)
Containers:
  cilium-agent:
    Container ID:  containerd://b24acc1625efac9be723368e13803d67d146bc8132f366a12096af99de1cd31b
    Image:         quay.io/cilium/cilium:v1.12.2@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Image ID:      quay.io/cilium/cilium@sha256:986f8b04cfdb35cf714701e58e35da0ee63da2b8a048ab596ccb49de58d5ba36
    Port:          <none>
    Host Port:     <none>
    Command:
      cilium-agent
    Args:
      --config-dir=/tmp/cilium/config-map
    State:          Running
      Started:      Fri, 30 Sep 2022 16:16:37 +0000
    Ready:          True
    Restart Count:  0
    Liveness:       http-get http://127.0.0.1:9879/healthz delay=0s timeout=5s period=30s #success=1 #failure=10
    Readiness:      http-get http://127.0.0.1:9879/healthz delay=0s timeout=5s period=30s #success=1 #failure=3
    Startup:        http-get http://127.0.0.1:9879/healthz delay=0s timeout=1s period=2s #success=1 #failure=105
    Environment:
      K8S_NODE_NAME:               (v1:spec.nodeName)
      CILIUM_K8S_NAMESPACE:       kube-system (v1:metadata.namespace)
      CILIUM_CLUSTERMESH_CONFIG:  /var/lib/cilium/clustermesh/
      CILIUM_CNI_CHAINING_MODE:   <set to the key 'cni-chaining-mode' of config map 'cilium-config'>  Optional: true
      CILIUM_CUSTOM_CNI_CONF:     <set to the key 'custom-cni-conf' of config map 'cilium-config'>    Optional: true
      KUBERNETES_SERVICE_HOST:    127.0.0.1
      KUBERNETES_SERVICE_PORT:    6443
    Mounts:
      /host/etc/cni/net.d from etc-cni-netd (rw)
      /host/opt/cni/bin from cni-path (rw)
      /host/proc/sys/kernel from host-proc-sys-kernel (rw)
      /host/proc/sys/net from host-proc-sys-net (rw)
      /lib/modules from lib-modules (ro)
      /run/xtables.lock from xtables-lock (rw)
      /sys/fs/bpf from bpf-maps (rw)
      /tmp/cilium/config-map from cilium-config-path (ro)
      /var/lib/cilium/clustermesh from clustermesh-secrets (ro)
      /var/lib/cilium/tls/hubble from hubble-tls (ro)
      /var/run/cilium from cilium-run (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5v99z (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  cilium-run:
    Type:          HostPath (bare host directory volume)
    Path:          /var/run/cilium
    HostPathType:  DirectoryOrCreate
  bpf-maps:
    Type:          HostPath (bare host directory volume)
    Path:          /sys/fs/bpf
    HostPathType:  DirectoryOrCreate
  hostproc:
    Type:          HostPath (bare host directory volume)
    Path:          /proc
    HostPathType:  Directory
  cilium-cgroup:
    Type:          HostPath (bare host directory volume)
    Path:          /run/cilium/cgroupv2
    HostPathType:  DirectoryOrCreate
  cni-path:
    Type:          HostPath (bare host directory volume)
    Path:          /opt/cni/bin
    HostPathType:  DirectoryOrCreate
  etc-cni-netd:
    Type:          HostPath (bare host directory volume)
    Path:          /etc/cni/net.d
    HostPathType:  DirectoryOrCreate
  lib-modules:
    Type:          HostPath (bare host directory volume)
    Path:          /lib/modules
    HostPathType:
  xtables-lock:
    Type:          HostPath (bare host directory volume)
    Path:          /run/xtables.lock
    HostPathType:  FileOrCreate
  clustermesh-secrets:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  cilium-clustermesh
    Optional:    true
  cilium-config-path:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      cilium-config
    Optional:  false
  host-proc-sys-net:
    Type:          HostPath (bare host directory volume)
    Path:          /proc/sys/net
    HostPathType:  Directory
  host-proc-sys-kernel:
    Type:          HostPath (bare host directory volume)
    Path:          /proc/sys/kernel
    HostPathType:  Directory
  hubble-tls:
    Type:                Projected (a volume that contains injected data from multiple sources)
    SecretName:          hubble-server-certs
    SecretOptionalName:  0xc0007905ea
  kube-api-access-5v99z:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              kubernetes.io/os=linux
Tolerations:                 op=Exists
                             node.kubernetes.io/disk-pressure:NoSchedule op=Exists
                             node.kubernetes.io/memory-pressure:NoSchedule op=Exists
                             node.kubernetes.io/network-unavailable:NoSchedule op=Exists
                             node.kubernetes.io/not-ready:NoExecute op=Exists
                             node.kubernetes.io/pid-pressure:NoSchedule op=Exists
                             node.kubernetes.io/unreachable:NoExecute op=Exists
                             node.kubernetes.io/unschedulable:NoSchedule op=Exists
Events:                      <none>
```