
challenge is different kernel version, etc

How to send data:
- perf buffer -> extra memory copy, variable size
- ring buffer -> no extra memory copy, fixed size

BTF -> see seperate md file

kprobes

XDP:
- cilium
- Katran: L4 loadbalancer
- LoxiLB
- Merbridge: service mesh

Tracing: -> syscall
- bpftrace (DSL)
- kubectl-trace
- pixie
- pyroscope: profiling
- parca: profiling
- wachy
- inspektor gadget
- hubbek
- keppler

Security: (actions)
- Falco
- Tracee
- Tetragon
- Kubearmor
- Pulsar: written in rust

[ebpf apps](ebpf.io/applications)

Help creating and 
- bcc
- L3AF
- bumblebee: packaging

Aya/bpflinker -> RUST
libbpf and bpftrace are hard to learn

verifier:
- used when loading a program
- skb -> socket buffer pointer
- why a verifier iso compiler
  - types -> verifier is having its own TYPES
  - value -> arr[i] => using if statement and with amask
    - verifier uses byte code and registers


XRP:
- offload an eBPF in the kernel to offload kernel overhead in storage