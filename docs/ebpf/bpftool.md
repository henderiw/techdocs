# ebf tool

[bpf tool info](https://github.com/qmonnet/echo-bpftool)

quentin monnet

## load the program

```
bpftool prog load counter_nobtf.o /sys/fs/bpf/counter_nobtf type xdp ==debug
```

when loading the program a map id is assigned

bpftool prog show

-> show byte code

bpftool prog dump xlated pinned /sys/fs/bpf/counter_nobtf
bpftool prog dump jited pinned /sys/fs/bpf/counter_nobtf

-> show map

bpftool map show
bpftool map dump name counter_map

-> attach program

bpftool net attach xdp pinned /sys/fs/bpf/counter_nobtf dev enp3s0

bpftool net show

## btf 

on newer kernel a 

sudo bpftool btf dump file /sys/kernel/btf/vmlinux | grep task_struct -m 1

## ctf challenge

xxd -r -p
52 75 6e 20 63 68 6d 6f  64 20 6f 6e 20 61 20 66 69 6c 65 20
Run chmod on a file

sudo bpftool perf list

sudo bpftool prog list
touch hello.txt
chmod hello.txt

sudo bpftool map dump name ctf_flag

## ctf challenge 3

crictl ps
ps -e f  | grep ctf
sudo nsenter -n -t 64631
sudo bpftool prog show id 13627
sudo bpftool prog dump xlated id 13627

-> shows dropping

sudo nsenter -n -t 64631
-> in the container
ip link set dev eth0 xdpgeneric off

-> networkpolicy.io
-> https://editor.cilium.io/?id=nAujd52rvzgb9gi6

```
henderiw@ctf:~$ cat policy.yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: cilium-allow
  namespace: default
spec:
  endpointSelector: {}
  egress:
    - toEndpoints:
        - matchLabels:
            io.kubernetes.pod.namespace: kube-system
            k8s-app: kube-dns
      toPorts:
        - ports:
            - port: "53"
              protocol: UDP
          rules:
            dns:
              - matchPattern: "*"
    - toEndpoints:
        - {}
    - toFQDNs:
        - matchPattern: "*.cilium.io"
      toPorts:
        - ports:
            - port: "443"
        - ports:
            - port: "80"
```