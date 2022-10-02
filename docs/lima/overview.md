# lima

## motivation

docker desktop is no longer free to use for professional usage

## what

containers are based on linux-specific technologies like cgroups and namespaces

### lima-VM

opensource VM which enables to run linux VM with:
- automatic file sharing
- port forwarding
- containerd

installing containerd on MAC is difficult

lima projects wrap QEMU hypervisor with containerd and nerdctl (containerd ctl) as a homebrew package

### containerd

container engine which manages the complete lifecycle of its host system

continerd is a daemon
- listening on a UNIX socket
- exposes gRPC endpoints
- handles all the low level container mgmt tasks: storagae, image distribution, network attachemnent, etc
- implements thr CRI spec

### nerdctl

executes containerd commands -> like docker cli

lazy pulling and ocicrypt -> not suppoered with docker cli