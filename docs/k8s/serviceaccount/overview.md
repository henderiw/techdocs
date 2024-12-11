# service account

- every namespace gets a default service account
- when a pod is associated with a service account -> a service account token is automatically mounted in the pod
    /var/run/secrets/kubernetes.io/serviceaccount
    -> JSON Web token (JWT) and includes
        - Namespace information
        - Service Account Name
        - Cluster API access permissions
- RBAC
    - service accounts get permissions using Role/ClusterRoles
- API access uses the mounted service account token for authentication

## Key features

- Bound to a namespace
- secret management
- automatic mounting: SA tokens and associated CA certs are automatically mounted in the pods unless explicitly disabled