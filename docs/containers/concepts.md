# container concepts

[container vocabulary](https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#containers_101)


## crio

kubelet <--grpc--> crio <--> runc

create pod -> sandbox
create containers -> within the sandbox

[crio api](https://github.com/kubernetes/cri-api/blob/master/pkg/apis/runtime/v1/api.proto)

## podman

