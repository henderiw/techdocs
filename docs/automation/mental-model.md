# automation mental model

## datastore (desired state) -> what we call SOT/SSOT

- device related: 
    examples:
    - node (ip)
    - interfaces/subinterfaces 
    - protocols
    - system info
- network related:
    examples:
    - design: protocol, etc
    - links: (ip, role)
    - services: 

TBD: we could explain the difference between files, xls, a true datastore, apis, schemas, etc
-> ideal you have version control and collaboration to track changes and provide a history
of who did what/when.

## datatore (actual state)

- actual -> config/state, flows, logs
- options: in memory, datastore with retentiaion, time series

TBD: we could explain the difference between files, xls, a true datastore, apis, etc etc
Some people go direct to the device and avoid this layer

We could explain normalization, ETL, data aggregation, etc

## secret store

- secure place to hold secrets/rotate certs/etc

## providers (interacts with network devices)

- aaa (tacacs/radius)
- discoverer: 
    - apis:
        - secret store: credentials
        - inventory: prefixes
- ztp:
    - dhcp, dns, ntp
    - apis:
        - secret store: credentials, certificates
        - inventory: ip, serial numbers
- config: cli, http, netconf, gnmi, etc 
- state: cli scraping, snmp, gnmi, netconf, etc
- logs: syslog
- flow: netflow/ipfix/sflow
- ops: gNOI, gNSI
- bmp, bgpls, etc etc

Some of these would be the producer of the actual state with the option to use an ETL pipeline before writing data

## automation agents/applications

implementing these automation agents/application can be done using scripts, workflows, event driven frameworks or combinations of these with pro/cons of the various systems. We could go to pro/cons of these if needed.

agents/business logic interact with desired state/actual state and potentially the providers to achieve a goal/outcome. In an API based work they have.assigned permission to do certain things and could have guardrails

Can interact with ITSM and chat/IM systems, etc as well as part of a bigger solution since networking is typically a service to other parts of the business.

Example automation agents/applications

### actuator
- goal:
    - take a change and apply it to the network
    - policy: based on the change (device per device, canary, transaction, etc)
    - pre/post checks (intercats with the desired/actual datastore)
    - rollback if fails

### upgrade agent (maybe a special actuaator)
- goal: upgrade a system in canary
    - pre/post checks
    - rollback if needed

### drift detector
- goal: check change of the actual config versus desrired config

### predictor
- goal: predict outages

### config generator
- takes the desired state and build device specific configuration

### link monitor
- look at links flaps and removes a link if redundancy is available

### bgp prefixe observer agent
- looks at certain bgp prefixes and visualize their state

### ztp
- you could look at ZTP as an agent as well btw.