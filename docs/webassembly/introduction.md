# Webassembly

## goals

- portable
- sandbox/security
- fast, efficient, speed

make the web more efficient for variaous use cases:

- 3D games
- AR/VR
- images & video processing/editing
- P2P
- Visualizations, simulation
- Encryption
- Webservers

## scope

- webassembly is a virtual instrtruction set architecure (vISA)
  - [webassembly spec](https://webassembly.github.io/spec/core/_download/WebAssembly.pdf)
    - instruction set
    - binary encoding
    - validation
    - execution semantics
    - texttual representation

## security

- functions to HW are performed via an embedder and imported in a webassembly module: WASI
- an embedder can establish security policies

## comparison to JS

| info   | JS            | WASM |
| :--:   | :--:          | :-:  |
| level  | high level    | low level |
| format | flexible      | binary    |
| type   | dynamic typed | static typed |
| perf   | variable      | near native  |
| compilation | interpreter | compilation |
| other | framework/libraries | various languages |         

## MVP

- module (distributable, loadable, executable unit code)
- stack based virtual machine
- binary format
- text format: .wat
- runtimes: web/browser, IOT, server, etc

## overview

### history

[asm.js](http://asmjs.org/spec/latest/)
[asm.js example](https://github.com/zbjornson/human-asmjs/blob/master/README.md)

### concepts

webassembly encodes a low-level assembly like programming language

- Values: 
  - 4 basic number types
    - integers and floating point in 32/64-bit
    - 32bit int serve as bool and memory address
    - 
- Instructions
- Traps: caught outside the webassembly env
- Functions
- Tables
- linear memory
- modules: webassembly binary
- embedder

## compiler websites

[wasm explorer](https://mbebenita.github.io/WasmExplorer/)
[wasdk](https://wasdk.github.io/WasmFiddle/)