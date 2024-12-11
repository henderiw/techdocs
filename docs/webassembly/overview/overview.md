# webassmbly

Webassembly
- binary instruction format for a stack based VM
- fast
- scalable
- secure


WASM: Web assembky -> binary format
WAT: Web Assembly text -> human readable format (what people called webassembly)
- [wat](https://developer.mozilla.org/en-US/docs/WebAssembly/Understanding_the_text_format)
- uses s-expressions

wat2wasm hello.wat

```wat
(module
 (func (export "hello") (param i32) (param i32) (result i32)
    local.get 0
    local.get 1
    i32.add))
```

Running WASM in a browser
- HTML -> JS -> WASM -> exports

browser will also use import functions

```wat
(module
    (func $print (import "js" "print") (param i32))
    (func (export "hello") (param i32) (param i32)
        local.get 0
        local.get 1
        i32.add
        call $print
    )
)
```

## WASI

[wasi announcement](https://hacks.mozilla.org/2019/03/standardizing-wasi-a-webassembly-system-interface/)
[wasi](https://wasi.dev)

Browser example:
- kernel <-> browser <-> JS glue code <-> WASM module
- JS glue code: emscrypten -> emulates a particular OS system interface (POSIX) on the web
    - emscrypten created its own implementation of libc
        - a part compiled into the WASM module
        - a part implemented in the JS glue code
    - Issue: was propriatery and not optimized

Goal:
- interface for a conceptual OS (any OS)
- run WASM outside the browser - need a was to talk to the system (system interface)
- portable (POSIX gives portable source code), but WASM need to go 1 step further portable binaries
- secure (OS provide access control based on group/ownership - a program has access to all file of the user who runs it)


WASI -> is POSIX for webassembly
WASI is about standardizing the import capabilities

Implementation:
- wasi-core -> similar as POSIX (files, network connection, clocks, random numbers)
- RUST open(...) -> calls __wasi_path_open when compiled to webassembly
- C/C++ openat(...) -> [wasi-libc](https://github.com/WebAssembly/wasi-libc)

The runtime passes wasi-core functions as imports 
- provides portability (each host can have their own implementation of wasi-core)
- provides sandboxing (host allows which sys calls to allow on a program by program basis)

## WIT (Webassembly interface types)

- Wabassembly just uses numbers -> API(s) JSON, etc are much harder to implement
    - [webassembly javascript interface](https://www.w3.org/TR/wasm-js-api/#intro) -> details how to translate between JS and Webassembly
    - [reference types](https://github.com/WebAssembly/reference-types/blob/master/proposals/reference-types/Overview.md#language-extensions)

.wasm <-> WIT <-> OS

- exported functions
    - parameters: accepting from the caller (lowering)
    - return: to the caller (lifting)
- imported functions
    - parameters: accepting to the fn (lifting)
    - return: accepting from the fn (lowering)

- lifting: concrete type to interface type
- lowering: interface type to a conrete type

WIT-BINDGEN -> based on wasmtime (Alex Crichton)
- export: guest fn that can run by the host
- import: host fn that can be run by the guest (provide helpers)

Why?
- add functionality to a long running program (avoid downtime using this plugin framework)
- Fast thsn integrating LUA, JS script
- Multi-lanaguage support

Why no?
- too early
- not as performant
- Not yet any code to any code