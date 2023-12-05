# logic

## kubernetes plugin

- creates a cache with services, pods, endpoints
- a headless service does not allocate an IP in the service

## k8sipam plugin

this only manages /32 and /128 prefixes

- service -> prefixkind: loopback
- endpoint -> mapping of service ip to pod ip (this is a local cluster thing)
    - we model this with 2 tags
    - headless-service = name -> groups all headless services together
    - alias = name
- pod -> prefixkind: network


what does coredns do with the endpoints ??
- used for headless services to map the endpoints to the service

