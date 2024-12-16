# variables

[variable](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html#storing-values-with-variables)

variable info:
- use lower snake case
- _apples before the variable removes the warning
- case sensitive
- by default variables are immutable

```rust
fn main() {
    let apples = 50;
    let oranges = 14 + 6;
    let fruits = apples + oranges;
    println!("fruits: {}", fruits); // {} is a spot where we can dynamic content -> interpolate; for each curly brace we need a argument
    println!("fruits: {fruits}: apples {apples} + oranges {oranges}"); // alternative syntax
    println!(
        "fruits: {1}: apples {2} + oranges {0}",
        fruits, apples, oranges
    );// allows to avoid repeating arguments
}
```

[interpolation](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html#printing-values-with-println-placeholders)

[immutable/mutable](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#variables-and-mutability)
[variable binding](https://doc.rust-lang.org/rust-by-example/variable_bindings/mut.html)

we can change the value but the type cannot change

```rust
fn main() {
     let _immutable_binding = 1;
    let mut mutable_binding = 1;

    println!("Before mutation: {}", mutable_binding);

    // Ok
    mutable_binding += 1;

    println!("After mutation: {}", mutable_binding);

    // Error! Cannot assign a new value to an immutable variable
    _immutable_binding += 1;
}
```

Error Codes

```shell
rustc --explain E0384 # documentation in the command line
```

[error code index](https://doc.rust-lang.org/error_codes/error-index.html)

## Variable shadowing

[variable shadowing](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#shadowing)

the 2nd declaration becomes the active value
-> we want to do multiple transformation on the same object

## scopes

[scopes](https://doc.rust-lang.org/rust-by-example/variable_bindings/scope.html)

{} -> represents a block or scope or boundary or region
scope is the boundary or region where this variable is valid is the body of the main function

inner block can access outerblock variables
outer block CANNOT access inner block variables -> the block concluded

## constant

[constant](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html#constants)
[constant example](https://doc.rust-lang.org/rust-by-example/custom_types/constants.html)

can never change -> permenantly immutab;e

```rust
const TAX_RATE: i32 = 100;

fn main() {

}
```

differences:
- variables are limited to a function scope, const are file scoped
    - variables: scope ends
- const value must be known at compile time, variable value is known at runtime
- explicit type need to be assigned

# type aliases

alias or nic name for an existing type
-> provide additional context what that type represents

rust syntax
- Start with capital letter

[type alias](https://doc.rust-lang.org/rust-by-example/types/alias.html)

```rust
type Meters = i32; // assigning a type

fn main() {
    let mile_race_length: Meters = 1600;
    let two_mile_race_length: Meters = 3200;
}
```

## compiler directives

Annotation that tells the compiler how to parse the source code

rust syntax
- compiler directive 
- #![allow(unused_variables)] => allows to the complete file

```rust
type Meters = i32;
#[allow(unused_variables)]
fn main() {
    
    let mile_race_length: Meters = 1600;
    let two_mile_race_length: Meters = 3200;
}
```

