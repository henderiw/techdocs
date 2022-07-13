# WASM WAT format

## WAT (Webassembly text format)

textual representation of the binary format

fundamental unit of code is a module; 
Module is a big s-expression (symbolic expression)
- representing trees
- used in lisp
    - each node in the tree describe the following
    - (node-type (child-node) attributes)
    - 1st label: node-type
    - other labels describe either child-nodes or attributes
        - child nodes have parenthesis
        - attributes dont have parenthesis
    - e.g. (module (memory 1) (func))
    - root-node: module
    - 2 children:
        - memory
        - func

Functions:
- (func <signatutre> <locals> <body>)
- signature: parameters and return values -> currently one
- locals: local variables
- body: instructions

Signature:
- e.g. (func (param i32) (param i32) (result f64) ...)
  - 4 types: i32, i64, f32, f64
  - if no result: vaoid function
Local variables e.g. (local i32)
  - local.get, local.set <index>
  - if parameters are present the index starts behind the amount of parameters defined
  - e.g. naming with $ to avoid the indexing
  - (func (param $p1 i32) (param $p2 i32) (local $loc f64) ...)
  - local.get $p1

stack machines:
- Every instruction pushes or pops a number of values on the stack
- (func (param $p i32) ...) -> empty stack
- result type -> stacj will return a single value of the stack
- local.get $p -> push value on the stack
- local.get $p -> pushes another value on the stack
- i32.add -> pops 2 values from the stack and pushes the result

body:
- list of instructions

```
(module
    (func $add (param $num1 i32) (paraam $num2 i32) (result i32)
        local.get $num1
        local.get $num2
        i32.add)
    (export "add" (func $add)))
```

## toolkit

[wabt toolkit](https://github.com/WebAssembly/wabt)

```
git clone --recursive https://github.com/WebAssembly/wabt
cd wabt
git submodule update --init
```

```
mkdir build
cd build
cmake ..
cmake --build .
```

## calling functions

call function within function

```
(module
    (func $return3 (result i32)
        i32.const 3)
    (func (export "multiplyBy2") (result i32)
        call $return3
        i32.const 2
        i32.mul
    )
)
```

call function from javascript using import
-> uses double namespace

```
(module
    (import "console" "log" (func $log (param i32)))
    (func (export "print)
        i32.const 13
        call $log
    )
)
```

js side

```
let importObject = {
    console: {
        log: function(arg) {
            console.log(arg);
        }
    }
}

WebAssembly.instantiateStreaming(fetch('logger.wasm), importObject)
    .then(result => {
        result.instance.exports.print();
    })
```

## globals

```
(global $g (import "js" "global) (mut i32))
```

to use the global we can use

```
global.get $g
global.set $g
```

javascript

```
const global = new WebAssembly.Global({value: "i32, mutable: true}, 0);
```

## strings

No string type in WASM
How to print a string?
- create a memory instance in WASM and pass to JS
- import a print function in WASM
- write a string to memory
- give offset and length to function
- call exported function in JS


[wasm string example](https://github.com/henderiw/udm-string)

## tables

Why we need them?
- array of references of functions
- call takes a static value, but we want a runtime parameter
- call_indirect -> takes a runtime value
  - uses tables which are more secure

[wasm runtime table example](https://github.com/henderiw/udm-table-runtime)
[wasm shared table example](https://github.com/henderiw/udm-table-shared)