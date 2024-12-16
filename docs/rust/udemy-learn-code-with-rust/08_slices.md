# slices

[slice type](https://doc.rust-lang.org/book/ch04-03-slices.html#the-slice-type)

slice
- collection type: can hold many values (arrays, tuples and strings)
- alias to pizza
- a slice is a reference to a portion/sequence of a collection type (it is a subcategory of a reference)
- a string slice is a reference to a sequence of characters from a string
- an array slice is a reference to a sequence of elements from an array
- a reference, a slice does not take ownership of the collection

analogy:
- borrow a room in the house
- portion is a slice of the hole collection -> portion can also be the hole think

## string slice

can be done from str or String

```rust
fn main() {

    ley action_hero = String::from("Arnold Schwarzenegger")
    // we cnanot bprrow option
    let ref = &action_hero
    println("{ref}")

    let first_name: &str = &action_hero[0..6]; // not including 6 -> string slice
    println!("{first_name}")
    let last_name: = &action_hero[7..21];
    println!("{last_name}")
}
```

[string slices](https://doc.rust-lang.org/book/ch04-03-slices.html#string-slices)
[string literals](https://doc.rust-lang.org/book/ch04-03-slices.html#string-literals-as-slices)


```rust
fn main() {
    // The "Arnold Schwarzenegger" is in the binary
    // action_hero is a ref to the binary location
    ley action_hero: &str = "Arnold Schwarzenegger"

    let first_name: &str = &action_hero[0..6]; // not including 6 -> string slice
    println!("{first_name}")
    let last_name: = &action_hero[7..21];
    println!("{last_name}")
}
```

```rust
fn main() {    
    // is this not a dangling ref: because the "Arnold Schwarzenegger" string is in the binary -> the text refering to is in the binary file
    let first_name = {
        let action_hero: &str = "Arnold Schwarzenegger"
        action_hero[0..6]
    } 
}
```

## string slice lengths

[string slice](https://doc.rust-lang.org/book/ch08-02-strings.html#slicing-strings)

the lnegth of a string slice refers to a count of its bytes, not its characters
- 

```rust
fn main() { 
    // the ASCII chars are 1 byte
    let food = "pizza";
    println!("{}", food.len())
    let pizza_slice = &food[0..3];

    // this is 4 bytes
    let emoji = "🍕";
    println!("{}", food.len())
    let pizza_slice = &food[0..3]; // this is not a valid boundary
}
```

## shortcuts

string literal or heap allocation -> ref does not matter, it depends on where the data sit that we borrow with a string slice

```rust
fn main() { 
    // The "Arnold Schwarzenegger" is in the binary
    // action_hero is a ref to the binary location
    ley action_hero: &str = "Arnold Schwarzenegger"

    let first_name: &str = &action_hero[..6]; // not including 6, start from the beginning -> string slice
    println!("{first_name}")
    let last_name: = &action_hero[7..]; // this is to the end of the 
    println!("{last_name}")

     let full_name: &str = &action_hero[..]; // this is a ref to the full content
}
```

## string slice as parameters

[string slice as parameters](https://doc.rust-lang.org/book/ch04-03-slices.html#string-slices-as-parameters)

```rust
fn do_hero_stuff(hero: &str) {
    println!("{hero}")
}

fn main() { 
    // The "Arnold Schwarzenegger" is in the binary
    // action_hero is a ref to the binary location
    let action_hero1: String::from("Arnold Schwarzenegger")
    // &String -> &str is supported
    // &str -> &String is not supported
    do_hero_stuff(&action_hero1); // rust is smart enough to convert this as ref str
    let action_hero2: &str = "Sylvester Stallone"
    do_hero_stuff(&action_hero2);
}
```

## array slices

[other slices](https://doc.rust-lang.org/book/ch04-03-slices.html#other-slices)

array slice: ref to a portion of an array

```rust
fn main() {
    let values = [4, 8, 15, 16, 23, 42]
    let my_slice = &values[0..3];
}
```

## deref coercion array slices

```rust
fn main() {
    let values = [4, 8, 15, 16, 23, 42]
    let regular_ref: &[i32: 6] = &values; // this is a regular ref
    print_length(regular_ref);

    let slice_3: &[i32] = &values[..3]; // this is slice -> no length -> more flexible, but more versitile
    print_length(slice_3); 
}

// coercion
fn print_length(ref: &[i32]) {
    println!("{}", ref.len());
}
```

## mutable array slice

rust: 
- if we borrow a str slice we can only do this immutably -> no modification allows
- Allows mutable slices of an array  


```rust
fn main() {
    let mut array: [i32, 5] = [10, 15, 20, 25, 30]
    
    let my_slice_ro: &[i32] = &array[2..4]; // we can read but not modify
    let my_slice_rw: &mut [i32] = &mut array[2..4]; // we can read and write
    // mutable reference to a portion

    my_slice_rw[0] = 100; // we modify my_slice but we also mutate the original array
}
