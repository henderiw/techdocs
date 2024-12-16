# functions

[function](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#functions)
[fn example](https://doc.rust-lang.org/rust-by-example/fn.html)

- a function is a sequence of steps to be executed in order
- a fn signature
- reusable
- functions have a scope
- convention snake case

```rust
fn main() {
    open_store();
}

fn open_store() {
    println!("Opening my pizza server store");
}
```

## Parameters and Arguments

[parameters](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#parameters)

- parameter is the name of the expected input to a function
- argument is the value

```rust
fn main() {
    open_store("Brooklyn");
    open_store("Queens");
}

fn open_store(neighborhood: &str) {
    println!("Opening my pizza server store in {neighborhood}");
}
```

## return values

```rust
fn main() {
    let result = square(5);
    println!("the square of 5 is {result}")
}

fn square(number: i32) -> i32 {
    return number * number; // it ends the function
}

fn square(number: i32) -> i32 {
    return number * number // it ends the function
}
```

[result](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#functions-with-return-values)

rust implicity returns the last value, so we can remove the return keyword + the semicolumn needs to be removed.
-> returns evaluation of the last executed line

## unit type

A unit is an empty tuple that holds no values
default return value of a function i

```rust
fn main() {
    let result = mystery(); // this returns a unit (empty tuple)
}

fn mystery() {}
```

## scopes

```rust
// main function scope
fn main() {
    let multiplier = 3;

    // this is an isolated scope - nested scope
    let calculation = {
        // when the block ends the variables become unaccessible
        let value = 5 + 4;
        value * multiplier // this becomes the output
    };

    println!("{calulation}")
}
```