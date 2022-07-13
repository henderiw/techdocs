# webassembly

webassembly javascript object act as a namespace for all WASm functionality

methods:

- WebAssembly.instantiate()
- WebAssembly.instantiateStreaming()
- WebAssembly.compile() : create a modul from binary code but leaves the instantiaation for later
- WebAssembly.compileStreaming()

classes:

- WebAssembly.Memory
- WebAssembly.Table
- WebAssembly.Global
- WebAssembly.Module

## Memory

contiguous range of untyoed bytes
-> lineair memory
-> cannot be broken

- Page: 64KB, offset 0
- Min, Max
- Can grow up till max -> can be replaced if the machine
- Operators: load (read), store (write)
- Values: i32, f32, i64, f64
- lineair memory is in JS seen as a byteArray

Exzmple:

[udm-memory](https://github.com/henderiw/udm-memory)

## Table

- resizable types array of references, similar to memory
- contains references iso raw bytes -> reason is safety
- at the moment one element type: function references
- methods:
  - Table.prototype.set(): write
  - Table.prototype.get(): read
  - Table.prototype.grow(): expand

Example:

[udm-table](https://github.com/henderiw/udm-table)

## Global

- accessible from JS and WASM
- can be imported/exported to multiple WASM instances
- Allow dynamic linking of multiple modules

Example:

[udm-global](https://github.com/henderiw/udm-global)