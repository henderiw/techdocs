# grpccurl

## code

add the following line in the grpc server

reflection.Register(grpcServer)

import "google.golang.org/grpc/reflection"


## usage

```yaml
cat <<EOF | kubectl apply -f -
  apiVersion: v1
  kind: Pod
  metadata:
    name: grpcurl
    namespace: fnrun
  spec:
    containers:
    - name: grpccurl
      image: golang:1.19
      command: [ "/bin/sh", "-c", "--" ]
      args: [ "while true; do sleep 30; done;" ]
EOF
```

login in the container

k exec -ti grpcurl /bin/bash

install grpcurl
go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest


## commands

insecure is plaintext

List the services enabled on the grpc server

```
grpcurl -plaintext 10.244.0.69:9446 list
executor.FunctionExecutor
grpc.health.v1.Health
grpc.reflection.v1alpha.ServerReflection
```

List the services within the service

```
grpcurl -plaintext 10.244.0.69:9446 list executor.FunctionExecutor
executor.FunctionExecutor.ExecuteFunction
```

Execute the service

```
grpcurl -plaintext 10.244.0.69:9446 executor.FunctionExecutor.ExecuteFunction
ERROR:
  Code: Internal
  Message: failed to execute function "" with stderr failed to evaluate function: error: unexpected end of JSON input with bytes
```