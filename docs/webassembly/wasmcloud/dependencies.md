# dependencies

wash build -> fetches all the WIT dependencies automatically

overrides -> wasmcloud.toml file (see overrides)

```tom
name = "http-task-manager
language = "rust"
type = "component"

[component]
wasm_target = "wasm32-wasip2"

[overrides]
"my:custom" = { path = "../wit" }
```

