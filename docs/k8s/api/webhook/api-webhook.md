# K8s api webhook

## cert manager

install cert-manager

```
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.7.1/cert-manager.yaml
```

## create and issuer

we are using a self-signed CA in this example

```
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: selfsigned-issuer
  namespace: ndd-system
spec:
  selfSigned: {}
```

```
kubectl get issuers -n ndd-system -o wide
```

## upgrade ndd-core

-> add the certifcate resource to the ndd-manager-role

it installs:
- service for the webhook
- certificate for the server to allow ssl/https
- deployment uses the certificate on the webhook server


## apply webhook config

```
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  annotations:
    cert-manager.io/inject-ca-from: ndd-system/nddp-srl3-8882f12f5a3e-webhook-serving-cert
  name: nddp-srl3-8882f12f5a3e-mutating-webhook-configuration
webhooks:
- admissionReviewVersions:
  - v1
  clientConfig:
    service:
      name: nddp-srl3-8882f12f5a3e-webhook-svc
      namespace: ndd-system
      path: /mutate-srl3-nddp-yndd-io-v1alpha1-srl3device
  failurePolicy: Fail
  name: srl3devices.srl3.nddp.yndd.io
  rules:
  - apiGroups:
    - srl3.nddp.yndd.io
    apiVersions:
    - v1alpha1
    operations:
    - CREATE
    - UPDATE
    resources:
    - srl3devices
  sideEffects: None
```

```
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  annotations:
    cert-manager.io/inject-ca-from: ndd-system/nddp-srl3-8882f12f5a3e-webhook-serving-cert
  name: nddp-srl3-8882f12f5a3e-validating-webhook-configuration
webhooks:
- admissionReviewVersions:
  - v1
  clientConfig:
    service:
      name: nddp-srl3-8882f12f5a3e-webhook-svc
      namespace: ndd-system
      path: /validate-srl3-nddp-yndd-io-v1alpha1-srl3device
  failurePolicy: Fail
  name: vsrl3device.srl3.nddp.yndd.io
  rules:
  - apiGroups:
    - srl3.nddp.yndd.io
    apiVersions:
    - v1alpha1
    operations:
    - CREATE
    - UPDATE
    resources:
    - "*"
  sideEffects: None
```