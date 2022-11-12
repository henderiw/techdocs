#

[informers blog 1](https://aly.arriqaaq.com/kubernetes-informers/)
[informers blog 2](https://medium.com/codex/explore-client-go-informer-patterns-4415bb5f1fbd)

client-go implementation:
- reflector: inputs data into the locaal Delta FIFO queue -> after calling list/watch
- informer: reads data -> adds to Indexer and distributes data to a specific eventhandler according to the data type (ADD, DELETE, UPDATE)
- indexer: maintains a map to cache data

client-go calls access the cache maintained by the indexer

=> event driven design to improve APIServer performance
=> OBSERVER PATTERN

## Indexer

key value cache -> geneous piece of code

## How to use the informer

