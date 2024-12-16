# trait

- a way to specify that some functionality exists
- used to standardize functionality accross multiple different types
  - standardization permits functions to operate on multiple different types
    - code deduplication
- traits define similar functionality for different types
- trait function are just regular functions
  - can accept arguments and return values
- use impl Trait as a function argument to pass data via trait
- trait should have caapital letter to distinguish from function

```rust
trait Noise {
    fn make_noise(&self);
}

// trait implementations
struct Person;
impl Noise for Person {
     fn make_noise(&self) {
         println!("hello")
     }
}

struct Dog;
impl Noise for Dog {
     fn make_noise(&self) {
         println!("woof")
     }
}

// how to use the functionality
// noisy -> something that implement Noise
fn hello(noisy: impl Noise) {
    noisy.make_noise();
}

fn main() {
    hello(Person {});
    hello(Dog {});
}
```

exercise a25

## default trait

to implement a default
if no arguments use default iso new

```
struct Package {
    weight: f64
}

impl Package {
    fn new(weight: f64) -> Self {
        Self { weigth}
    }
}

impl Default for Package {
    fn default() -> Self {
        Self { weight: 3.0 }
    }
}

fn main() {
    let p = Package::default();
}
```