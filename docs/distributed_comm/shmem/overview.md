# shmem

- [open shmem spec](http://www.openshmem.org/site/sites/default/site_files/OpenSHMEM-1.4.pdf)

## Terminology

- `PGAS`: partitioned global address space
- `PE`: processing elements or processes
- `SPMD`: Single Program Multiple Data
- `Private Data Objects`
- `Remotely accessible symmetric data objects`

## Goal
- implements `PGAS` by defining:
    - remotely accesible data objects as mechanims to share information among `OpenSHMEM` `PE(s)`
    - private data objects that are accesible by the PE itself
- API allows communication and synchronous operations on bpth private and remotely accessible data objects
- Data transfer operations are one side only
    - a local PE executing a data transfer routine does not require the remote PE to complete the routine
    - allows for overlap between communication and computation to hide data transfer latencies
    - ideal for unstructured, small medium sized data transfers.
- used to implement `SPMD` programs
    - divide problem into multiple sub problems that can be solved independently or with coordination

## OpenSHMEM routines

- library setup and query
- symmetric data object management
- communication management
- remote memory access
- atomics
- synchronization and ordering
- collective communication
- mutual exlcusion
- data cache control
    - mechanisms to exploit the capabilities of the HW cache

## memory model

- private data objects: only accessible by the local PE
- remote data objects: accessible by SHMEM routines
    - called `Symmetric Data Objects`
    - corresponding object with the same name, type and size on all PE(s).
    - `shpalloc` and `shmem_malloc` allow collective allocation of `Symmetric Data Objects`

## execution model

- initilaization routine (`shmem_init` or `shmem_init_thread`)
- program closure: `shmem_finalize` or `shmem_global_exit`.
- PE(s) have unique ids
