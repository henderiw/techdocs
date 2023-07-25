# cni overview

[cni docs](https://www.cni.dev)


  +------+          +-------------+
  ! POD or Container| runtime (kubletor other, like podman, cloudfoundry)
  +------+          +-------------+
     |                   | Add/Del/Check/Version
     |<------- CNI-------+
     |
     +---------------- Network



+----------+        +-------------------+                         +------------+
| runtime  |        | env vars:         |                         | exit code  |
| kubelet  +--------+ - CNI_COMMAND     |      +----------+       |            |
|          |        | - CNI_CONTAINERID |      | cni      |       |            |
+----------+        | - CNI_IFNAME      +------+ binary   +-------+------------+
                    | - CNI_NETNS       |      |          |       | stdout:    |
                    +-------------------+      |          |       | json       |
                    | stdin:            |      +----------+       |            |
                    | - json conf       |                         +------------+
                    +-------------------+

## overview cni project

- specification
    - JSON doc
        - name
        - type -> some parameters are tied based on the types
        - ipam
    - verbs: add, del, check, version
- reference plugins
    - interface plugins:
        - ptp, bridge, macvlan, ipvlan
    - chained plugins
        - ipam: host-local, dhcp, static
        - meta: bw, firewall, flannel, portmap, source based routing, tuning
    - chain is linear (verbs calls them in order, del is reverse order)
- libcni: go lib used by runtimes (convenience functions)
    - version handling
    - parse result and config caching -> used to validate which config was used, etc

## execution flow

- plugin is executabale
- spawned by runtime (kubelet or other runtimes)
- fed json through STDIN
- fed container-specific data through STDIN
- report structured result via STDOUT

## vlan tagging

- ipvlan, macvlan, bridge: all requires the host to be prepared
- sriov/vlan/hostconfig: no host preparation required

-> openshift has an operator for this

## plugins

[plugin github](https://github.com/containernetworking/plugins)