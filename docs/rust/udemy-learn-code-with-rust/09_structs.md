# structs

[struct](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#defining-and-instantiating-structs)

struct:
- container for related pieces of data
- tuples: elements are stored in order
    - no context
    - order might not be that important
- 3 kind of structs
    - name field structs
        - each field has a corresponding name
    - tuple-like structs
    - unit-like structs
- style:
    - struct type: use PascalCase
    - fields: is_hot use snakecase
- instance: realized value
    - missing fields will create an error

```rust
fn main() {
    struct Coffee {
        price: f64,
        name: String,
        is_hot: bool, 
    }

    let mocha = Coffee {
        price: 3.99,
        name: String::from("mocha"),
        is_hot: true,
    };

    println!("My {} this morning cost {}", mocha.name), mocha.price;

    // moves ownership since String does not implement the copy trait
    let favorite_cofee = mocha.name

    // this is will create an error in the compiler
    println!("{}", mocha.name)
}
```

ownership:
- variable -> owns the instance (cleans the struct)
- struct -> owns the field, cleans the field
- a field -> owns the data, cleans the data

## change data of a struct

- the template has no notion of mutability
- the complete struct is either mutable or not mutable

```rust
fn main() {

    struct Coffee {
        price: f64,
        name: String,
        is_hot: bool, 
    }

    let mut beverage = Coffee {
        name: String::from("Mocha"),
        price: 3.99,
        is_hot: true,
    };

    // ownership moves
    beverage.name = String::from("Caramel Macchiato")
    beverage.price = 6.99
    beverage.is_hot = false

    println!("My {} this morning cost {}", beverage.name), beverage.price;

   
}
```

## struct with function

```rust
struct Coffee {
    price: f64,
    name: String,
    is_hot: bool, 
}

fn main() {
    let name = String::from("Latte")
    let coffee = make_coffee(name, 4.99, true);
    println!("My {} this mornign cost {}", coffee.name, coffee.price)
}

// ownership of name moves to param
fn make_coffee(name: String, price f64, is_hot bool) -> Coffee {
    Coffee {
        name: name, // ownership moves from param to name field
        price: price,
        is_hot: is_hot,
    }
}
```

## shortcut

[shortcut](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-the-field-init-shorthand)

```rust
struct Coffee {
    price: f64,
    name: String,
    is_hot: bool, 
}

fn main() {
    let name = String::from("Latte");

    let coffee = make_coffee(name, 4.99, true);
    println!("My {} this mornign cost {}", coffee.name, coffee.price)

    let name = String::from("Latte");
    let price = 5.99;
    let is_hot = false;
    let latte = Coffee {
        name,
        price,
        is_hot,
    }
}

// ownership of name moves to param
fn make_coffee(name: String, price f64, is_hot bool) -> Coffee {
    Coffee {
        name, // shortcut, ownership moves from param to name field
        price,
        is_hot,
    }
}
```

## struct update syntax

[struct update](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#creating-instances-from-other-instances-with-struct-update-syntax)

```rust
struct Coffee {
    price: f64,
    name: String,
    is_hot: bool, 
}

fn main() {
    let name = String::from("Latte");

    let coffee = make_coffee(name, 4.99, true);
    println!("My {} this mornign cost {}", coffee.name, coffee.price)

    let caramel_machiatto = Coffee {
        name: String::from("Machiato");
        // all fields seen before the below statement, are not copied over
        // name and is_hot are copied -> this is ok but we need to take care of ownership, same types might not be ok
        ..coffee
    }

    // this moves ownership from coffee to new_cofee
    // we can no longer access coffee.name since owneship moved to new_coffee
    let new_coffee = Coffee {
        ..coffee
    }

    // this will not move ownerhsip
    let new_coffee = Coffee {
        name: mocha.name.clone(), // this is a copy
        ..coffee
    }
}

// ownership of name moves to param
fn make_coffee(name: String, price f64, is_hot bool) -> Coffee {
    Coffee {
        name, // shortcut, ownership moves from param to name field
        price,
        is_hot,
    }
}
```

## pass struct into a function

// option 3 and 4 are the most common usages


```rust
struct Coffee {
    price: f64,
    name: String,
    is_hot: bool, 
}

fn main() {
    let name = String::from("Latte");

    // option 1,2,3
    let coffee = make_coffee(name, 4.99, true);
    // option 4
    let mut coffee = make_coffee(name, 4.99, true);
    // option 1 and 2
    // we cannot use coffee after the fn instantiation since ownership moved
    drink_coffee(coffee)
    // option 3
    // we can continue to use coffee after this
    drink_coffee(&coffee)
    // option 4
    // we can continue to use coffee after this
    //
    drink_coffee(&mut coffee)
   

}

// ownership of name moves to param
fn make_coffee(name: String, price f64, is_hot bool) -> Coffee {
    Coffee {
        name, // shortcut, ownership moves from param to name field
        price,
        is_hot,
    }
}

// option1: define a parm that receives a struct as immutable param
// ownership moves to the coffee parameter
// we cannot change any field
// coffee is removed from the memory after the fn
fn drink_coffee(coffee: Coffee) {
     println!("My {} this mornign cost {}", coffee.name, coffee.price)
     // No update possible
     // coffee is removed from the memory
}

// option2: define a parm that receives a struct as mutable param
// ownership moves to the coffee parameter
// we can change any field
// coffee is removed from the memory after the fn
fn drink_coffee(mut coffee: Coffee) {
    println!("My {} this mornign cost {}", coffee.name, coffee.price)
    coffee.is_hot = true
    
}

// option3: define a parm that receives an immutable ref
// ownership DOES NOT move to the coffee parameter
// we cannot change any field
// coffee is NOT removed from the memory after the fn
fn drink_coffee(coffee: &Coffee) {
    // rust is automatically dereferecing (*coffee).name
    println!("My {} this mornign cost {}", coffee.name, coffee.price)
    // No update possible
}

// option4: define a parm that receives an mut ref
// ownership DOES NOT move to the coffee parameter
// we change any field
// coffee is NOT removed from the memory after the fn
fn drink_coffee(coffee: &mut Coffee) {
    // rust is automatically dereferecing (*coffee).name
    println!("My {} this mornign cost {}", coffee.name, coffee.price)
    // No update possible
    coffee.is_hot = true
}
```

## deriving debug trait for struct

a trait is a proomise on certain functionality
-> display trait
-> debug trait

An atrribute is a directive to the compiler. It is metadata on the line above a construct that customizes how the compiler parses the code.

[derive](https://doc.rust-lang.org/book/ch05-02-example-structs.html#adding-useful-functionality-with-derived-traits)
[]
[debug](https://doc.rust-lang.org/rust-by-example/hello/print/print_debug.html)


```rust
// derive -> atribute is a trait
#[derive(Debug)]
struct Coffee {
    price: f64,
    name: String,
    is_hot: bool, 
}

fn main() {
    let name = String::from("Latte");

    // option 1,2,3
    let coffee = make_coffee(name, 4.99, true);

    println!("{:?}", coffee)
    println!("{:#?}", coffee)
}

// ownership of name moves to param
fn make_coffee(name: String, price f64, is_hot bool) -> Coffee {
    Coffee {
        name, // shortcut, ownership moves from param to name field
        price,
        is_hot,
    }
}
```

## methods on struct

[methods](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#defining-methods)

value.method(arguments)
- fields: data
- method: behavior

```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}

// Option 1. Immutable struct value (self parameter takes ownership)
// Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
// Option 1/2 does not allow to use more than 1 method due to the ownership movement
// Option 3. Immutable reference (no ownership move)
// Option 4. Mutable reference (no ownership move), mutable permission

// method are sperated in the 
// impl definition
impl TaylorSwiftSong {
    // self can vary based on its implementation

    // Option 1. Immutable struct value (self parameter takes ownership)
    
    // Option 3. Immutable reference (no ownership move)
    // Option 4. Mutable reference (no ownership move), mutable permission
    fn display_song_info(self) {    
        println!("Title {}", self.title);
        println!("Release Year {}", self.release_year);
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(mut self) {    
        self.duration_secs *= 2
        println!("Duration {:?}", self);
    }
}

fn main() {
    let song = TaylorSwiftSong {
        title: String::from("Blank space"),
        release_year: 2024,
        duration_secs: 231
    }

    // option1 -> ownership moved, after this song is no longer available
    song.display_song_info();

    // option2 -> ownership moved, after this song is no longer available
    // remark previous statement need to be removed
    song.double_length()
}
```

Option 3/4

```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}


// Option 3. Immutable reference (no ownership move)
// Option 4. Mutable reference (no ownership move), mutable permission

// method are sperated in the 
// impl definition
impl TaylorSwiftSong {
    // self can vary based on its implementation
    fn display_song_info(&self) {    
        println!("Title {}", self.title);
        println!("Release Year {}", self.release_year);
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(&mut self) {    
        self.duration_secs *= 2
    }
}

fn main() {
    let mut song = TaylorSwiftSong {
        title: String::from("Blank space"),
        release_year: 2024,
        duration_secs: 231
    }

    // rust will use a reference behind the scenes (&song)
    // this operion does not move ownership, so we can continue
    // to use song after a method invokation
    song.display_song_info();
    // rust will use a reference behind the scenes (&song)
    song.double_length()

    song.display_song_info();
}
```

## method parameters

[multiple parameters](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#methods-with-more-parameters)


```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}

// method are separated in the 
// impl definition
impl TaylorSwiftSong {
    // self can vary based on its implementation
    fn display_song_info(&self) {    
        println!("Title {}", self.title);
        println!("Release Year {}", self.release_year);
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(&mut self) {    
        self.duration_secs *= 2
    }

    fn is_longer_than(&self, other: &TaylorSwiftSong) -> bool {
        self.duration_secs > other.duration_secs
    }
}

fn main() {
    let blank_space = TaylorSwiftSong {
        title: String::from("Blank space"),
        release_year: 2024,
        duration_secs: 231,
    }

    let all_to_Well = TaylorSwiftSong {
        title: String::from("All to well"),
        release_year: 2012,
        duration_secs: 327,
    }

    if blank_space.is_longer_than(&all_to_Well) {
        println!("{} is longer than {}", blank_space.title,  all_to_Well.title)
    } else {
        println!("{} is shorter than or equal to {}", blank_space.title,  all_to_Well.title)
    }
}
```

## callign ethods from methods

```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}

// method are separated in the 
// impl definition
impl TaylorSwiftSong {
    // self can vary based on its implementation
    fn display_song_info(&self) {    
        println!("Title {}", self.title);
        println!("Years since release {}", self.years_since_release());
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(&mut self) {    
        self.duration_secs *= 2
    }

    fn is_longer_than(&self, other: &TaylorSwiftSong) -> bool {
        self.duration_secs > other.duration_secs
    }

    fn years_since_release(&self) -> u32 {
        2024 - self.release_year
    }
}

fn main() {
    let blank_space = TaylorSwiftSong {
        title: String::from("Blank space"),
        release_year: 2024,
        duration_secs: 231,
    }

    let all_to_Well = TaylorSwiftSong {
        title: String::from("All to well"),
        release_year: 2012,
        duration_secs: 327,
    }

    if blank_space.is_longer_than(&all_to_Well) {
        println!("{} is longer than {}", blank_space.title,  all_to_Well.title)
    } else {
        println!("{} is shorter than or equal to {}", blank_space.title,  all_to_Well.title)
    }

    blank_space.display_song_info();
}
```

## asscociated functions

[asscociated functions](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#associated-functions)

[associated fn & blocks](https://doc.rust-lang.org/rust-by-example/fn/methods.html)

asscociated functions 
- are fn that are attached to a type
    - they are attached to the type
    - not attached to implementation, but attached to a type
- namespace: like a file in a folder
- used for constructor -> fn constructs a new value of that type


```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}

// method are separated in the 
// impl definition
impl TaylorSwiftSong {
    // no self -> mean associated function
    // constructor fn
    fn new(title: string, release_year: u32, duration_secs: u32) -> Self {
        Self {
            title,
            release_year,
            duration_secs,
        }
    }
    // self can vary based on its implementation
    fn display_song_info(&self) {    
        println!("Title {}", self.title);
        println!("Years since release {}", self.years_since_release());
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(&mut self) {    
        self.duration_secs *= 2
    }

    fn is_longer_than(&self, other: &TaylorSwiftSong) -> bool {
        self.duration_secs > other.duration_secs
    }

    fn years_since_release(&self) -> u32 {
        2024 - self.release_year
    }
}

fn main() {
    ley blank_space = TaylorSwiftSong::new(
        String::from("Blank space"),
        2024,
        231,
    )
}
```

## multiple implementation Blocks

[multiple implementation blocks](https://doc.rust-lang.org/book/ch05-03-method-syntax.html#multiple-impl-blocks)

```rust
#[derive(Debug)]
struct TaylorSwiftSong {
    title: String,
    release_year u32,
    duration_secs u32,
}

impl TaylorSwiftSong {
    // no self -> mean associated function
    // constructor fn
    fn new(title: string, release_year: u32, duration_secs: u32) -> Self {
        Self {
            title,
            release_year,
            duration_secs,
        }
    }
}

impl TaylorSwiftSong {
    // self can vary based on its implementation
    fn display_song_info(&self) {    
        println!("Title {}", self.title);
        println!("Years since release {}", self.years_since_release());
        println!("Duration {}", self.duration_secs);
    }

    // Option 2. Mutable struct value (self parameter takes ownership),  mutate permission
    fn double_length(&mut self) {    
        self.duration_secs *= 2
    }

    fn is_longer_than(&self, other: &TaylorSwiftSong) -> bool {
        self.duration_secs > other.duration_secs
    }

    fn years_since_release(&self) -> u32 {
        2024 - self.release_year
    }
}

fn main() {
    ley blank_space = TaylorSwiftSong::new(
        String::from("Blank space"),
        2024,
        231,
    )
}
```

## Builder pattern

a design pattern is a recommended way to write or structure code to solve a specific problem

- we retain the reference 

```rust
#[derive(Debug)]
struct Computor {
    cpu: String;
    memory: u32;
    hard_drive_capacity: u32;
}

impl Computer {
    fn new(cpu: string, memory: u32, hard_drive_capacity: u32) -> Self {
        Self{
            cpu,
            memory,
            hard_drive_capacity,
        }
    }

    fn upgrade_cpu(&mut self, new_cpu: String) -> &mut Self {
        self.cpu = new_cpu;
        self
    }
     fn upgrade_memory(&mut self, new_memory: String) -> &mut Self {
        self.memory = new_memory;
        self
    }
     fn upgrade_hard_drive_capacity(&mut self, new_capacity: String) -> &mut Self {
        self.hard_drive_capacity = new_capacity;
        self
    }
}

fn main() {
    let mut computer = Computer::new(String::from("M3 max"), 54, 3)
    computer.
        .upgrade_cpu(String::from("M3 max"))
        .upgrade_memory(128)
        .upgrade_hard_drive_capacity(4T);

    println!("Stats: {computer:#?}");
}   
```

## Tuple struct

[tuple like structs](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#using-tuple-structs-without-named-fields-to-create-different-types)


A tuple struct is a struct that assigns each piece of data an order in line rather than a name

why not a tuple?
- Name of the struct serves as an identifier -> the compiler can differentiate the tuple struct iso a generic tuple

```rust
// uses patenthesis
// Hourse, minutes
struct ShortDuration (u32, u32);

// Years, months
struct LondDuration (u32, u32);


fn main() {
    let work_shift = ShortDuration(8, 0)
    println!("{} hours {} minutes", work_shift.0, work_shift.1)

    let era = LongDuration(5, 3)
    println!("{} years {} months", era.0, era.1)

    //let work_shift = (8, 0)
    //let era = (5, 3)

    go_to_work(work_shift)
    go_to_work(era) // will be catched by the compiler
}

fn go_to_work(length: ShortDuration) {
    println!("{} hours {} minutes", length.0, length.1)
}

```

## Tuple struct

[unit like struct](https://doc.rust-lang.org/book/ch05-01-defining-structs.html#unit-like-structs-without-any-fields)

A unit is an empty tuple, a tuple w/o values

```rust

struct Empty;

fn main() {
    let my_empty_struct = Empty;
}
```

[struct examples](https://doc.rust-lang.org/rust-by-example/custom_types/structs.html#structures)

