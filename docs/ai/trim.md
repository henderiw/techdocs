# trim sai discussion

- Is TRIM queue
- Are all ports configured with same number of queues and same TRIM queue index
- How is the TRIM queue derived?
    DSCP -> TC -> Queue
    Static binding of the queue
- How much of the shared buffer is dedicated to the TRIM queue?
- What kind of counters are needed?
- Is TRIM a configurable?
    - global
    - per port
    - per queue
- Is all the traffic through UE fabric subjected to TRIM or there is a subset of traffic that need to undergo the TRIm flow?


- TRIMMABLE
- control

Implementation:
- ACL Table is required

SAI Logical Pipeline
- 

- global scope config
    - TRIMMING SIZE -> MIN is needed so the receiver can identify the source
        - TRUNCATE SIZE seems a better naming (iso MAX)
    - TRIMMING DSCP -> TRIMMED PKT DSCP
    - Congestion Proposal
    - ACL: disable trimming
    - Burn ACL rules on egress
    - Burn ACL rules on ingress
