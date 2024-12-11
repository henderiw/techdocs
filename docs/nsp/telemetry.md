# Telemetry

## layers:

- network
- collection layer
    - accounting (file based) - 150 Million -> need to deal with catch up if network was disconnected
    - gnmi (1500 records/sec)
    - snmp ongoing (poll)
- mapping layer
- normalization layer
- output/storage layer (kafka/vertica/etc)
- analytics/optimization layer

## telemetry focus
- collection layer
- mapping layer
- normalization layer

## capabilities

polish/enrich
baseline analytics
inicator -> trend
threshold actions -> workflow/action
visualization/plotting
reports

## cloud native scaling

- HBA
- KEDA: custom metrics

deployments

- provider: target/subscription
    - telemtry:/base/interfaces/interface/received-octets
- device model mapper
    - nokia-state:/state/port/ethernet/statistics/in-octest
- collector
    - maintains gnmi
- NSP model mapper (reverse mapping)
    - updates are converted to vendor agnostic model
- output processor
    - vertica/kafka/file.NATS

2 CRD:
- DeviceHelper: encoding, maxsubscription
- Transformer: provides the mapping
    - per device type
    - spec:
        nsp-path: telemetry:/base/interfaces/interface/received-octet
        device-path: nokia-state:/state/port/ethernet/statistics/in-octest
        attibutes:
        - nsp-attribute: received-broadcast-packets
          device-attribute: in-broadcast-packets
        - nsp-attribute: received-multicast-packets
          device-attribute: in-multicast-packets

components:
- DC UI (data collector)
- telemtry core
- telemetry provider (new/old)
- request processor (translates vendor agnostic, to vendor specific subscriptions) + assigns a collector/target => COORDINATOR
- input processor (gnmic, SNMP, file)
- NATS (3 pods) (messaging buss)
    - no Jetstream, core NATs
    - things can get out of order
    - store previous value + current value ->
- Workers (transformers) -> do the reverse mapping
- Output processors -> kafka, postgres, vertica ->  gnmic future