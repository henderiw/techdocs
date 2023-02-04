# architecture

## schema server

- List
- Get
- Create
- Reload
- Upload: stream -> Create + Upload hash per file + hash
- ToPath: read the data tree and get the actual path

single RLock -> no write possible, read many which is ok

## data server

- datastore
  - schema
  - target (backend)
    - gnmi
    - netconf
    - redis
    - pub/sub

- Get datastore
- Create Datastore (main, candidate)
- Get Data -> gnmi get
- Set Data -> gnmi set (does only syntax validation, no true validation)
- Diff
- Subscribe
- Commit
  - we have the baseline + prepared candidate -> used to do the diff
  - when going to the device we will execute a diff

we store interface/ethernet-1.1/sub-interface/1/...


target differences
- srl and sros can be subscribed to for on-change config
  - operation we commit, we send to the target w/o writing to the running datastore + we wait for the on change notification to fillout the cache/datastore
- other devices: we need to do a regular sync, but we have to write to the cache/running datastore locally as we will not get a confirmation


## controller operation

- create candidate
- set (candidate)
- commit (candidate)
  - cache does a diff


## todo
- validation (leafref)
- xml
- json ietf
- 