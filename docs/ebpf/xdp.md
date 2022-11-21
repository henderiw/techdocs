# xdp

[tutorial](https://github.com/xdp-project/xdp-tutorial)

## kernel headers

/usr/include/linux



## actions

- XDP_PASS
- XDP_DROP
- XDP_ABORTED: drop with notification
- XDP_TX: send pkt back from the same interface (loadbalancer for icmp replies)
  - both sides of veth need to implement the xdp program
- XDP_REDIRECT: fwd pkt to egress port ports of other interface
- XDP_FORWARD: router lookup

## hw offloading

XDP_FLAGS_HW_MODE -> could be used in conjunction with netronome NIC

## vlan offload

```
# Check current setting:
ethtool -k DEV | grep vlan-offload
# Disable for both RX and TX
ethtool --offload DEV rxvlan off txvlan off
# Same as:
# ethtool -K DEV rxvlan off txvlan off
```

## rewrite - enlarging and shrinking

Helper:
bpf_xdp_adjust_head() -> helps in adjusting the pkt 
bpf_xdp_adjust_tail() -> helps in shrinking the pkt

## redirect

action -> XDP_TX
action -> XDP_REDIRECT

Helper:
bpf_redirect -> should not be used in production as it is slow
bpf_redirect_map

return XDP_REDIRCT

## router

action -> XDP_FORWARD

Helper:
bpf_fib_lookup() -> Forwarding needs to be enabled

sudo sysctl net.ipv4.conf.all.forwarding=1
sudo sysctl net.ipv6.conf.all.forwarding=1

## tracepoints

```
henderiw@lima-ebpf:/Users/henderiw/Documents/codeprojects/ebpf/ebpf-example/packet03-redirect$ sudo ls /sys/kernel/debug/tracing/events/xdp

enable	
mem_connect	
mem_return_failed  
xdp_cpumap_enqueue  
xdp_devmap_xmit	
xdp_redirect	  
xdp_redirect_map
filter	
mem_disconnect	
xdp_bulk_tx	   
xdp_cpumap_kthread  
xdp_exception	
xdp_redirect_err  
xdp_redirect_map_err
```

### exception

### raw tracepoints

### debug print

sudo cat /sys/kernel/debug/tracing/trace_pipe

stream = fopen(TRACEFS_PIPE, "r");