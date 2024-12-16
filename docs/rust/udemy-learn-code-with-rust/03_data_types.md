# data types

[data types](https://doc.rust-lang.org/book/ch03-02-data-types.html#data-types)

- every rust value has a data type (what kind this thing is)
- rust is statically types language -> compiler infers the types and assigns memory

## scalar types

holds a single value
- integer: is a whole number
    - signed (positive and negative): start with i8 (-127, 127)
    - unsigned: 0 and positive: u8 (0, 255)
- floating-point: is a decimal number a fractional component
- numbers
- booleans
- characters

i8, u8 ... i128, u128

f32: 6-9 digits of precision
f64: 15-17 digits of precision

### integer

rust syntax:
- default type i32
- underscores can be used
- usize/isize: will depend on the architectire they run on


[integers](https://doc.rust-lang.org/book/ch03-02-data-types.html#integer-types)

```rust
fn main() {
    ley eight_bit: i8 = -112; // compiler infers i32, but we can explicitly define it using the syntax on the left

}
```

### string and raw string

- piece of text
- collector of chars in sequence
- string literal -> text is known at compile time
- special chars: \n, \t, 
- escape characters: \" -> show " in output
- raw string _> let filepath = r"C:\My Docuements\new\videos";
    - avoid to escape to much characters.

### method

rust:
- method: fn that lives on a value or type
    - value.method()
- argument: input to a method


```rust
fn main() {
    let value: i32 = -15;
    println!("{}", value.abs())

    let empty_space: &str = "    bla bla    ";
    println!("{}", empty_space.trim())

    println!("{}", value.pow(2))
}
```

### floating point

[float](https://doc.rust-lang.org/book/ch03-02-data-types.html#floating-point-types)


rust:
- no signed, unsigned options
- f32: 6-9 digits of precision
- f64: 15-17 digits of precision -> default in rust
- method would work if the type is made explicit

```rust
fn main() {    
    let pi: f64 = 3.14159;
    println!("{}", pi.floor()); // round down
    println!("{}", pi.ceil()); // round up
    println!("{}", pi.round()); // round to the closest
    println!("The current value of pi is {pi:.2}")
    println!("The current value of pi is {:.2}", pi)
}
```

format specifier customizes the viaual representation
- {pi:.2} -> displays 2 digits

## casting

convert a type from one to another
- use keyword as

```rust
fn main() {
    let miles_away: i32 = 50;
    let miles_away_i8 = miles_away as i8; // the value must fit in the casted type

    let miles_away = 100.329032;
    let miles_away_f32 = miles_away as f32;
    let miles_away_int = miles_away as i32; // we loose the decimal part
}
```

### numeric operations

[numeric operations](https://doc.rust-lang.org/book/ch03-02-data-types.html#numeric-operations)

rust:
- 5 + 4: operands (5, 4), + is the operator

```rust
fn main() {
    let add = 5 + 4;
    let sub = 10 -6;
    let mutiplication = 3 * 4;
    let div = 5 / 3; // this result in an integer
    let devi_f64 = 5.0 / 3.0;
    let modulo = 5 % 3 // 2

    // augmented assignment operator -> original value must be mutable
    let mut year = 2025;
    year = year + 1; // rust evaluates the right hans side of = first
    year += 1 // same as previous line

    year *= 2;
    year /= 4;
}
```

### boolean

[bool](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-boolean-type)

rust:
- model the idea of truth -> false or true
- use a full byte
- inverse: !

```rust
fn main() {
    let is_handsome: bool = true;
    let is_silly: bool = false;

    println!("handsome {is_handsome}, silly: {is_silly}")

    let age = 40;
    let is_young: bool = age < 35;
    println!("{} {}", age.is_positive(), age.is_negative())
}
```

### equality and inequality operator

rust:
- `==` equality operator
- `!=` inequality operator

```rust
fn main() {
    fmt.println!("{}", "Coke" == "Pepsi");
    fmt.println!("{}", 13 == 13.0 as i32);
}
```

### conditions

rust:
- `&&` and condition
- `||` or condition

```rust
fn main() {
    let purshased_ticket = true;
    let plane_on_time = true;
    let making_event = purshased_ticket && plane_on_time;
    fmt.println!("{}", making_event);
}
```

### character type

[char](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-character-type)

unicode is a computing standard for the representaiton of text for the world's writing systems.
-> emoji
-> UTF-8 
-> UTF-16 how much memory is allocated to a char
-> UTF-32

rust
- 4 bytes: 32bit -> goal is to support emoji, we have the capacity for these characters
- methods:

```rust
fn main() {
    let first_initial = 'a'
    let emoji = '🎧';

    println!("{} {}", emoji.is_alphabetic(), emoji.is_uppercase());
}
```

### array

[array type](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-array-type)
[array and slices](https://doc.rust-lang.org/rust-by-example/primitives/array.html)

- compound type
- an array is a fixed-size collection of homogenous data (data of the same type)
- in order 
- [type, length]

```rust
fn main() {
    let numbers: [i32; 6] = [4, 8, 15, 16, 23, 42];
    println!("length {}", apples.len())
}
```

[accessing arrays](https://doc.rust-lang.org/book/ch03-02-data-types.html#accessing-array-elements)

index position
- first: 0
- last len() -1

```rust
fn main() {
    let mut numbers: [i32; 6] = [4, 8, 15, 16, 23, 42];
    println!("index 0 {}, last {}", numbers[0], numbers[numbers.len()-1])
}
```
We cannot add or delete elements, we can replace elements
A vector allows to reduce and add elements

## traits

- contract: state obligation

- a trait:
    - like contract: a type must support a method
- the type implements the trait

### display trait

[display](https://doc.rust-lang.org/rust-by-example/hello/print/print_display.html)
[trait display](https://doc.rust-lang.org/std/fmt/trait.Display.html)


- display trait mandates a format method that returns a string
- {} interpolation relies on the format method
- array dont implement format trait

### debug trait

[debug](https://doc.rust-lang.org/rust-by-example/hello/print/print_debug.html)
[debug trai](https://doc.rust-lang.org/std/fmt/trait.Debug.html)

```rust
fn main() {
    let seasons = ["a", "b", "c", "d"];
    println!["{:?}", seasons]; // {:?} is invoking the debug trait
    println!["seasons{:?}"];
    println!["seasons{#?}"]; // this is pretty print -> using the debug trait
}
```

### dbg macro

[dbg macro](https://doc.rust-lang.org/std/macro.dbg.html)

```rust
fn main() {
    let seasons = ["a", "b", "c", "d"];
    println!["{:?}", seasons]; // {:?} is invoking the debug trait
    println!["seasons{:?}"];
    println!["seasons{#?}"]; // this is pretty print -> using the debug trait

    // debug macro
    // the content must implement the debug trait
    dbg!(2 + 2); // show line info, code, resulting value
}
```

### tuple type

[tuple type](https://doc.rust-lang.org/book/ch03-02-data-types.html#the-tuple-type)

- collection that can contain multiple elements
- support different types for its values
- e.g. employee -> name, age, department
- does not implement the display trait, but implements the debug trait

```rust
fn main() {
    let employee = ("Molly", 32, "Marketing");

    /*
    let name = employee.0;
    let age = employee.1;
    let dep = employee.2;
    */
    // shorter version of the above
    let (name, age, dep) = employee
}

```

### range type

- a range is a sequence/interval of consecutives values
- implemnts the debug trait but not the display trait

```rust
fn main() {
    let month_days = 1..31; // the upper value is excludes 1-30
    let month_days_inclusive = 1..=31; // includes 31

    println!("{month_days:?}")

    for number in month_days {
        println!("{number}")
    }

    let letters = 'b'..'f';
     for letter in letters {
        println!("{letter}")
    }
}
```

### generics

- a generic is a type argument (input to something), with the argument being a type
- generic uses types as arguments (a name for an expected type)
- analogy: box
    - container in which we can put
- a range is nested in a module -> not loaded up front
    - we need to get into the module to load them
    - std::ops

```rust
fn main() {
    let month_days: std::ops::Range<i8> = 1..31;
}
```