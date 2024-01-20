# libfabric

Rajalaxmi Angadi Intel
Juee Himalbhai Desai Intel

## building blocks

how do we write a program to transfer data

traditional way:
- socket based
- connection oriented TCp, connection-less UDP
- used for client or servers

server                              client                        server                                       client
  |
  x
getaddrinfo()                       getaddrinfo()               fi_getinfo()                                  fi_getinfo()
  |                                     |                       fi_febric()                                   fi_febric()
  x                                     x                       fi_domain()                                   fi_domain()
socket()                            socker()                    fi_endpoint()                                 fi_endpoint()
  |
  x
bind()                                                          fi_ep_bind()                                  fi_ep_bind()
  |
listen()                                                        fi_listen()  block until conn established     fi_connect()
  |                                                                        <-----------------------------
accept()                                                        
                  establish conn                     
block untile the <-----------------  connect()                  fi_accept()
client connects  
                  client send a req                                           client send data to server
receive()  <---------------------->  send()                     fi_recv()   <---------------------------      fi_send()

process data 
               server replies back                              fi_close()                                    fi_close()
send()    ------------------------> receive()

close()                             close()


changing arena of HW &SW

- CPU, GPU, XPU
- Ethernet, infiniband, fiber channel, XeLink, NvLink
- SW providers
- MiddleWare libraries
- Apps

There is a need for common interface to bridge various apps/middleware with different hardware
-> libfabric (open interface) enables a tight semantic map between app and underlying fabric services

App -> libfabric kernel drivers -> hw (compute/fabric)

MiddleWatre (MPI, CCL, SHMEM) -> libfabric api (core) - provider api
    providers
        - socket provider
        - rdma provider
        - GPU
        - SHM provider

Enabling GPU communication

sockfd = connect_tcp()
xe_init()  => initialize GPU device
init_buf() => xe_alloc_buf => zeMemAllocDevice (allocate GPU buffers)
init_ofi() => init_nic -> fi_mr_regattr (register buffer with the NIC)
sync_tcp(sockfd)
for (size = 1; size <= MAX_SIZE; size <<= 1):
    run_test()
          post_rdma()
            READ: fi_readmsg,
            WRITE: fi_writemsg
    sync_tcp(sockd)
sync_ofi()
finalize_ofi()
free_buf()
clode(sockfd)

Libfabric service
- control services: used to discover fabrics
- communication interfaces: setup communciation link
- completion services: used to report the results of submitted data transfer operations
- data transfer services: fi_recv(); fi_send()
    - Message queue
    - Tag matching
    - RMA
    - Atomic operations.


API/services
fabric
    - fi_fabric()
domain
    - fi_domain()
    - fi_domain_bind()
- control service: discover
    - fi_getinfo()
- communcication service: setup communciation link
    - passive endpoints
        - fi_passive_ep()
    - address vector
        - fi_av_open()
        - fi_av_insert()
    - memory regions
        - fi_mr_reg()
        - fi_mr_desc()
        - fi_mr_key()
    - active endpoints
        - fi_endpoint()
- completion service: report the results of submitted data transfer operations
    - event queues
        - fi_eq_open()
        - fi_eq_bind()
        - fi_eq_read()
        - fi_eq_sread()
    - wait sets
    - completion queues
        - fi_cq_open()
        - fi_cq_read()
    - completion counters
        - fi_cntr_open()
        - fi_cntr_read()
    - poll sets
- data transfer service: 4 types (Mesage queu, Tag matching, RMA, Atomic operations)
    - fi_send()
    - fi_recv()
    - fi_readmsg()
    - fi_writemsg()
    - fi_sendmsg()
    - fi_recvmsg()

Examples:

// server
```c
hints = fi_allocinfo()
if (!hints)
  return EXIT_FAULURE

// similar to a socket - we req for a msg endpoint
hints->ep_attr-type = FI_EP_MSG;
// req for basic messaging capabilities
hints->caps = FI_MSG;
// req for the tcp provider
hints->fabric_attr->prov_name = "tcp";
// req FI_SOCKADDR_IN addressing format
hints->addr_format = FI_SOCKADDR_IN;
// req client does not get completion until client finsihed sending message
hints->tx_attr->op_flags = FI_DELIVERY_COMPLETE

// start server
// get list of all providers -. we use the first one
fi_getinfo()
// open fabric
fi_fabric()
// open an event queue -> connect event messaging -> bind to 
fi_eq_open()
// track connection request
fi_passive_ep()
// bind ep to event queu
fi_pep_bind()
// liste to incoming requests
fi_listen(pep);

// read event queue to make progress
fi_eq_sread()
// set of resources that can be grouped together
fi_domain()
// bind domain with event queue
fi_domain_bind()
// open a completion queue -> log data transfer completion event
fi_cq_open()
// active endpoint for data transfer -> like a socket
fi_endpoint()
//
fi_ep_bind()
// enable endpoint
fi_enable()
// server accept data
fi_accept()
// read event queue for driving progress
fi_eq_sread()

// Data transfer -> requires ep, buffer to store the message + address (any client)
fi_recv()
// read for the completion queu
fi_cq_read()

// read the completion quue
```

// client

```c
// get list of all providers -. we use the first one
fi_getinfo()
// open fabric
fi_fabric()
// open an event queue -> connect event messaging -> bind to 
fi_eq_open()
// set of resources that can be grouped together
fi_domain()
// open a completion queue -> log data transfer completion event
fi_cq_open()
// active endpoint for data transfer -> like a socket
fi_endpoint()
// bind to ev q and completion queue
fi_ep_bind()
// enable endpoint
fi_enable()

// connect to the server
fi_connect()
// event queue read -> ready for data transfer
fi_eq_sread()

// data transfer
fi_send()
// read completion queue to drive progress
fi_cq_read()

// close resource in reverse order
fi_close(ep)
fi_close(cq)
fi_close(fabric)
...

```

## GPU data transfer

ibv api versus libfabric api

```c
// socket connection + initialzation
sockfd = connect_tcp()
// api call with xe_alloc buffer
init_buf()
// initialize libfabric resources (nic) register the buffer with the nic - similar fabric/domain/cq/eq/ep/...
init_ofi()
// dummy data trasfre for further operation
sync_tcp(sockfd)
for (size=1; size <= MAX_SIZE; size <<= 1):
    // 
    run_test()
            post_rdma()
                // remote memory data transfer
                READ:fi_readmsg,
                // remote memory client to server
                WRITE: fi_writemsg
            sync_tcp(sockfd)
sync_ofi()
// closes libfabric resources - similar fabric/domain/cq/eq/ep/...
finalize_ofi()
free_buf()
close(sockfd)
```

specify where we allocate the memory -> e.g. host + message size: 1 bytes