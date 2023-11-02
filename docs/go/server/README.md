# readme server

allows to start a server w/o exposing it to the user

serve.go:
- entry point
- provides a wrapper to the user to start a server

plugin.go:
- implementation of the signatures of the go-plugin using a provider server implementation

provider_server.go:
- implementation of kfprotov1.ProviderServer -> server capable of handling kform protocol requests and issuing responses
- proxies it to the actual provider implementation