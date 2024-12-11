# wasm

## install wash

brew install wasmcloud/wasmcloud/wash


## choose your language


export WASMCON_LANG="go"

export WASMCON_LANG="rust"

# choose your app

fetch animal pictures

## part2 compose

wash app deploy ./wadm.yaml

wadm -> application manifest

// manifest 
-> wash dev --manifest-output-dir .

// use the manifest
wash dev --node-manifest wasm.yaml

wash app list
wash app delete <name of the app>


-> provider
-> component
    - 

// wasm go
-> compilar tinygo -> no garbage collector
-> wasm-tools -> temporary because we dont have brw install but apparently this is working now

-> go does language bindings (wasm-tools-go) binds to the world/interfaces we
-> change WIT to talk to my world (targeting a world) -> we target the fetcher world.


