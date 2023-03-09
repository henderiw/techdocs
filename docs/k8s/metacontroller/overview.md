# metacontroller

- create ns
- create CRD -> kubebuilder
- define composite controller (through a dedicated CRD) -> uses webhooks to initiate business logic
- define Webhook (business logic)
- deploy the webhook