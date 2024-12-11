## AMD overview 19 Sept

Endpoint: AI PC
- 1-10s of TOPS
- AMD Ryzen
    - 50 TOPs
    - all on NPU, offloading from CPU and DPU
        -> NPU: neural processing


Embedded/edge: (zylynx)
- AMD Versal
    - heathcare (medical imaging, surgical robotics, sientific resoearch)
    - automotive 
    - industrial
    - 10x scalr , ARM subsystems

Cloud:
- AMD EPYC: CPU
    - 5th gen AMD
        - 192 cores, 384 threads
        - 2H 2024, SP5 socket

- AMD Instinct (GPU) 
    - MI300A: GPU and CPU chiplets - HBM chiplets -> HPC
    - MI300X: only GPU chiplets -> AI/Hyperscalers
    2024: 2,4x HBM, 1,6 x more memory BW
        192GB
    - MI325X: 288GB, 6TB/s (Q1/2025) - 400G
    - MI350: (2025) compute and memory - 400G
    - MI400: (2026) -> NEW fabric interconnect
        800G
        Liquid cooled
        partnership with Cisco/Broadcom
        pod: 256 GPU(s)
        UALInk which was infinityFabric based XGMI

- AI NIC: polara 400G -> pensando based using P4
    - Q1 2025 GA
    - 30-60K GPU
    - PFC too complex
    - SACK retransmission iso goBackN
    - UDP port hashing (iso)
    - No encryption
    - Receive buffer/reordering
    - Distance ????
    - 800G (2026)
    
Infiniband crossbar -> HPE Frontier
    - El capitan -> cray/slingshot
    - 

FlashAttention
KVCache
OpenAI: compiler - triton compiler

Ecosystem:
- pyTorch (RoCM open source), (ZenDNN - CPU focussed), Vitis AI (embedded)
- openAI triton
- vLLM (inference server)


SILO AI
Zt Systems -> rack scale systems

-> if written
PyTorch: NVIDEA -> works at AMD, but the performance is not optimized
CUDA: NVIDEO -> works at AMD, but the performance is not optimized