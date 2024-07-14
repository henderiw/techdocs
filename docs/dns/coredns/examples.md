# examples

- consolidate data sources
- the response depends on the origin of the request

dev:
- coredns started as a plugin of caddy
- 


## build plugin

1. add kuid:kuid to plugin.cfg
2. 

```
docker run --rm -i -t \
-v $PWD:/go/src/github.com/coredns/coredns \
-w /go/src/github.com/coredns/coredns \
golang:1.22 sh -c 'GOFLAGS="-buildvcs=false" make gen && GOFLAGS="-buildvcs=false" make'
```

docker run --rm -v $(pwd):/go/src/github.com/coredns/coredns -w /go/src/github.com/coredns/coredns golang:1.22 make
