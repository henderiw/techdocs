# crate

## introduction

// collection of code is a crate
// crate refers to all the code
use crate::*;

## external crates

use other programs 

- crates.io
- lib.rs

Cargo.toml
Cargo.lock -> keeps track of the used dependencies

```
[dependencies]
humantime = "2.0.1"
```

src file

```
use hmantime::format_duration;
use std::time::Duration;

fn main() {
    let d = Duration::from_secs(9876);
    println("{}", format_duration(d));
}
```

exercise a26