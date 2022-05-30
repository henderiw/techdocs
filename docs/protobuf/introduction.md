


##

[protobuf with go modules](https://stepan.wtf/importing-protobuf-with-go-modules/)

go mod vendor

protoc $(find ./apis/ -name '*.proto') --gofast_out=. --gofast_opt=paths=source_relative -I . -I ./vendor 