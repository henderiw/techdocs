# consul practical info

## Health services:

we use grpc and ttl e.g. in k8s deployment

- if there are more than 1: 
  - service:$ID:$INDEX
  - $INDEX always starts from 1