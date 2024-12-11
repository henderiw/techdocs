# telemetry design

- subscriptions
    - protocol
        - path
            - interval
                - mode (SAMPLE, ONCHANGE)
                - encoding ()
                - outputs
                - sources
                - meta
                - subscription
                - description
                - adminState

- outputs
    - prometheus: cache
    - NATS
    - Kafka
    - file

- transformer (uses NATS) ->
    - device path
    - choreo path

- Another transformer