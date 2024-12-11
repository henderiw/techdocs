# exercises

[wasmcloud](https://github.com/ricochet/wasmcon-na-2024)

wash: bundles some tools

- static linking: components build
- runtime linking: 


```shell
brew install wasmcloud/wasmcloud/wash
```

```
wash new component --git ricochet/wasmcon-na-2024 --subfolder go/dog-fetcher
wash dev
```

## WADM application manifest

- provider
- component

```bash
wash dev --manifest-output-dir .
```

rename to wadm.yaml

wash dev --wadm-manifest wadm.yaml

wash app deploy wadm.yaml