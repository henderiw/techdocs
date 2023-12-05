# k8s core dns plugin

based on caddy

step1: parse config and setup your internal information

```golang
setup.go

init() // register the plugin that parses the config file
setup(c *caddy.Controller) error // parses the config, add handler
```

step2: serve dns

```golang
ServeDNS(context.Context, dns.ResponseWriter, *dns.Msg) (int, error)
```

- process DNS req and returns a response, or, passes it down the chain

Managed by ZONE

-> services
- Services
- Records
- Reverse
- Serial
- IsNameError
- Lookup

## implementation

ServeDNS -> (handler.go) has various plugin calls based on the QueryType
    -> kubernetes struct implements the interface the plugin requires
Services -> (kubernetes.go) is being called by the plugin
