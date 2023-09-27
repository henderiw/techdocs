# this file explains the details of the slog implementation

## logger 

## handler interface

```go
type Handler interface {
    Enabled(context.Context, Level) bool
    Handle(context.Context, Record) error
    WithAttrs(attrs []Attr) Handler
    WithGroup(name string) Handler
}
```

Handler options

```go
type HandlerOptions struct {
    AddSource bool
    Level Leveler
    ReplaceAttr func(groups []string, a Attr) Attr
}

```

## record struct

```go
type Record struct {
    Time time.Time
    Message string
    Level Level
    // program counter
    PC uintptr 
    // Allocation optimization
    front [nAttrsInline]Attr
    // the number of attributed in front
    nFront int
    back []Attr
}
```

```go
type Attr struct {
	Key   string
	Value Value
}
```

built-in attributes:
- time
- level
- msg
- source
- key/values