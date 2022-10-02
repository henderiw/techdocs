# bpftrace

[bpftrace](https://github.com/iovisor/bpftrace/blob/master/INSTALL.md)

```
sudo bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'
```

only bpf systemcalls

```
sudo strace -e bpf bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @[comm] = count(); }'
```

