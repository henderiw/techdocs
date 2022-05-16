# consul api information

## consul servers

- responsible for maintaining state information about
    - service/node registration
    - service/node health

- servers:
    - leader: 
        - acts as the ultimate authority on consul's state
        - responsible for recording the change in state and distributing to the followers
            -> results in stale = slightly outdated information
    - followers

## what is consistency

[consistency modes](https://www.consul.io/api-docs/features/consistency)

- a response from the leader is guaranteed to be fully consistent
- folowers can also respond but the info maybe less consistent -> based on stale/outdated information

The consistency mode controls which consul server can respond to a read request
-> enables control between consistenct and performance

The consistency mode can be controlled per HTTP API endpoint
- stale: 
    - default mode for consult dns queries
    - any server can handle read requests
    - 50 msec delay with the leader
    - when no quorum, read requests can still be handled  
- default:
    - default mode for HTTP API queries
    - during leader election, stale responses can be returned
- consistent:
    - a leader verifies within a quorum of the peers that it is still the leader
    - an additional round trip is handled, to guarantee consistency

## api interaction

### blocking queries

used to wait for potential change using long polling
-> returns an index which represnts the current state of the requesting resource
-> can be set by the client to indicate that the client wishes to wait for any changes subsequent to that index
    - the http request will hang until a change in the system occurs or the max timeout (wait timeout) is reached

implementation details:
- reset the index if it goes backwards
- index returned should always be greater than 0

```
client --> query (client index=0, waittime)   ---> server
client <-- response with server index       <--- server
client --> query (client index, waittime)   ---> server
                                          wait time expiry
client <-- response with server index       <--- server

if server index == client index -> info is up to date
if server index >= client index -> new info is available
if server index <= client index -> error
if server index == 0            -> error
```

### streaming backend

publish change events to a topic, like gnmic subscription

introduced in consul 1.10

### hash-based blocking queries

supported by a limited number of endpoints
A response contains a hash iso index

## filtering

filtering-expression -> matching operator with a selection and a value

```
<Selector> == "<Value"
<Selector> != "<Value"

<Selector> is empty
<Selector> is not empty

...
```

## agent caching

### simple

may return a result from the cache without a roundtrip to the server

parameters can be used to control the cache time: 
- max-age
- stale-if-error

### backend refresh

