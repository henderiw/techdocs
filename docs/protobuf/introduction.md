# protobuf

## protobuf with go modules

[protobuf with go modules](https://stepan.wtf/importing-protobuf-with-go-modules/)

go mod vendor

protoc $(find ./apis/ -name '*.proto') --gofast_out=. --gofast_opt=paths=source_relative -I . -I ./vendor 

proto file

'''
syntax = "proto3";

package common.v1;

import "k8s.io/apimachinery/pkg/apis/meta/v1/generated.proto";

option go_package = "github.com/yndd/ndd-runtime/apis/common/v1";

message Condition {
    ConditionKind kind = 1;
    ConditionStatus status = 2;
    k8s.io.apimachinery.pkg.apis.meta.v1.Time lastTransitionTime = 3;
    //optional github.com.kubernetes.apimachinery.pkg.apis.meta.v1.Time lastTransitionTime = 3;
    ConditionReason reason = 4;
    string message = 5;
}
'''