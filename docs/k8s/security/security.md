## api access

APISERVER=https://kubernetes.default.svc
SERVICEACCOUNT=/var/run/secrets/kubernetes.io/serviceaccount
NAMESPACE=$(cat ${SERVICEACCOUNT}/namespace)
TOKEN=$(cat ${SERVICEACCOUNT}/token)
CACERT=${SERVICEACCOUNT}/ca.crt

curl --cacert ${CACERT} --header "Authorization: Bearer ${TOKEN}" -X GET ${APISERVER}/api/v1/secrets > /tmp/output

## how to provide security

- transparancy and documentation
- define the scope: clusterwide, external or namespace
- restrict RBAC permissions
  - clusterrole if asolutely necessary
  - limit CLoud IAM permissions for external operators

## preventive strategies

- restrict the namespace the is operator eployed
- restrict what namespace the operator can watch
- cluster-wide -> review clusterorle permissions
- external operators -< review permission>

No payload in the operator namespace
POD security admission features

-> Pod security policy