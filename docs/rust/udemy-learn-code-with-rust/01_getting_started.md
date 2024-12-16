# overview

Compiler: translates source code (human) into an executable program (computer)
Syntax: combination of characters/symbols

```shell
xcode-select --install
```

```shell
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

rustup -> ~/.rustup
cargo -> ~/.cargo

compiler

```shell
rustc --version
```

vscode-extension
- rust-analyzer
- winter is coming
- material icon theme

## rustup

upgrade rust // every 6 weeks there is an update
uninstall rust

```shell
rustup update
rustup self uninstall
rustup doc
```

## create a rust project

create a binary crate

```shell
cargo new hello_world
```

rust project is also called package or crate

2 types of crates:
- binary crate : runs standalone
- library crate : to be imported

src: where src code
target: final executable

## code

```rust
fn main() {
    p
}
```

## compiling

```shell
cd src
rustc main.rs
```

## formatting/styling

```shell
rustfmt main.rs
cargo fmt
```

## build

debug mode: is fast and optimized build/compilation -> beneficial for dev (not optimized, but has info to help debugging)
release mode: smaller, optimized for speed

```shell
cargo build # also build all the dependencies
cargo build --release
cargo b
cargo clean
```

run either debug or release

```shell
./target/debug/hello_world
./target/release/hello_world
```

## run

```shell
cargo run
cargo run --quiet
cargo r
cargo r --quiet
cargo run --package hello_world --bin hello_world
```

## check

```shell
cargo check
```

