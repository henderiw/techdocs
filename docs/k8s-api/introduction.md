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