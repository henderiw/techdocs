install telepresence local

```s
brew install datawire/blackbird/telepresence
```

telepresence helm install
telepresence connect -n network-system
telepresence intercept config-apiserver

```
(base) henderiw@MacBook-Pro apiserver-runtime-example % ~/Downloads/telepresence-darwin-arm64 intercept config-apiserver
Using Deployment config-apiserver
   Intercept name    : config-apiserver
   State             : ACTIVE
   Workload kind     : Deployment
   Destination       : 127.0.0.1:8080
   Volume Mount Error: sshfs is not installed on your local machine
   Intercepting      : all TCP connections
```

install deployment as is

vscode

decrypt secret
-> base64 tls.key; tls.crt used in vscode

yq '.data."tls.key"' artifacts/secret.yaml  | base64 -d  > ./debug/tls.key
yq '.data."tls.crt"' artifacts/secret.yaml  | base64 -d  > ./debug/tls.crt

-> copy kubeconfig local and modify the token we generate in the next step

kubectl create token -n network-system config-apiserver
-> create token

add output to the kubeconfig

example

kubectl create token -n network-system config-apiserver
```
eyJhbGciOiJSUzI1NiIsImtpZCI6IldrUzZJU0NwaDFHSWFYZTFHcmgwV3Z4dmZqSDVvdkxaRGx6MVdPOWRTXzQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzAxNzAzMzA5LCJpYXQiOjE3MDE2OTk3MDksImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJuZXR3b3JrLXN5c3RlbSIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJjb25maWctYXBpc2VydmVyIiwidWlkIjoiMWM4NjJiYmMtMzNiNy00YjZkLWE0MDItNjk0NDhjNGEyOGYwIn19LCJuYmYiOjE3MDE2OTk3MDksInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpuZXR3b3JrLXN5c3RlbTpjb25maWctYXBpc2VydmVyIn0.TQVH0HFgeUEKEQDdLNS6EVUP6isGJLUAVPSCSxm8dMFeypiWIHEs4296UHs2gTmARgIcJz9N1P1185KVomsmX_sDwB5yrRoIiEO5fLrGXAZd6DxpqBKeXLoE9MErOifgPF_-F99YvFELIiKhG_YSZcztCtR17Pxj23Vv3iUiUFMPY9owgIJPS_qHVuQzvpU9bQcAcLTDUQdaeiP-_BAnHJLq1JJ76nUDog9lcSIVTNPJ0TUxoFlx5XRLzxHp25UwtvttJh12-UYKgP9rleIxNeN2Ub1OSwJY5HqiooWJFFx7aBVpLXhy3znLh1jeDrsI5_VhJGBBHtsY2Zmc0-7i5w

```

add to kubeconfig


```yaml
- name: kind-mgmt
  user:
    token: eyJhbGciOiJSUzI1NiIsImtpZCI6IldrUzZJU0NwaDFHSWFYZTFHcmgwV3Z4dmZqSDVvdkxaRGx6MVdPOWRTXzQifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzAxNzAzMzA5LCJpYXQiOjE3MDE2OTk3MDksImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJuZXR3b3JrLXN5c3RlbSIsInNlcnZpY2VhY2NvdW50Ijp7Im5hbWUiOiJjb25maWctYXBpc2VydmVyIiwidWlkIjoiMWM4NjJiYmMtMzNiNy00YjZkLWE0MDItNjk0NDhjNGEyOGYwIn19LCJuYmYiOjE3MDE2OTk3MDksInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpuZXR3b3JrLXN5c3RlbTpjb25maWctYXBpc2VydmVyIn0.TQVH0HFgeUEKEQDdLNS6EVUP6isGJLUAVPSCSxm8dMFeypiWIHEs4296UHs2gTmARgIcJz9N1P1185KVomsmX_sDwB5yrRoIiEO5fLrGXAZd6DxpqBKeXLoE9MErOifgPF_-F99YvFELIiKhG_YSZcztCtR17Pxj23Vv3iUiUFMPY9owgIJPS_qHVuQzvpU9bQcAcLTDUQdaeiP-_BAnHJLq1JJ76nUDog9lcSIVTNPJ0TUxoFlx5XRLzxHp25UwtvttJh12-UYKgP9rleIxNeN2Ub1OSwJY5HqiooWJFFx7aBVpLXhy3znLh1jeDrsI5_VhJGBBHtsY2Zmc0-7i5w%    
```
vscode launch.json

```json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "debug",
            "program": "${workspaceFolder}/apiserver-runtime-example/cmd/apiserver/main.go",
            "cwd": "${workspaceFolder}",
            "args": [
                "--tls-cert-file=./apiserver-runtime-example/debug/tls.crt",
                "--tls-private-key-file=./apiserver-runtime-example/debug/tls.key",
                "--feature-gates=APIPriorityAndFairness=false",
                "--audit-log-path=-",
                "--audit-log-maxage=0",
                "--audit-log-maxbackup=0",
                "--secure-port=6443",
                "--kubeconfig=./apiserver-runtime-example/debug/kubeconfig",
                "--authorization-kubeconfig=./apiserver-runtime-example/debug/kubeconfig",
                "--authentication-kubeconfig=./apiserver-runtime-example/debug/kubeconfig",
            ],
            "console": "integratedTerminal",
        }
    ]
}
```