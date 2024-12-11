//go:generate go run github.com/bytecodealliance/wasm-tools-go/cmd/wit-bindgen-go generate --world fetch --out gen ./wit





go generate
tinygo build --target-wasip2 --wit-package ./wit --wit-world password-checker