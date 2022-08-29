# smartnic overview

## history

- too much horsepower taken away by the main CPU
  - network: DPU/IPU
  - graphics: GPU
  - soundacrd: audio, now a chip on the board

- network:
	- DMA access
	- TOE: TCP offload engine
  	- iSCSI
  	- RDMA
  	- NFS

Other:
- DPDK
- CNS: converged network switch -> blade servers
  - virtualized NIC
- FPGA:
- RDMA: remote DMA
  - infiniband used in HPC
    - RoCE
    - iWARP


## Vendors:

- AWS: nitro runs hypervisor + storage + network
- Pensando
- Open source

Liunx foundation -> OPEN PROGRAMMABLE INFRA