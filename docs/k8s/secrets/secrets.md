# secrets

[how to handle secrets with vault](https://medium.com/@lingxiankong/vault-integration-with-kubernetes-access-secrets-be2e59c171ba)

## kubernetes secrets

- base64 encoding
- secrets can be automatically injected into pods as env variables or mounted as files in a volume
- namespace scoped
- dynamic updates
- access control with RBAC
- encryption at Rest
- can be marked as immutable -> prevent accidental changes