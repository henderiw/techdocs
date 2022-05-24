# getting started with buf

## terminology

- BSR: Buf Schema Registry
- Module: initialized using buf.yaml file

```
git clone https://github.com/bufbuild/buf-tour.git
```

## configure buf

```
buf mod init -> generates a buf.yml file
```

```
version: v1
lint:
  use:
    - DEFAULT
breaking:
  use:
    - FILE
```

-> it is analogous to the -I path in protoc whre it should be placed

## build the api

buf build
-> no error means we will not generate an error
buf build --exclude-source-info -o -#format=json | jq '.file[] | .package'

## list files

buf ls-files

buf ls-files https://github.com/bufbuild/buf-tour.git#branch=main,subdir=start/petapis

## lint the api

buf lint

buf lint --error-format=json

buf lint "https://github.com/bufbuild/buf-tour/archive/main.tar.gz#strip_components=1,subdir=start/petapis" --config buf.yaml

## detect breaking changes

buf breaking --against ../../.git#branch=main,subdir=start/petapis

## generate code

brew install protobuf

-> creates a gen/proto directory with the respective code

## log into the BSR

[login to buf](https://buf.build/login)

export BUF_USER=henderiw

buf registry login

with api token

cat ~/.netrc 

## push a module

- modules: a collection of proto files -> configured, built and versioned as a logical unit; is initialized using buf/mod file
- repositories: only exist in a remote location, do not exist in multiple locations, unlike git
- module names: + 3 other components
    - remote: the dns name buf.build
    - owner: the user or organization that owns the repo
    - repository: repository name

```
buf beta registry repository create buf.build/$BUF_USER/petapis --visibility public
```

in buf.yaml

```
version: v1
+name: buf.build/$BUF_USER/petapis
 lint:
   use:
     - DEFAULT
 breaking:
   use:
     - FILE
```

```
buf push
```

## generate documentation

add a byf.md file

```
## PetAPIs

This module contains all of the APIs required to interact with the `PetStoreService`.
```

buf push

## dependency

buf.yaml

```
version: v1
name: buf.build/henderiw/petapis
deps:
  - buf.build/googleapis/googleapis
breaking:
  use:
    - FILE
```

```
buf build
buf mod update
```

BSR dependency management

- buf noticed there is a dependency using the deps key
- buf resolved the latest version and wrote it to buf.lock (buf build)
- When another buf command is run, buf downloads the buf.build/googleapis/googleapis module to the local module cache.

pinning dependencies

buf.yaml file

```
 version: v1
 name: buf.build/$BUF_USER/petapis
 deps:
-  - buf.build/googleapis/googleapis:4bdf33e750fb409da9d403e1e98031f4
+  - buf.build/googleapis/googleapis
 lint:
   use:
     - DEFAULT
 breaking:
   use:
     - FILE
```

## generate go code

```
export GOBIN=$HOME/go/bin
export PATH="$PATH:$(go env GOPATH)/bin"
```

```
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest
```

buf.gen.yaml

```
version: v1
plugins:
  - name: go
    out: gen/proto/go
    opt: paths=source_relative
  - name: go-grpc
    out: gen/proto/go
    opt:
      - paths=source_relative
      - require_unimplemented_servers=false
```

```
buf generate buf.build/$BUF_USER/petapis
```

If a --template isn't explicitly specified, the buf.gen.yaml found in the current directory is used by default.

## grpc endpoints

```
go mod init github.com/bufbuild/buf-tour/petstore
```

## workspace

initialize the workspace

```
mkdir <dir>
cd <dir>
buf mod init
add name in the buf.yaml file
```

add the proto files

```
mkdir -p payment/v1alpha1
touch payment/v1alpha1/payment.proto
implement the proto file
```

build the module and add dependencies

```
version: v1
name: buf.build/$BUF_USER/paymentapis
deps:
  - buf.build/googleapis/googleapis
lint:
  use:
    - DEFAULT
breaking:
  use:
    - FILE
```

```
buf mod update
buf build
```

buf.work.yaml

```
version: v1
directories:
  - paymentapis
  - petapis
```

```
buf.work.yaml
```

## managed mode

