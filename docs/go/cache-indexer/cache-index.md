# cache with indexers

per cache we also calculate the indices to retrieve an object
-> e.g. we hold in the index the value of the result of the query and this leads to the key

e.g. labels
foo = bar -> obj1 -> key1 (namespace1/name1)
foo = bar -> obj2 -> key2 (namespace2/name2)
foo = biz -> obj3 -> key3 (namespace3/name3)

indexName = `labelIndexed`
index - map[labelIndexed]sets(map[string]struct{}{`key1`, `key2`})
with getKeysFromIndex(indexName, obj) -> `key1`, `key1`

## FAQ 

1. How do the various indexNames be used/consumed?


## concepts

e.g. labels
foo = bar -> obj1 -> key1 (namespace1/name1)
foo = bar -> obj2 -> key2 (namespace2/name2)
foo = biz -> obj3 -> key3 (namespace3/name3)

Indexer -> interface to Store + additional methods
    - Parameters:
        - keyFunc -> used to determine the key of the object to store in the cache
        - indexers -> map[string]indexFunc -> provide additional ways/keys that can be used later to access the object stored in the cache

Indexers -> map[string]IndexFunc
    - map name to an IndexFunc

Index map[string]sets[string]
    - map the indexed value to a set of keys in the store
    example:
    - map[bar] -> sets namespace1/name1, namespace2/name2
    - map[biz] -> sets namespace3/name3

indices map[string]Index

indexName -> unique name for the index
indexValue -> values
indexFunc -> func(obj interface{}) ([]string, error)

For every update of an object we update the related index

## Thread safe map

