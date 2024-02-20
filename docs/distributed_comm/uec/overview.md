# overview

[issues with rdma](https://arxiv.org/pdf/2302.03337.pdf)

## Terminology

- FEP: logical network endpoint
    mFEP: nic or equivalent
    sFEP: switch
- FA: FEP IP address
- PIDonFEP: process ID on a FEP
- Parallel job: collection of processes with same user
- JobID: unique ID in the cluster
- RankID: unique process ID in a job
- Initiator: (target): read, write, send
- Receiver: (destination): read resp, write req, send data
- Delivery mode
    - RUD: reliable unordered delivery
    - ROD: reliable orderd delivery
    - RUDI: reliable unordered delivery idempodent
    - UUD: unreliable, unordered delivery

## UET stack

- App (Mem)
- libfabric
- Semantic layer
- Packet delivery
- Security
- MAC

## goal/environment

- Best effort and lossless networks
- Extreme scale: Millions of endpoints
- Flexible packet transports: ROD, RUD, RUDI
- Modern congestion control
- HW offload optimize (incl. rendez-vous) and tag matching
- Built in securoty
- INC: IN network collectives

## Semantic layer

- 256K fabric endpoints
- libfabric support
    - Tag matching (exact match and wildcard)
    - Lower packet overhead options
    - atomic operations
- libfabric is a connection less API (no persistent process to process connection)
    - addressing:
        - Fabric Address (FA) identifies the NIC
        - PIDonFEP: identifies a process
        - index selects one of the resources associated with an endpoint
    - Authorization:
        - based on being part of a job
- 

## PDS reliability

## PDS congestion control

## security





### tagged send

- Tagged send: 
    Are commonly used in message-passing systems, where processes communicate by exchanging messages. In a distributed system, where computations are distributed across multiple nodes or processors, effective communication is essential. Tags provide a way to differentiate between different types of messages and help the receiving process understand how to handle each message appropriately.
- PGAS: Partitioned Global Address Space
    PGAS is a programming model that simplifies the task of programming parallel applications by providing a global address space abstraction while also allowing for explicit data distribution across a parallel system.
    Examples:
        - `Broadcast` (or One-to-All): One process sends data to all other processes in the group.
        - `Gather (or All-to-One)`: All processes send their local data to one process.
        - `Scatter (or One-to-All)`: One process sends data to all other processes in the group.
        - `Reduce`: All processes contribute their data, and the result is computed using a specified operation (e.g., sum, product) and then distributed back to all processes.

