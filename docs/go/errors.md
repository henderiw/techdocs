# introduction

an error have to implement the Error() interface

```golang
type error interface {
    Error() string
}
```

## error wrapping

provide more context to an error

```golang
type WrappedError interface {
    Unwrap() error
}
```

example:

```golang
type wrapError struct {
    msg string
    err error
}

func (e *wrapError) Error() string {
    return e.msg
}

func (e *wrapError) Unwrap() error {
    return e.err
}
```

## errors.Is

```golang
var RecordNotFoundErr = errors.New("not found")
const name, id = "lzap", 13

werr := fmt.Errorf("unknown user %q (id %d): %w", name, id, recordNotFoundErr)

fmt.Println(werr.Error())
```

errors are essentially a list of strings
Before go1.20 we could only have 1 %w in fmt.Errorf

```golang
if errors.Is(err, RecordNotFoundErr) {
    // ...
}
```

## errors.As

```golang
var nerr *net.Error
if errors.As(err, &nerr) {
    // ... (use nerr which is a *net.Error)
}
```

## go 1.20

```golang
err1 := errors.New("err1")
err2 := errors.New("err2")

err := errors.Join(err1, err2)

fmt.Println(err)
```

theoretcial interface for go 1.20 which does not exist

```golang
type MultiWrappedError interface {
    Unwrap() []error
}
```



```golang
type joinError struct {
    errs []error
}

func (e *joinError) Error() string {
    // concatenate errors with a new line character
}

func (e *joinError) Unwrap() []error {
    return e.errs
}
```

summary:
- New Unwrap []error function contract allowing traversing through tree of errors.
- New errors.Join function which is a handy function to join two error string values (with a newline).
- Existing functions errors.Is and errors.As updated to work both on list and tree of errors.
- Existing function fmt.Errorf now accepts multiple %w format verbs.

