# container concepts

[container vocabulary](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#containers_101)


## crio

kubelet <--grpc--> crio <--> runc

create pod -> sandbox
create containers -> within the sandbox

[crio api](https://github.com/kubernetes/cri-api/blob/master/pkg/apis/runtime/v1/api.proto)

## podman

## linux concepts

[unshare-user-namespaces](https://ericchiang.github.io/post/user-namespaces/)
[minimal container youtube](https://www.youtube.com/watch?v=gMpldbcMHuI)
[containers under the hood](https://ericchiang.github.io/post/containers-from-scratch/)
[unshare](https://man7.org/linux/man-pages/man1/unshare.1.html)
[podman unshare](https://man.archlinux.org/man/community/podman-docker/docker-image-mount.1.en)

1. container files system (rootfs)
2. chroot (syscall) ->  restrict a process’ view of the file system
    - sudo chroot rootfs /bin/bash
    - sudo chroot rootfs python -m SimpleHTTPServer
    - host process tree is still visible -> no containment
3. create process namespace with unshare (syscall)
    - sudo unshare -p -f --mount-proc=$PWD/rootfs/proc \
        chroot rootfs /bin/bash
    - shell is PID 1, we cannot see the host processes
4. entering namespaces with nsenter (syscall setns)
    - /proc/(pid)/ns/
    - sudo nsenter --pid=/proc/29840/ns/pid \
        unshare -f --mount-proc=$PWD/rootfs/proc \
        chroot rootfs /bin/bash
5. getting around chroot with mounts
    - sudo mount --bind -o ro $PWD/readonlyfiles $PWD/rootfs/var/readonlyfiles
6. cgroups
    - /sys/fs/cgroup