# rdma versus sendrecv

[rdma versus send/recv](https://www.hpcwire.com/2006/08/18/a_critique_of_rdma-1/)

How to determine the destination buffer

- Send/Recv
    - SRC issues a Send: describes the location of the data to be sent
    - DST posts a Recv: describes where the data will be written
    - A matching capability is used to associate a posted Recv to an incoming Send
    - A 2 sided interface
- RDMA
    - Origin and Destination buffers must be registered prior to any operation
    - A handle is returned that can be used by the RDMA operations (Read/Write) aka Get/Put, to describe the origin or destination buffer
    - A One sides interface

Matching is key in MPI
- MPI Recv is associated to a MPI Recv according to several criteria, such as
    - Sender
    - Tag
    - Context
- A Send can be posted before the matching MPI Recv is ready -> need to deal with UNEXPECTED messages

Infiniband Verbs: no matching support
- Associate incoming Sends with outstanding Recv in order in which recv where posted
- Consequence:
    - Send has to be done in the same order as recv buffers were posted
    - Shared recv queue: no guarantee about the order between senders

RDMA benefit: 
- ZERO copy
    - avoids intermediate memory copies
    - MPI:  difficult to implement and needs synchronization


[ARMCI](https://hpc.pnl.gov/armci/)
[UPC unified parallel C](https://en.wikipedia.org/wiki/Unified_Parallel_C#:~:text=Unified%20Parallel%20C%20(UPC)%20is,clusters).)