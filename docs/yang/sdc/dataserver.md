## SetIntent flow

- create cache client + schemaClientBound (with specific schema)
- populate
    - retrieve index (intended only)
    - convert setIntent to sdcpb paths
    - caclulate paths (old (from index based on owner), new (from setIntent))
    - populate paths from cache (delete flag if owner == setIntent)
    - populate paths from setIntent
    - close insertion (marker we are done)
- calculate
    - calculate update/delete for device and cache
        - device (based on highest priority)
        - cache (based on owner)
    - Set Candidate in cache
- Validation
    - validate must statements (grab schame + uses candidate)
    - validate leafref (grab schame + uses candidate)
    - validate mandatory is disabled (since we dont read from running)


## Tree

- pkg/tree
- RootEntry -> / for both SROS/SRL
- EntryImp -> anything else
- sharedEntryAttributes
    - child
    - leafVariant ( leaf/leaflist)
    - key: no schema