# eBPF

BPF is like a VM construct
- allows to execute bytecode at various hook points

BPF architecture
- instruction set: -> restricted set of C
- maps -> sharing info between kernel space and user space
- helper functions to intercat with and leverage kernel functionality -> help with contextual information
- tail calls for calling into BPF programs
- security hardening primitives
- pseudo file system for pinning objects (maps, programs)
- infra to offload to a NIC

LLVM -> backend for tools like c-lang to comile C into a BPF object file

BPF triggered by events:
- in response to system calls -> e.g. hook on syscall, fn entry/exit, kernel tracepoint, network event
- kprobe entry on kernel function

Subsystems:
- XDP: no meta data
- TC
- kprobes
- uprobes
- tracepoints
- ...

challenge is different kernel version, etc

## linux instruction set

[kernel bpf instruction set](https://www.kernel.org/doc/html/latest/bpf/instruction-set.html)


## compilers

libbpf
bpf2go -> compiler using go generate written by cilium/ebpf

[sk lookup example](https://github.com/fbac/sklookup-go)

## other

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

## tools

libbpfgo -> go wrapper around libbpf

ELF object file 

[bpf and xdp refrence guide](https://docs.cilium.io/en/latest/bpf/)

## instruction set

BPF consists of:
- 11 64bit registers (R0-R10)
  - with 32 subregisters
  - a program counter
  - 512 byte large BPF stack space
- operate in 64 bt, 32 bit sureisters can only be access through special ALU (algorhitmic logic unit) operations
- R10: read-only
- R0-R9: read-write
  - R0: contains the return value of a helper function call
  - R1-R5: hold argument from the BPF program to the kernel helper function
  - R6-R9: are callee save registers