## BTF

BTF: BPF type format -> allows for portability
- CORE
  - compile once, run everywhere
  - compiled BPF + BTF -> loader library (adjust program) -> patched eBPF program
- available on newer kernels
  - CONFIG_DEBUG_INFO_BTF=y
  - RHEL 8.2+
  - Ubuntu 20.10
- /sys/kernel/btf/vmlinux


BTFHub -> used for older kernels
- 5MB in size -> not possible to distribute
- bpftool gen min_core_btf


files located here

ls /sys/kernel/btf