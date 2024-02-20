# in network collectives working group

WHy?
- speedup
- offload IO

HPC:
- Barrier, Broadcast
- smaller operations (<1MB)

AI:
- AllReduce(ReduceScatter/AllGather) and AlltoAll
- large operations (>1MB)

## Communciation

- Completion Send
- Initialting Send
- Input Read(s)
- Input Writes(s)
- Output Write(s)

## collectives

### Data Movement collectives

- **Broadcast**: distribute values from one mebers to all other mebers
- **AllGather**: gather and distribute values from all members
- AllToAll: scatter data from all members to all other members
- Scatter: distribute different values from one member to all other mebers
- Gather: gather values from all members to one member

### Data Reducation collectives

- **Reduce**: combine values from all members to one member
- **AllReduce**: combines and distribute values from all members
- **ReduceScatter**: combine values from all members but scatter the result to all members

reducation functions:
- sum, min, max, product, average, logicql AND/OR/XOR, Bitwise AND/OR/XOR, Min with rank, max with rank

data types:
- floating point: 16, 32, 64
- int 8,16,32,64
- uint: 8,16,32,64
- blfloat
- FP8

conversions:
- upconvert: 8->16, 16->32, 32->64
- downconvert: 64->32, 32->16, 16->8

reproducability
- floating point operation depend on order

### synchronization callectives

- **Barrier**: sync accross all members

### FSDP -> Fully Sharded Data Parallel

2GB AllGather done by 50000 FEPs = 40.000 bytes of input data per FEP

[fsdp](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html)