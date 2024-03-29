# cel

[cel github](https://github.com/google/cel-go)
[cel codelabs](https://codelabs.developers.google.com/codelabs/cel-go/index.html#0)
[kubcon eu 2023](https://www.youtube.com/watch?v=KIL1BAq3J2g)
-> min 07:00

-> example: /Users/henderiw/code/tmp/cel-go/codelab

## highlevel

- create an env: defines the environment (defines variables and functions + other options)
- parse and check the expression
- evaluate the expression

## limitations

- no for/while/...
    - use comprehension "macros"
    -> all(), exists(), exists_one(), map(), filter()
- no if/else/...
    - use the ternary operator:
    -> <condition> ? <ifTrue> : <ifFalse>

## steps

- Configure the environment

```go
env, err := cel.NewEnv()
    if err != nil {
        glog.Exitf("env error: %v", err)
    }
```

- Parse and check the expression

```go
// Check that the expression compiles and returns a String.
    ast, iss := env.Parse(`"Hello, World!"`)
    // Report syntactic errors, if present.
    if iss.Err() != nil {
        glog.Exit(iss.Err())
    }
    // Type-check the expression for correctness.
    checked, iss := env.Check(ast)
    // Report semantic errors, if present.
    if iss.Err() != nil {
        glog.Exit(iss.Err())
    }
    // Check the output type is a string.
    if !reflect.DeepEqual(checked.OutputType(), cel.StringType) {
        glog.Exitf(
            "Got %v, wanted %v output type",
            checked.OutputType(), cel.StringType,
        )
    }
    
```

- Evaluate the expression

```go
    // Plan the program.
    program, err := env.Program(checked)
    if err != nil {
        glog.Exitf("program error: %v", err)
    }
    // Evaluate the program without any additional arguments.
    eval(program, cel.NoVars())
    fmt.Println()
```