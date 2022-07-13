# emscripten

## goal

compiles c/c++ to asm.js/wasm

## uses

- LLVM (Low level virtual machine)
- CLang

C/C++ ---- emscripten ----> WASM module + Html + JS glue code

glue code:
- run webassembly
- helps to access webassembly to DOM/WEB API(s)

can be run in the browser or in node.js

## installation

### MAC

[install emscripten](https://emscripten.org/docs/getting_started/downloads.html)

- install xcode: appstore
- install git: brew
- install cmake: brew

## example

[example emscripten](https://github.com/henderiw/udm-emscrypten-random-array)

## advanced

[example emscripten module]()

using JS in C++
[example emscripten module]()

## files, threads, arguments

only posix threads
-> from thread_t[100] to pthread_t[100]

em++ -O3 *.cpp -o *.html --embed-file <input-file> 
    -s USE_PTHREADS=1
    -s MAXIMUM_MEMORY=128
    -s PTHREAD_MAX=100
    -s ASSERTIONS=1
    -s ALLOW_MEMORY_GROW=1


## debug

compile w-th -g3

-> levels g4 (allows c++ to be used in the debugger), g5

in chrome goto sources (in chrome seperated by functions)

we can also set breakpoints in chrome

compile with -v

turn on during compilation -> 

-s ASSERTIONS=1
-s SAFE_HEAP=1
-s 

## emrun

webserver

emrun <html file> -> opens in default browser
emrun 

[emrun informaation](https://emscripten.org/docs/compiling/Running-html-files-with-emrun.html)

## qt

[qt for wasm](https://doc.qt.io/qt-5/wasm.html)