# implementation details

1. options (server options)
extension apiserver: scheme is fixed
builder apiserver: schema is dynamic based on the resources it serves

- etcd path
- openapi definitions
- resource/storage/ etc etc

-> in the options we provide the codec, defaultEtcdpath, etc

extension apiserver
- serverRunOptions
- recommendedOptions -> etcd, codec
- apiEnablementOptions -> allows to enable/disable api(s)
builder apiserver
- recommendedOptions only -> etcd, codec (based on all resources supplied)