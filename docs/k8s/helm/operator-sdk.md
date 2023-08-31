# operator sdk

```bash
operator-sdk init \
      --plugins=helm.sdk.operatorframework.io/v1 \
      --domain=example.com \
      --group=demo \
      --version=v1alpha1 \
      --kind=Nginx
```

```bash
operator-sdk init \
      --plugins=helm.sdk.operatorframework.io/v1 \
      --domain=example.com \
      --helm-chart=helm-charts
```