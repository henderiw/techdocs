# kindnet

cni for kind cluster

[kindnet repo](https://github.com/aojea/kindnet)

uses CNI-plugins
- ptp or bridge
- host-local
- portmap

kindnet daemon:
- CNI config
- routing: routing between pods
- ipmasq: non masquerade traffic that is directed to the POD

## daaemonset

- init container to install the cni binaries
- regular container: 
    - HOST_IP, POD_IP
    - securityContext:
          privileged: false
          capabilities:
            add: ["NET_RAW", "NET_ADMIN"]

## daemonset code

- host ip and pod ip need to be the same
- mtu is checked by eth0
- check if uses bridge or ptp cni plugin
    for bridge offload can be set
- get v4 and v6 pod subnets from kubeadmin or kubeproxy -> determines single or dual stack or error is none are defined
- update and sync iptables forever to avoid masquerading the ips of the pod network
- create a nodes reconciler (lists nodes) -> update route table
    - every node gets a /24 and the route syncer adds a default route to the host ip and add a route to every other node it sees in the cluster

## /etc/cni/net.d/10-kindnet.conflist

with cni type bridge

```json
{
	"cniVersion": "0.4.0",
	"name": "kindnet",
	"plugins": [
	{
		"type": "bridge",
		"bridge": "kind-br",
		"ipMasq": false,
		"isGateway": true,
		"isDefaultGateway": true,
		"hairpinMode": true,
		"ipam": {
			"type": "host-local",
			"dataDir": "/run/cni-ipam-state",
			"ranges": [
				[ { "subnet": "10.244.0.0/24" } ]
			]
		}
	},
	{
		"type": "portmap",
		"capabilities": {
			"portMappings": true
		}
	}
	]
}
```

