# block solution for UET

NVME over UET

now:
NVME over RDMA

UET mapping:
- map RDMA_SND to UET_SEND
    q? is tagged send needed

- map RDMA_WRITE to UET_WRITE and RDMA_READ to UET_READ

- use RUD?
    - multipathing (would be nice to leverage this)
    - ordering: storage devices dont care about the order
        - control command: write and read -> they independently need to be ordered
        - fuse command need to be order
        - completion cannot come before data arrives

- disocvery

- security


connectionless architecture
