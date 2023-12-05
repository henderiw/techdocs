## kpt package operations

go to yndd

mkdir blueprint
cd blueprint

mkdir core
kpt pkg init core

add info in the kptfile, like below

```
apiVersion: kpt.dev/v1
kind: Kptfile
metadata:
  name: core
  annotations:
    config.kubernetes.io/local-config: "true"
info:
  description: NDD core app.
  site: ndd.yndd.io
  emails:
    - ndd@yndd.io
  license: Apache-2.0
  keywords:
    - ndd
    - yndd
```

add the kubernetes resource to the package

```
kpt pkg tree
```

add pipeline mutators/validaters

```
apiVersion: kpt.dev/v1
kind: Kptfile
metadata:
  name: core
  annotations:
    config.kubernetes.io/local-config: "true"
info:
  description: NDD core app.
  site: ndd.yndd.io
  emails:
    - ndd@yndd.io
  license: Apache-2.0
  keywords:
    - ndd
    - hans
pipeline:
  mutators:
    #- image: gcr.io/kpt-fn/search-replace:v0.2.0
    #  configMap:
    #    by-value: yndd
    #    put-value: ${REGISTER}
    - image: docker.io/henderiw/set-image-with-configmap:0.0.1
      configMap:
        name: transform-image-core
    - image: docker.io/henderiw/set-image-with-configmap:0.0.1
      configMap:
        name: transform-image-rbac
```

## publish the package

```
git add .
git commit -m "initial package
git push origin
git tag v0.0.1
git push origin v0.0.1
```