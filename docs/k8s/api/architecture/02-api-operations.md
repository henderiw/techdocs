# api operations

```bash
kubectl proxy
CLUSTER=http://127.0.0.1:8001
```

## CREATE

```yaml
cat > pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
EOF
```

Namespace:
- yaml does not provide it -> apiserver takes the one from the path
- if yaml would provide it they need to match

Verb:
- X POST is ommitted since the --data-binary is providing the equivalent

```bash
curl $CLUSTER/api/v1/namespaces/default/pods -H "Content-Type: application/yaml" --data-binary @pod.yaml
```

## GET

```bash
curl -X GET $CLUSTER/api/v1/namespaces/default/pods
```

same as 

```
k get pods --namespace default nginx -o json
```

## LIST

cluster wide

```bash
curl $CLUSTER/api/v1/pods
```

namespace based

```bash
curl $CLUSTER/api/v1/namespaces/default/pods
```

## Filtering LabelSelector

```bash
k run nginx1 --image nginx --labels mylabel=foo
k run nginx2 --image nginx --labels mylabel=bar
```

```bash
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=mylabel"
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=\!mylabel"
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=mylabel==bar"
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=mylabel\!=bar"
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=mylabel+in+(foo,bar)"
curl "$CLUSTER/api/v1/namespaces/default/pods?labelSelector=mylabel+notin+(foo,bar)"
```

## Filtering FieldSelector

```bash
curl "$CLUSTER/api/v1/namespaces/default/pods?fieldSelector=status.phase==Running"
curl "$CLUSTER/api/v1/namespaces/default/pods?fieldSelector=status.phase\!=Running"
```

## DELETE

```bash
curl -X DELETE $CLUSTER/api/v1/namespaces/default/pods/nginx
```

## DELETE COLLECTION

```bash
curl -X DELETE $CLUSTER/api/v1/namespaces/default/pods
```

## UPDATE

```yaml
cat > deploy.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
EOF
```

```bash
curl $CLUSTER/apis/apps/v1/namespaces/default/deployments -H "Content-Type: application/yaml" --data-binary @deploy.yaml
``` 

```bash
cat deploy.yaml | sed 's/image: nginx/image: nginx:latest/' > deploy2.yaml
```

```bash
curl -X PUT $CLUSTER/apis/apps/v1/namespaces/default/deployments/nginx -H "Content-Type: application/yaml" --data-binary @deploy2.yaml
``` 

```bash
k replace -f deploy2.yaml
```

1. Replace operation

Managing conflicts when updating a resource:
- if someone updates the resource in between the get an replace the changes will be lost
- you can read the resourceVersion and add this in the PUT in which case the apiServer looks at the resourceVersion and if it changed an error will be returned by the apiServer.

2. Strategic Merge Patch (only the deltas are send)

PATCH request with Content-Type: application/strategic-merge-patch+json

```json
cat > deploy-patch.json << EOF
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine"
                    }
                ]
            }
        }
    }
}
EOF
```

```bash
curl -X PATCH $CLUSTER/apis/apps/v1/namespaces/default/deployments/nginx -H "Content-Type: application/strategic-merge-patch+json" --data-binary @deploy-patch.json
```

```bash
k patch deployment nginx --patch-file deploy-patch.json --type strategic
```


Patching array fields -> patching directive
- replace directive

```json
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine",
                        "securityContext": {
                            "$patch": "replace",
                            "runAsNonRoot": false
                        }
                    }
                ]
            }
        }
    }
}
```

```json
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine",
                        "env": [
                            {"$patch": "replace"},
                            {"name": "a", "value": "b"}
                        ]
                    }
                ]
            }
        }
    }
}
```
- delete directive

```json
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine",
                        "securityContext": {
                            "$patch": "delete"
                        }
                    }
                ]
            }
        }
    }
}
```

```json
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine",
                        "env": [
                            {"name": "a", "$patch": "delete"}
                        ]
                    }
                ]
            }
        }
    }
}
```

- deleteFromprimitiveList directive
only useful to deleting object from an array

```json
{
    "spec": {
        "template": {
            "spec": {
                "containers": [
                    {
                        "name": "nginx",
                        "image": "nginx:alpine",
                        "$deleteFromPrimitiveList/env": [
                            {"name": "a", "$patch": "delete"}
                        ]
                    }
                ]
            }
        }
    }
}
```

- setElementOrder directive
used to reorder elements in a list

3. Server side apply

Avoids the conflicts we discussed earlier -> in case of conflicts you need to write specific directives for the server to understand how to resolve them
-> requires a field-manager field
-> allows to create a resource with an update if the resource does not exist
-> How: `contentType: application/apply-patch+yaml`
-> Server uses .metadata.ManagedFields -> lists the apply operations performed on the resource
-> conflicts can be identified by different fieldManager setting the field to a different value
-> force poassible to override

```bash
curl -X PATCH $CLUSTER/apis/apps/v1/namespaces/default/deployments/nginx?fieldManager=manager1 -H "Content-Type: application/apply-patch+yaml" --data-binary @deploy.yaml
```

```bash
curl -X PATCH $CLUSTER/apis/apps/v1/namespaces/default/deployments/nginx?fieldManager=manager2&force=true -H "Content-Type: application/apply-patch+yaml" --data-binary @deploy.yaml
```

## WATCH

```bash
curl -X GET "$CLUSTER/api/v1/namespaces/default/pods?watch=true"
```

-> filtering can be done using labelSelectors and fieldSelectors
-> bookmarks can be used for watching resources

## FORMAT

Table

```bash
curl -X GET "$CLUSTER/api/v1/pods" -H "Accept: application/json;as=Table;g=meta.k8s.io;v=v1"
```

YAML

```bash
curl -X GET "$CLUSTER/api/v1/pods" -H "Accept: application/yaml"
```

PROTOBUF

also contentType is possible

```bash
curl -X GET "$CLUSTER/api/v1/pods" -H "Accept: application/vnd.kubernetes.protobuf" --output wim
```

