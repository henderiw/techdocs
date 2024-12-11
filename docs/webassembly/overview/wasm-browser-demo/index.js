async function start() {
    console.log("Started!");
    const wasm = await WebAssembly.instantiateStreaming(
        fetch("./hello.wasm"),
        {
            "js": {
                "print": (x) => console.log(`This function was called by webassembly program woth argument ${x}`)
            }
            
        });
    wasm.instance.exports.f();
    console.log(wasm.instance.exports.hello(34, 35));
    console.log(wasm);
}

start().catch((e) => console.error(e));