# k8s-api

## introduction

There are multiple ways to provider the k8s api specification

| Options         | go/kubuibuilder  |  ygot               | proto        | cue        |
|:----------------|:-----------------|:--------------------|:-------------|:-----------|
| Methods         | manual           | ygot                | protoc       | cue?       |
| Constraints     | kubebuilder tags | ygot                | cue-val tags | cue?       |
| OpenAPI tags    | kubebuilder tags | kubebuilder         | cue-gen      | cue-gen    |
| OpenAPI         | controller-gen   | controller-gen/blob | cue-gen      | cue-gen    |
| API validation  | native           | webhook             | native       | native     |
| Challenges      | go code          | small eco-systen    | import       | new        |

## protobuf

Good:
- uniform language for grpcs
Bad:
- import/package/dependency strategy -> use go mod vendor for remote dependencies, but local
  - import k8s proto is ok in local proto
  - import local proto that imports remote proto is nok since the local imports or local to the repo
- no constraints in proto

## cue

Good:
- nice data modeling
- can be used as a replacement for TNG
Bad:
- no go code generation 
- cue-gen is specific to istio