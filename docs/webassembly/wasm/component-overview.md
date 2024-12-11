# component overview

[component model](https://component-model.bytecodealliance.org/introduction.html)

[WASI](https://github.com/WebAssembly/WASI)

## WASM module

- .wasm file
    - functions
    - memory
    - imports
    - exports
- run in browser, seperate runtime (wasmtime or WAMR)
- [webassembly core specification](https://webassembly.github.io/spec/core/)
    - core works with integer and floats -> richer types such as strings, lists, records, etc

## Interwork between WASM modules

A WASM component is a wrapper around a module that specifies its import and exports.
- WIT (WASM interface type) translates into bits and bytes -> translation is called Canonical ABI (application Binary interface)

## Components

- logically, components are containers for modules or other components (which expresses thier interfaces and WIT)
- unit of code that interacts ony through interfaces iso shared memory
- physically: a component is a specifically formatted webassembly file
- external interface of a component (import/export) corresponds to a worls

## Interfaces

- described using WIT

## Worlds

- higher level contracts that describes a components capabilities and needs

example
- HTTP proxy
    - export: a handle HTTP request
    - import: send HTTP requests

## WIT



## commands:

wasm-tools component wit build/dog-fetcher.wasm

wasmtime serve -$common ./build/dog-fecther_s.wasm