# why networking


- training 6 weeks -> core tuning
    - failures: HW/SW failures -> communication library (Go Back N)
    - 50% time to wait for data
    - GPU:
        - read mem, computation, comm
- RDMA: 
    - CCL library (runs on GPU)
    - when GPU need to send data (memory block/NIC -> block of the remote host)
- Collectiva operation
    - All to ALL
    - All Reduce: math fn over the data (sum)
        - backward pass
- Network data
    - Dependencies - Sequence
    - All pkt look the same: size is the same, period is the same -> load balance (reordering)
    - Message bursts/Incast

