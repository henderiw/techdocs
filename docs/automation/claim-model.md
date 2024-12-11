# claim model

[claim model](https://itnext.io/what-is-the-kubernetes-claim-model-1572d7cf39a8)

1. producer/consumer decoupling pattern
    - facilate separation of roles
    - requester (consumer) 
        - does not have permissions to directly provision that resource
        - does not need to know how and what criteria are being used
    - implementation can seperate concerns (who does what is irrelavant to the consumer)
2. provisioning/use decoupling
    - late binding
    - provisioning and setup cna be done in advance
    - can enable auto-provisioning
3. recycle/reuse
4. sharing/suballocation
    - 