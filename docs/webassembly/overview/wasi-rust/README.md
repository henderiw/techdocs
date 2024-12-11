

# compile to main
rustc main.rs


rustup target install wasm32-unknown-unknown
rustup target install wasm32-wasip1
rustup target add wasm32-wasip1

rustc --target wasm32-wasip1 main.rs

