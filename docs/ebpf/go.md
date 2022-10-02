# develop go module

## linux

fedora

sudo dnf instakk clang go make libbpf-devel bpftool
sudo dnf install clang make libbpf-devel

ubuntu

linux-tools-common

## go

go mod github.com/cilium/ebpf
go get github.com/cilium/ebpf/internal/unix

//go:generate go run github.com/cilium/ebpf/cmd/bpf2go -target bpfel -cc clang gen_execve ./bpf/execve.bpf.c -> used by the compiler to create an object file

## sample

masmulim2000

docuemntation

[cilium ebpf](https/github.com/cilium/ebpf)

[bpf helpers](https://man7.org/linux/man-pages/man7/bpf-helpers.7.html)

[bcc bpf reference](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md)

[bpf kernel test](https://elixir.bootlin.com/linux/latest/source/tools/testing/selftests/bpf)

/sys/kernel/btf/vmlinux