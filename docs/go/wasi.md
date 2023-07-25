# wasi support is enabled since go.21

[wasi issue for golang](https://github.com/golang/go/issues/58141)

## compilation example

```bash
go install golang.org/dl/gotip@latest 
gotip download
GOARCH=wasm GOOS=wasip1 gotip build -o main.wasm main.go
wazero run main.wasm
hello world!
```