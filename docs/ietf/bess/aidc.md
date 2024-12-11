# aidc

Requirement for supporting AI

Agenda: https://github.com/Yingzhen-ietf/AIDC-IETF120/blob/main/AIDC%20Side%20Meeting%20Agenda.md
Presentations: https://github.com/Yingzhen-ietf/AIDC-IETF120
Remote attendance: https://ietf.webex.com/meet/ietfsidemeeting2

- routing for AI training
    History:
    - 100K/20MWatt; ECMP was the new thing; East-West (map-reduce)
    - TCP with fat flow; ECN/DCTCP
    - RDMA was not popular
    Now:
    - GPUDDirect
    - data parallism
    - model parallilsm
    - flows:
        logical: all-to-all/all-reduce/all-gather/reduce-scatter
        NICL: exchange data between CPU/GPU
        -> callective communication
    - fabrics:
        - N/S
        - E/W
        - NVLink: 9x more BW than E/W -> issue is power
    - New worlds
        - RDMA is full line rate -> fat flows is a fact
            - NCCL can have MPTCP alike behavior
        - collectives: 
            - ring: multiple hops -> latency more problimatic than congestion
            - trees: congestion/incast is the challange
        - resiliency:
            - rail based design (allows to keep 1 hop)
                - NCCL does the placement to a rail
                - loosing a switch has big impact
                - optics required 
            - leaf/spine
                - copper (more reliable)
                - loadbalancing at the TOR
                    - more uplinks
                - 16 + 2 spines for resilience
            - rail with spine
                - NCCL does the loadbalancing ()
                - ALL to ALL is more BW
                - optics in GPU/leaf
        - load-balancing
            - beyond ECMP
                - adaptive routing: loadbalance based on congestion of the fabric
                - flowlet/packate spraying
        - 100K clusters
            - 100-150 MW for a 100K cluster
            - 100-200W per CPU; now 1KW per GPU
            - 22-25W for 1,6T OSPF -> power contribution 
            - shallow fat-tree : NIC fine grained load-balancing
            - single tier 512 port easier to troubleshoot

Eddie Ruan (ALibaba) - SONiC
    - HON network
    - differences:
        - GPU connected to 2 TOR(s) iso 1
            -> checkpointing is not reliable
            -> ARP broadcast
        - Rail optimized design
        - 15K is one building
        - alternative marking DSCP

perceptive routing:
    - 

Queue pair



## ietf 121

### meta (Adi Gangidi)

- recomendation engine
- generative AI -> bigger model better results (training)
- inference for genAI (concurrent requests increase)
    -> to serve these models we need a different architecture
    -> inference systems need to get distributed

network: RDMA -> ROCEv2/PFC -> 100K or larger

SW stack
- pytorch
- *CCL
- CUDA/IB/Virbs
- CPU/GPU/NIC

MAST/SLURM -> scheduler
Routing
NW switch

recomendation models -> 

AlltoAll: 65,6
AllReduce: 13
AllGather: 22,1
ReduceScatter: 19,6

model serving -> lots of small messages

### nvidea Petr Lapukhov (Nvidia)

ToR: what is it good for?

NVLink: 9x scaled out NIC
- NVswitch

NCCL: ring topology was the first logical topology used
    -> logical rink
    -> step1: once you go from tor up -> ECMP (load balancing)
        -> pro: copper cables
        -> con: congestion when going between tors
        -> need adaptive routing
    -> step2: rail based design
        -> 64/8
        -> rail group
        -> con: need optics
        -> job parellism -> scheduling needs to be aware
        -> maintenance for a switch
        -> no integrations at the SI sites
        
rail:
- pro:
    - save $
    - cut switch hops - avoid load balancing
    - BUT...
- con:
    - switch down -> impact 512 servers
    - scale limits: 512
    - copper
    - larger NVL domains

### google (JK Lee (Google))

