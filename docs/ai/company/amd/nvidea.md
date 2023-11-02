# nvidea

## libraries

numpy (matrix)
tensorflow (cuda)

## container

## container scheduler

kubernetes
run.ai
[flyte](https://github.com/flyteorg/flyte)

or baremetal, GPU virtualization

## GPU HW

[H100](https://resources.nvidia.com/en-us-tensor-core/gtc22-whitepaper-hopper)
- GraphicalProcessingCluster
- TextualProcessingCluster (in GPC)
- StreamingM ultiprocessor
- CUDA cores
- tensor core
- L2 Cache -> provides access to GPC
- High BW Memory (Memory controller) - 3 TB/sec 

GPU is accessable via PCIe5 or NVLink (gen4) (faster)
- NVLink: 900GB/s
- NVLink: 7x faster than PCIe Gen5

PCIegen5: 128 GB/sec - 64 GB/Sec per direction

SXM5 formfactor
- 8 GPCs, 66 TPCs, 2 SMs/TPC, 132 SMs per GPU
- 128 FP32 CUDA Cores per SM, 16896 FP32 CUDA Cores per GPU
- 4 Fourth-generation Tensor Cores per SM, 528 per GPU
- 80 GB HBM3, 5 HBM3 stacks, 10 512-bit Memory Controllers
- 50 MB L2 Cache
- Fourth-Generation NVLink and PCIe Gen 5

NVswitch: 64 ports

-> CUDA: compute unified device architecture
    does math fast, original NVIDEA
    vector based floating point
-> Tensor: more optimized for matrix operations

we need a scheduler to device which operataion goes to which core: cuda or tensor
-> CUDA library

# GPU system

DGX H100
- 8 GPU (H100)
- 2TB Memory
- 2 Xeon CPU
- 32TB internal storage: NVMe SSD
- 4 NV switches
- External: 400G infiniband

8U(s)
4 per rack (due to power)
10,2 KWatt per system
40 KW per rack
300K$ starting price

42U CPU rack was 10kWatt
GPU rack is 40 kWatt -> nee DC build

## CUDA

CUBLS
CUDNN: deep learning library

tensor flow calls CUDA -> C++/RUST

## infiniband

sub 100 nsec
no retransmissions

license cost of infiniband
was targeted as replacement for PCI

RDMA: no need for CPU