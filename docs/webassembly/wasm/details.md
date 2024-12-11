# wasm

## runtimes

- wasmtime
- wasmcloud

## sdk

## wasm module

-> provider implementation
-> upon CRD change invoke the wasm module

## WIT

```rust
package provider

world Provider {
  // Initialize the provider with a configuration
  init: func(config: string) -> result<_, string>  // Takes json and returns success or string (error)
  
  // Handle an event and return a result
  handle-event: func(event: string) -> result<string, string> // Takes a kson string and returns a success string or error string
  
  // Clean up resources
  cleanup: func() -> result<_, string> // return success or a string
}
```

generate WIT bindings for host

```rust
cargo install wit-bindgen-cli
wit-bindgen rust-wasm provider.wit
```

rust module

```rust
use serde::{Deserialize, Serialize};
use provider::*;

#[derive(Serialize, Deserialize)]
struct Config {
    api_key: String,
    endpoint: String,
}

#[derive(Serialize, Deserialize)]
struct Event {
    action: String,
    payload: String,
}

struct MyProvider;

impl Provider for MyProvider {
    fn init(config: String) -> Result<(), String> {
        let config: Config = serde_json::from_str(&config).map_err(|e| e.to_string())?;
        println!("Initialized with API Key: {}", config.api_key);
        Ok(())
    }

    fn handle_event(event: String) -> Result<String, String> {
        let event: Event = serde_json::from_str(&event).map_err(|e| e.to_string())?;
        println!("Handling event: {:?}", event);
        let response = serde_json::json!({
            "status": "success",
            "message": "Event processed"
        });
        Ok(response.to_string())
    }

    fn cleanup() -> Result<(), String> {
        println!("Cleaning up resources");
        Ok(())
    }
}
```

```shell
cargo build --target wasm32-unknown-unknown --release
```

Host integration

```rust
use provider::*;

fn main() {
    // Load the WASM module
    let module_path = "path/to/wasm/module.wasm";
    let instance = Provider::load(module_path).expect("Failed to load WASM module");

    // Initialize the provider
    instance.init(r#"{"api_key": "my-key", "endpoint": "https://api.example.com"}"#)
        .expect("Failed to initialize");

    // Handle an event
    let result = instance.handle_event(r#"{"action": "create", "payload": "test"}"#)
        .expect("Failed to handle event");
    println!("Event result: {}", result);

    // Cleanup
    instance.cleanup().expect("Failed to cleanup");
}
```

Other languages

```
rust: wit-bindgen rust-wasm
js: wit-bindgen js
go wit-bindgen go
python: wit-bindgen py

```

