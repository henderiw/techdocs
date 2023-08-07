1000 gpu together
-> parameters drives # gpu -> bigger networks
-> rdma (lossless transfers)
-> job completion time is what matters
-> many different networks (memory ) -. GPU compute, genral compute, storage, management
    -> GPU2GPU, GPU2Storage, memory, management, compute
-> platform play -> comm libraries + smartNICs = switches

[ietf github](https://github.com/Yingzhen-ietf/AIDC-IETF117/blob/main/AIDC.md)

why a different network?
- high bw => 400G at the host
- low latency
- lossless
- preditable performance
- robust network

NO oversubsription
RDMA -> low entropy, no underutilization

Deep buffers are not necessarily good

distributed computation vs distribute transfers

dragonfly topologies:
- dynamic adaptive routing in dragon fly
- happens on the nic with flow label as a path steering solution => based on ECN feedback
- routing: virtual links required for non-minimal paths

[dragonfly routing yandex ietf](https://datatracker.ietf.org/meeting/117/materials/slides-117-rtgwg-sessa-14-dragonfly-routing)

ztp alike infiniband

questions:
- redundant nic? no too expensive


[cuda spec](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#)
