# submariner

[submariner](https://submariner.io)

## architecture

aims to provide multi-cluster connectivity and is cni agnostic
- cross-cluster L3 connectivity using encrypted or unencrypted connetcions
- service discovery accross clusters (lighthouse)
- interconnecting clusters using overlapping IP(s)

components
- Gateway Engine: manages secure tunnels to other clusters
    - dataplane (libreswan, wireguard, vxlan)
    - active/ passive gateway is supported
    - communicates Endpoint and CLuster info to the Broker:
        - push to broker -> local cluster/endpoint information
        - watch broker for -> remote cluster/endpoint information
- Route agent: routes cross-cluster traffic from nodes to the active gateway engine
- Broker: facilitates the exchange of metadata between gateway engines for discovery
    - deployed on a public endpoint - exposes the k8s api of the cluster
    - CRD(s) consumed
        - Endpoint: ip(s) of the gateway engines
        - Cluster: info on originating cluster such as service and pod CIDR(s)
- service discovery: cross cluster service discovery (lighthouse agent)
    - uses dns exhange using the clusterset.local domain name
- globalnet controller (optional): handles interconnection of clusters with overlapping CIDR(s)
    - pod and service cidrs are typically deployed using the default cidrs (all clusters have overlapping ip(s))
    - perform SNAT/DNAT using global ip(s) allocated globally

## terminology and concepts

- clusterset: a group of 2 or mote clusters with a degree of mutual trust that share services amongst themselves
    - namespace is globally unique
- ServiceExport CRD
    - service dns record: <service>.<ns>.svc.clusterset.local
    - headless dns record: <pod-name>.<cluster-id>.<svc-name>.<ns>.svc.clusterset.local
- ServiceImport CRD

## analysis

- gateway is a bottleneck (only active/passive support)
- broker is a single point of failure -> when it is down no control plane updates are possible
- 