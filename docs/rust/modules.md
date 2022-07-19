# modules

grouping
refered in the documentation

```
// only available in main
use std::collections::HashMap;

mod greet {
    fn hello()

    fn goodbeye()
}

mod match {
    fn add(...)

    fn sub(...)
}

fn main() {
    // hello is in scope of greet
    use greet::*;
    hello();
}

fn main() {
    // hello is in scope of greet
    greet::hello();
}
```

## seperate files

modules in seperates files is easier to follow

Cargo.toml

```
[lib]
name = "demo"
path = "src/lib.rs"

[dependencies]
```

src/lib.rs

```
mod helper;

// pub is an access modifier -> public
pub fn print_from_lib() {
    user helper{print_from_helper, print_from_helper_again}

    println!("hello from lib);
    print_from_helper();
    print_from_helper_again();
}
```

src/helper.rs

```
// pub is an access modifier -> public
pub fn print_from_helper() {
    println!("hello from helper);
}

pub fn print_from_helper_again() {
    println!("hello from helper aagin");
}
```

src/bin/demo.rs

```
// name in the Cargo.toml file we specified in the lib
use demo::print_from_lib;

fn main() {
    print_from_lib();
}
```

// group of modules
src/group/mod.rs

```
pub mod g1;
```

src/group/g1.rs
```
pub fn g1_hello()
```
