# inter dc AI

## inter-dc congestion control

## communication

- data parallel: all reduce
- model parallel: all reduce & allgather
- pipeline: Send &Recv
- MoE: all in all

topology:

data input:
- pull: 1-RTT, high latency but good reliability
- push: 0-RTT init, low latency but not reliable

data synchronization
- important for allReduce

error recovery:
- 