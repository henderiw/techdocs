## wasmtime

curl localhost:8080 -d '{"id": 1}'

build on wasi:http
-> export wasi:http/incoming-handler@0.2.2;

implementation:
- see wasmcloud-component
-> convert wasm-cloud to http creates

## scaffold

wash dev

## build:

wasmcloud toolchain

```shell
wash build
```

cargo toolchain

```shell
cargo build --target wasm32-wasip2
```

## serve

wasmtime serve -Scommon ./build/http_hello_world_s.wasm