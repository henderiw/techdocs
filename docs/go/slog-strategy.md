# slog strategy

## main program

1. create a logger with a daemon that is the wire-name
2. set the default logger to the new logger i created
3. add the logger in the context

```go
l := log.NewLogger(&log.HandlerOptions{Name: "wirer-daemon", AddSource: false})
slog.SetDefault(l)
l.Info("start daemon")

ctx := ctrl.SetupSignalHandler()
ctx = log.IntoContext(ctx, l)
```

## inherit the logger from context

create a new logger and set a new group

```go
func New(ctx context.Context, c Config, opts ...Option) *GrpcServer {
	c.setDefaults()
	s := &GrpcServer{
		l:      log.FromContext(ctx).WithGroup("grpcserver"),
	}

	for _, o := range opts {
		o(s)
	}

	return s
}

type GrpcServer struct {
	...
	// logger
	l *slog.Logger
    ...
}
```

## grpc service or equivalent

change the context and add extra attributes in the context that will be logged by the subsequent loggings

```go
ctx = log.IntoContext(ctx, r.l.With("nsn", req.NodeKey.String(), "server", req.ServerType))
```

## regular program

can use slog -> uses the logger set as default