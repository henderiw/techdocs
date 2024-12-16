# traits

trait:
- a distinguishing quality or characteristic
- a contract that describes functionality that a type should have 
- a definition declares the methods that a type implementaint that trait must have
    - method name
    - parameters with types
    - return value type
- example Display and Debug trait
    - requires a type to define methods for presenting itself as a string
- Clone trait:
    - requires a type to define a clone mthod for creating a duplicate of itself
- Implementation
    - we can implement it on structs and enums, the type honors the traits contract
    - multiple can implement the same trait
    - a type can implement multiple traits
- PascalCase

## defining a trait

[defining a trait](https://doc.rust-lang.org/book/ch10-02-traits.html#defining-a-trait)


```rust
trait Accomodation {
    // options:
        //&self
        //&mut self
        //self
        //mut self
    // &self and immutable reference
    fn get_description(&self)  -> String;
    // mutate the eventual type
    fn book(&mut self, name: &str, nights: u32) // returns a Unit by default (empty Tuple)
}

fn main() {

}
```

## implementing trait for Struct I

[implementing a trait](https://doc.rust-lang.org/book/ch10-02-traits.html#implementing-a-trait-on-a-type)

```rust
use std::collections::HashMap;

trait Accomodation {
    // options:
        //&self
        //&mut self
        //self
        //mut self
    // &self and immutable reference
    fn get_description(&self) -> String;
    // mutate the eventual type
    fn book(&mut self, name: &str, nights: u32) // returns a Unit by default (empty Tuple)
}

#[derive(Debug)]
struct Hotel {
    name: String,
    reservations: HashMap<String, u32>,
}

impl Hotel {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            reservations: HashMap::new(),
        }
    }
}

impl Accomodation for Hotel {
    fn get_description(&self) -> String {
        format!("{} is the pinacle of luxury", self.name)
    }
    fn book(&mut self, name: &str, nights: u32) {
        self.reservations.insert(name,.to_tring() nights);
    }
}

```

## implementing trait for Struct II

```rust
use std::collections::HashMap;

trait Accomodation {
    // options:
        //&self
        //&mut self
        //self
        //mut self
    // &self and immutable reference
    fn get_description(&self) -> String;
    // mutate the eventual type
    fn book(&mut self, name: &str, nights: u32) // returns a Unit by default (empty Tuple)
}

#[derive(Debug)]
struct Hotel {
    name: String,
    reservations: HashMap<String, u32>,
}

impl Hotel {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            reservations: HashMap::new(),
        }
    }
}

impl Accomodation for Hotel {
    fn get_description(&self) -> String {
        format!("{} is the pinacle of luxury", self.name)
    }
    fn book(&mut self, name: &str, nights: u32) {
        self.reservations.insert(name,.to_tring() nights);
    }
}

#[derive(Debug)]
struct AirBnB {
    host: String,
    guests: Vec<(String, u32)>,
}

impl AirBnB {
    fn new(host: &str) -> Self {
        Self {
            host: host.to_string(),
            guests: vec![],
        }
    }
}

impl Accomodation for AirBnB {
    fn get_description(&self) -> String {
        format!("Please enjoy {}'s apartment", self.host)
    }
    fn book(&mut self, name: &str, nights: u32) {
        self.guests.push((name.to_tring(), nights));
    }
}

fn main() {
    let mut hotel = Hotel::new("The luxe")
    println("{}", hotel.get_description())
    hotel.book("wim", 5)
    println("{#:?}", hotel)

    let mut airbnb = AirBNB::new("Pater")
    println("{:?}", airbnb.get_description())
    airbnb.book("wim", 5)
    println("{#:?}", airbnb)
}
```

## default implementation

[default implementation](https://doc.rust-lang.org/book/ch10-02-traits.html#default-implementations)


```rust
trait Accomodation {
    fn get_description(&self) -> String {
        String::from("A wonderful place to stay")
    }
    fn book(&mut self, name: &str, nights: u32) 
}
```

## calling trait method from another method

```rust
use std::collections::HashMap;

trait Accomodation {
    // options:
        //&self
        //&mut self
        //self
        //mut self
    // &self and immutable reference
    fn get_description(&self) -> String;
    // mutate the eventual type
    fn book(&mut self, name: &str, nights: u32) // returns a Unit by default (empty Tuple)
}

#[derive(Debug)]
struct Hotel {
    name: String,
    reservations: HashMap<String, u32>,
}

impl Hotel {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            reservations: HashMap::new(),
        }
    }
    fn summarize(&self) -. String {
        format!("{}: {}", self.name, self.get_description)
    }
}

impl Accomodation for Hotel {
    fn get_description(&self) -> String {
        format!("{} is the pinacle of luxury", self.name)
    }
    fn book(&mut self, name: &str, nights: u32) {
        self.reservations.insert(name,.to_tring() nights);
    }
}

fn main() {
    let mut hotel = Hotel::new("The luxe")
    println("{}", hotel.summarize())
    hotel.book("wim", 5)
    println("{#:?}", hotel)

}
```

## trait for fn parameters constraints

[trait as parameters](https://doc.rust-lang.org/book/ch10-02-traits.html#traits-as-parameters)

```rust
// entity can be any type as long as it implement the Accomodation trait
// entity is an immutable reference that implement the accomodation trait
fn book_for_one_night(entity: &mut impl Accomodation, guest: &str) {
    entity.book(guest, 1)
}

fn main() {
    let mut hotel = Hotel::new("The luxe")
    book_for_one_night(&mut hotel, "Piers")
    println!("{hotel:#?}")
    let mut airbnb = AirBNB::new("Pater")
    book_for_one_night(&mut airbnb, "Amanda")
    println!("{airbnb:#?}")
}
```

## trait bound syntax

[trait bound syntax](https://doc.rust-lang.org/book/ch10-02-traits.html#trait-bound-syntax)

- generics help solve the same problem

a trait bound requires that a generic type implement a specific trait

```rust
fn book_for_one_night<T:Accomodation>(entity: &mut impl T, guest: &str) {
    entity.book(guest, 1)
} 

// both 1st and 2nd has to be a Accomodation, but both need to be the same time
fn mix_an_match<T:Accomodation, U: Accomodation>(first: &mut T, second: &mut U, guest: &str) {
    first.book(guest, 1);
    second.book(guest, 1);
}

fn main() {
    let mut hotel = Hotel::new("The luxe")   
    let mut airbnb = AirBNB::new("Pater")

    mix_an_match(&mut hotel, &mut airbnb, "Piers")
}
```

## multiple trait bound

[multiple trait bounds](https://doc.rust-lang.org/book/ch10-02-traits.html#specifying-multiple-trait-bounds-with-the--syntax)

```rust
use std::collections::HashMap;

trait Accomodation {
    fn book(&mut self, name: &str, nights: u32) // returns a Unit by default (empty Tuple)
}

trait Description {
    fn get_description(&self) -> String {
        String::from("A wonderful place to stay")
    }
}

#[derive(Debug)]
struct Hotel {
    name: String,
    reservations: HashMap<String, u32>,
}

impl Hotel {
    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            reservations: HashMap::new(),
        }
    }
}

impl Accomodation for Hotel {
    fn book(&mut self, name: &str, nights: u32) {
        self.reservations.insert(name,.to_tring() nights);
    }
}

impl Description for Hotel {}

#[derive(Debug)]
struct AirBnB {
    host: String,
    guests: Vec<(String, u32)>,
}

impl AirBnB {
    fn new(host: &str) -> Self {
        Self {
            host: host.to_string(),
            guests: vec![],
        }
    }
}

impl Accomodation for AirBnB {
    fn book(&mut self, name: &str, nights: u32) {
        self.guests.push((name.to_tring(), nights));
    }
}

impl Description for AirBnB {
    fn get_description(&self) -> String {
        format!("Please enjoy {}'s apartment", self.host)
    }
}

fn book_for_one_night<T:Accomodation + Description>(entity: &mut impl T, guest: &str) {
    entity.book(guest, 1)
} 

fn mix_an_match(
    first: &mut (impl Accomodation + Description), 
    second: &mut impl Accomodation, 
    guest: &str,
) {
    first.book(guest, 1);
    first.get_Desciption();
    second.book(guest, 1);
}
```

## where clauses

[where clauses](https://doc.rust-lang.org/book/ch10-02-traits.html#clearer-trait-bounds-with-where-clauses)

```rust
fn mix_an_match<T, U>(
    first: &mut T, 
    second: &mut U, 
    guest: &str,
) where 
    T: Accomodation + Description,
    U: Accomodation,
{
    first.book(guest, 1);
    first.get_Desciption();
    second.book(guest, 1);
}
```

## trait as return types

[return types](https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-implement-traits)

```rust
fn choose_best_place_to_stay() -> impl Accomodation + Description {
    Hotel:::new("The Luxe")
    
    /*
    let likes_luxury = true;
    if likes_luxury {
        Hotel:::new("The Luxe")
    } else {
        AirBnB::new("Peter") // this provides a compile error
    }
    */
}

fn mix_an_match<T, U>(
    first: &mut T, 
    second: &mut U, 
    guest: &str,
) where 
    T: Accomodation + Description,
    U: Accomodation,
{
    first.book(guest, 1);
    first.get_Desciption();
    second.book(guest, 1);
}

fn main() {
    let mut hotel = choose_best_place_to_stay();
    let mut airbnd = AirBnB::new("Peter");

    mix_an_match(&mut hotel, &mut airbnb, "Piers")
    
}
```

## trait bounds to conditionaly implement methods

[trait bounds to conditionaly implement methods](https://doc.rust-lang.org/book/ch10-02-traits.html#using-trait-bounds-to-conditionally-implement-methods)

```rust
use std::fmt::Display;

struct Hotel<T> {
    name: T,
    reservations: HashMap<String, u32>,
}

impl<T> Hotel<T> {
    fn new(name: T) -> Self {
        Self {
            name: name
            reservations: HashMap::new(),
        }
    }
}

// trait bound -> constraint
impl<T: Display> Hotel<T> {
    fn summarize(&self) -> String {
        format!("{}: {}", self.name, self.get_description())
    }
}

impl<T> Accomodation for Hotel<T> {
    fn book(&mut self, name: &str, nights: u32) {
        self.reservation.insert(name.to_string(), nights);
    }
}

impl<T> Description for Hotel<T> {}

fn main() {
    let hotel1 = Hotel::new(String::from("The Luxe"));
    let hotel2 = Hotel::new("The Golden Standard");
    let hotel3 = Hotel::new(vec!["a", "b"]);
}
```

## trait objects

trait objects is an instance of a type that implements a particular trait whose methods will be accesses at runtime using a feature called dynamic dispatch

```rust
fn main() {
    let mut hotel = Hotel::new(String::from("The Luxe"));
    let mut airbnb = AirBnb::new("Peter");
    // this does not work since rust considers them as 2 different types
    //let stays = vec![hotel, airbnb];
    
    // dynamic dispath -> the exact method will be called at runtime
    // dynamic dispath is slower
    // dynamic dispath only works with references
    // rust looks at these as trait Objects
    let mut stays: Vec<&dyn Accomodation> = vec![&mut hotel, &mut airbnb];
    stays[0].book("Piers", 2)
    stays[1].book("Amanda", 2)
}
```

## scope

- the add trait must be available in the file
- this is to ensures the binary only includes things that are needed

```rust
use std:ops::Add;
use std::str::FromStr;

fn main() {
    let a = 5;
    let b = 10;
    let sum = a.add(b);

    let numeric_count = u64::from_str("5");
}
```

## project structure

src/lib.rs -> library crate
```rust
use std::collections::HashMap;
use std::fmt::Display;

pub trait Accomodation {
    fn book(&mut self, name: &str, nights: u32);
}

pub trait Description {
    fn get_description(&self) -> String {
        String::from("A wonderful place to stay")
    }
}

#[derive(Debug)]
pub struct Hotel<T> {
    name: T,
    reservations: HashMap<String, u32>,
}

impl<T> Hotel<T> {
    pub fn new(name: T) -. Self {
        Self {
            name,
            reservations: HashMap::new(),
        }
    }
}

impl<T: Display> Hotel<T> {
    pub fn summarize(&self) -> String {
        format!("{}: {}", self.name, self.get_description())
    }
}

impl<T> Accomodation for Hotel<T> {
    fn book(&mut self, name: &str, nights: u32) {
        self.reservation.insert(name.to_string(), nights);
    }
}

impl<T> Description for Hotel<T> {}

#[derive(Debug)]
struct AirBnB {
    host: String,
    guests: Vec<(String, u32)>,
}

pub impl AirBnB {
    pub fn new(host: &str) -> Self {
        Self {
            host: host.to_string(),
            guests: vec![],
        }
    }
}

impl Accomodation for AirBnB {
    fn book(&mut self, name: &str, nights: u32) {
        self.guests.push((name.to_tring(), nights));
    }
}

impl Description for AirBnB {
    fn get_description(&self) -> String {
        format!("Please enjoy {}'s apartment", self.host)
    }
}


pub fn book_for_one_night(entity: &mut impl Accomodation, guest: &str) {
    entity.book(guest, 1)
}

pub fn mix_an_match<T, U>(first: &mut T, second: &mut U, guest: &str) where 
    T: Accomodation + Description,
    U: Accomodation,
{
    first.book(guest, 1);
    first.get_Desciption();
    second.book(guest, 1);
}
```

src/main.rs -> binary crate
```rust
use traits::{mix_an_match, book_for_one_night, Hotel, AirBnb, Accomodation, Description};

fn main() {
    let mut hotel = Hotel::new(String::from("The Luxe"));
    println!("{}", hotel.summarize());
    hotel.book("Dana", 5);

    let mut airbnb = AirBnb::new("Peter");
    println!("{}", airbnb.get_description());
    book_for_one_night(&mut airbnb, "Dan");
    
    
    mix_and_match(&mut hotel, &mut airbnb, "Phil");
}
```

## project structure - multiple modules

src/lodging/mod.rs
```rust
use std:ops::Add;
use std::str::FromStr;

fn main() {
    let a = 5;
    let b = 10;
    let sum = a.add(b);

    let numeric_count = u64::from_str("5");
}
```

## project structure

src/lodging.rs -> library crate
```rust
use std::collections::HashMap;
use std::fmt::Display;

pub trait Accomodation {
    fn book(&mut self, name: &str, nights: u32);
}

pub trait Description {
    fn get_description(&self) -> String {
        String::from("A wonderful place to stay")
    }
}

#[derive(Debug)]
pub struct Hotel<T> {
    name: T,
    reservations: HashMap<String, u32>,
}

impl<T> Hotel<T> {
    pub fn new(name: T) -. Self {
        Self {
            name,
            reservations: HashMap::new(),
        }
    }
}

impl<T: Display> Hotel<T> {
    pub fn summarize(&self) -> String {
        format!("{}: {}", self.name, self.get_description())
    }
}

impl<T> Accomodation for Hotel<T> {
    fn book(&mut self, name: &str, nights: u32) {
        self.reservation.insert(name.to_string(), nights);
    }
}

impl<T> Description for Hotel<T> {}

#[derive(Debug)]
struct AirBnB {
    host: String,
    guests: Vec<(String, u32)>,
}

pub impl AirBnB {
    pub fn new(host: &str) -> Self {
        Self {
            host: host.to_string(),
            guests: vec![],
        }
    }
}

impl Accomodation for AirBnB {
    fn book(&mut self, name: &str, nights: u32) {
        self.guests.push((name.to_tring(), nights));
    }
}

impl Description for AirBnB {
    fn get_description(&self) -> String {
        format!("Please enjoy {}'s apartment", self.host)
    }
}
```

src/utils/mod.rs
```rust
//alternative
//use super::lodging::{Accomodation, Description};
use crate::lodging::{Accomodation, Description};

pub fn book_for_one_night(entity: &mut impl Accomodation, guest: &str) {
    entity.book(guest, 1)
}

pub fn mix_an_match<T, U>(first: &mut T, second: &mut U, guest: &str) where 
    T: Accomodation + Description,
    U: Accomodation,
{
    first.book(guest, 1);
    first.get_Desciption();
    second.book(guest, 1);
}
```

src/lib.rs
```rust
pub mod lodging;
pub mod utils;
```

src/main.rs -> binary crate
```rust
use traits::lodging::{Hotel, AirBnb, Accomodation, Description};
use traits::utils;

fn main() {
    let mut hotel = Hotel::new(String::from("The Luxe"));
    println!("{}", hotel.summarize());
    hotel.book("Dana", 5);

    let mut airbnb = AirBnb::new("Peter");
    println!("{}", airbnb.get_description());
    utils.book_for_one_night(&mut airbnb, "Dan");
    
    
    utils.mix_and_match(&mut hotel, &mut airbnb, "Phil");
}
```

## assocaited constant

An associated constant is a constant declared within a trait
A constant is a name for an immutable value

```rust
trait Taxable {
    const TAX_RATE: f64 = 0.25; // associated constant
    fn tax_bill(&self) -> f64;
}

#[derive(Debug)]
struct Income {
    amount: f64
}

impl Taxable for Income {
    
}

#[derive(Debug)]
struct Bonus {
    amount: f64
}

impl Taxable for Bonus {
    const TAX_RATE: f64 = 0.50;

    fn tax_bill(&self) -> f64 {
        self.amount * Self::TAX_RATE
    }
}

fn main() {
    let income = Income { amount: 50000.50 };
    println!("Total tax owed: ${:.2})", income.tax_bill());

    let bonus = Bonus { amount: 10000.23 };
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
}
```

## getter

An associated constant is a constant declared within a trait
A constant is a name for an immutable value

```rust
trait Taxable {
    const TAX_RATE: f64 = 0.25; // associated constant
    
    fn amount(&self) -> f64;

    fn tax_bill(&self) -> f64  {
        self.amount{} * Self::TAX_RATE
    }


}

#[derive(Debug)]
struct Income {
    amount: f64
}

impl Taxable for Income {
    fn amount(&self) -> f64 {
        self.amount
    }
}

#[derive(Debug)]
struct Bonus {
    amount: f64
}

impl Taxable for Bonus {
    const TAX_RATE: f64 = 0.50;

     fn amount(&self) -> f64 {
        self.amount
    }
}

fn main() {
    let income = Income { amount: 50000.50 };
    println!("Total tax owed: ${:.2})", income.tax_bill());

    let bonus = Bonus { amount: 10000.23 };
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
}
```

## setters

A setter methos is a method to set a value

```rust
trait Taxable {
    const TAX_RATE: f64 = 0.25; // associated constant
    // getter
    fn amount(&self) -> f64;
    // setter
    fn set_amount(&mut self, new_amount: f64);

    fn double_amount(&mut self) {
        self.set_amount(self.amount() * 2.0)
    }
    
    fn tax_bill(&self) -> f64  {
        self.amount{} * Self::TAX_RATE
    }
}

#[derive(Debug)]
struct Income {
    amount: f64
}

impl Taxable for Income {
    fn amount(&self) -> f64 {
        self.amount
    }

    fn set_amount(&mut self, new_amount: f64) {
        self.amount = new_amount;
    }
}

#[derive(Debug)]
struct Bonus {
    amount: f64
}

impl Taxable for Bonus {
    const TAX_RATE: f64 = 0.50;

    fn amount(&self) -> f64 {
        self.amount
    }

    fn set_amount(&mut self, new_amount: f64) {
        self.amount = new_amount;
    }
}

fn main() {
    let mut income = Income { amount: 50000.50 };
    println!("Total tax owed: ${:.2})", income.tax_bill());
    income.double_amount();
    println!("Total tax owed: ${:.2})", income.tax_bill());

    let mut bonus = Bonus { amount: 10000.23 };
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
    bonus.double_amount();
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
}
```

## supertraits (trait inheritence)

A supetrait is a trait from which another trait inherts functionality
The parent is called the supertrait and the child is called the subtrait

```rust
trait Investment {
    fn amount(&self) -> f64;

    fn set_amount(&mut self, new_amount: f64);

    fn double_amount(&mut self) {
        self.set_amount(self.amount() * 2.0)
    }
}

// inheritence
// Investment -> supertrait
// Taxable -> subtrait/childtrait
trait Taxable: Investment {
    const TAX_RATE: f64 = 0.25; // associated constant
    
    fn tax_bill(&self) -> f64  {
        self.amount{} * Self::TAX_RATE
    }
}

#[derive(Debug)]
struct Income {
    amount: f64
}

impl Investment for Income {
    fn amount(&self) -> f64 {
        self.amount
    }

    fn set_amount(&mut self, new_amount: f64) {
        self.amount = new_amount;
    }
}

impl Taxable for Income {}

#[derive(Debug)]
struct Bonus {
    amount: f64
}

impl Investment for Bonus {
    fn amount(&self) -> f64 {
        self.amount
    }

    fn set_amount(&mut self, new_amount: f64) {
        self.amount = new_amount;
    }
}

impl Taxable for Bonus {
    const TAX_RATE: f64 = 0.25; // associated constant
}

struct QualityTime {
    minutes: f64,
}

impl Investment for QualityTime {
    fn amount(&self) -> f64 {
        self.minutes
    }

    fn set_amount(&mut self, new_amount: f64) {
        self.minutes = new_amount;
    }
}

fn main() {
    let mut income = Income { amount: 50000.50 };
    println!("Total tax owed: ${:.2})", income.tax_bill());
    income.double_amount();
    println!("Total tax owed: ${:.2})", income.tax_bill());

    let mut bonus = Bonus { amount: 10000.23 };
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
    bonus.double_amount();
    println!("Total tax owed: ${:.2})", bonus.tax_bill());

    let weekend = QualityTime { minutes: 120.0 };
    println!("relaxation time: ${:.2}) min", weekend.amount());

}
```

## traits generics

```rust
trait Investment<T> {
    fn amount(&self) -> T;

    fn double_amount(&mut self) 
}

// if something chooses to implement taxable, it requires the investment to implement f64
trait Taxable: Investment<f64> {
    const TAX_RATE: f64 = 0.25; // associated constant
    
    fn tax_bill(&self) -> f64  {
        self.amount{} * Self::TAX_RATE
    }
}

#[derive(Debug)]
struct Income {
    amount: f64
}

impl Investment<f64> for Income {
    fn amount(&self) -> f64 {
        self.amount
    }

    fn double_amount(&mut self) {
        self.amount *= 2.0;
    }
}

impl Taxable for Income {}

#[derive(Debug)]
struct Bonus {
    amount: f64
}

impl Investment<f64> for Bonus {
    fn amount(&self) -> f64 {
        self.amount
    }

    fn double_amount(&mut self) {
        self.amount *= 2.0;
    }
}

impl Taxable for Bonus {
    const TAX_RATE: f64 = 0.25; // associated constant
}

#[derive(Debug)]
struct QualityTime {
    minutes: u32,
}

impl Investment<u32> for QualityTime {
    fn amount(&self) -> u32 {
        self.minutes
    }

    fn double_amount(&mut self) {
        self.minutes *= 2;
    }
}

fn main() {
    let mut income = Income { amount: 50000.50 };
    println!("Total tax owed: ${:.2})", income.tax_bill());
    income.double_amount();
    println!("Total tax owed: ${:.2})", income.tax_bill());

    let mut bonus = Bonus { amount: 10000.23 };
    println!("Total tax owed: ${:.2})", bonus.tax_bill());
    bonus.double_amount();
    println!("Total tax owed: ${:.2})", bonus.tax_bill());

    let weekend = QualityTime { minutes: 120.0 };
    println!("relaxation time: ${:.2}) min", weekend.amount());

}
```

## implementing the Display trait on a struct

[display trait](https://doc.rust-lang.org/std/fmt/trait.Display.html)

```rust
pub trait Display {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

```rust
use std:fmt::{Display, Formatter, Result}

struct Apple {
    kind: String,
    price: f64,
}

impl Display for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "{} 🍎 for {}", self.kind, self.price)
    }
}

fn main() {
    let lunch_snack: Apple = Apple {
        kind: String::from("Pink Ladies"),
        price: 1.04,
    }
    println!("{}", lunch_snack);
}
```

## implementing the Display trait with enum

```rust
use std:fmt::{Display, Formatter, Result}

enum AppleType {
    PinkLady,
    GrannySmith,
}

impl Display for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "🍎 lady 🍎"),
            AppleType::GrannySmith => write!(f, "🍏 ganysmith 🍏")
        }
    }
}

struct Apple {
    kind: AppleType,
    price: f64,
}

impl Display for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "{} for {}", self.kind, self.price)
    }
}

fn main() {
    let lunch_snack: Apple = Apple {
        kind: AppleType::PinkLady,
        price: 1.04,
    }
    println!("{}", lunch_snack);
}
```

## implementing the Display trait with enum

[debug trait](https://doc.rust-lang.org/std/fmt/trait.Debug.html)

```rust
pub trait Debug {
    // Required method
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), Error>;
}
```

```rust
use std:fmt::{Debug, Display, Formatter, Result}

enum AppleType {
    PinkLady,
    GrannySmith,
}

impl Display for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "🍎 lady 🍎"),
            AppleType::GrannySmith => write!(f, "🍏 ganysmith 🍏")
        }
    }
}

impl Debug for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "ApplyType::PinkLady"),
            AppleType::GrannySmith => write!(f, "ApplyType::GrannySmith")
        }
    }
}

struct Apple {
    kind: AppleType,
    price: f64,
}

impl Display for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "{} for {}", self.kind, self.price)
    }
}

impl Debug for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "Apple ::: [ Kind: {}, Price: {} ]", self.kind, self.price)
    }
}

fn main() {
    let lunch_snack: Apple = Apple {
        kind: AppleType::PinkLady,
        price: 1.04,
    }
    println!("{}", lunch_snack);
}
```

## formatter methods

```rust
use std:fmt::{Debug, Display, Formatter, Result}

enum AppleType {
    PinkLady,
    GrannySmith,
}

impl Display for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "🍎 lady 🍎"),
            AppleType::GrannySmith => write!(f, "🍏 ganysmith 🍏")
        }
    }
}

impl Debug for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "ApplyType::PinkLady"),
            AppleType::GrannySmith => write!(f, "ApplyType::GrannySmith")
        }
    }
}

struct Apple {
    kind: AppleType,
    price: f64,
}

impl Display for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "{} for {}", self.kind, self.price)
    }
}

impl Debug for Apple {
    fn fmt(&self, formatter: &mut Formatter<'_>) -> Result {
        formatter
        .debug_struct("** Apple **") //DebugStruct
        .field("Kind", &self.kind)
        .field("Price", &self.price)
        .finish()
    }
}

fn main() {
    let lunch_snack: Apple = Apple {
        kind: AppleType::PinkLady,
        price: 1.04,
    }
    println!("{}", lunch_snack);
}
```

## implementing the Drop trait

[drop trait](https://doc.rust-lang.org/std/ops/trait.Drop.html)

```rust
pub trait Drop {
    // Required method
    fn drop(&mut self);
}
```

if we want to cleanup things before dropping
- write a file to file system

```rust
use std:fmt::{Debug, Display, Formatter, Result};
use std::fs;
use std::ops::Drop;

enum AppleType {
    PinkLady,
    GrannySmith,
}

impl Display for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "🍎 lady 🍎"),
            AppleType::GrannySmith => write!(f, "🍏 ganysmith 🍏")
        }
    }
}

impl Debug for AppleType {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            AppleType::PinkLady => write!(f, "ApplyType::PinkLady"),
            AppleType::GrannySmith => write!(f, "ApplyType::GrannySmith")
        }
    }
}

struct Apple {
    kind: AppleType,
    price: f64,
}

impl Display for Apple {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        // f: write to formatter
        write!(f, "{} for {}", self.kind, self.price)
    }
}

impl Debug for Apple {
    fn fmt(&self, formatter: &mut Formatter<'_>) -> Result {
        formatter
        .debug_struct("** Apple **") //DebugStruct
        .field("Kind", &self.kind)
        .field("Price", &self.price)
        .finish()
    }
}

impl Drop for Apple {
    fn drop(&mut self) {
        //println!("Apple is being cleaned up");
        match fs::remove_file("apple.txt") {
            Ok(_) => println!("Goodbye, my sweet apple"),
            Err(Error) => eprintln!("Error deleting file: {error}"),
        }
    }
}

fn main() {
    let lunch_snack: Apple = Apple {
        kind: AppleType::PinkLady,
        price: 1.04,
    }
    println!("{}", lunch_snack);
}
```

## Clone trait

The clone trait models the ability to create a duplicate of an instance

[clone trait](https://doc.rust-lang.org/std/clone/trait.Clone.html)

```rust
pub trait Clone: Sized {
    // Required method
    fn clone(&self) -> Self;

    // Provided method
    fn clone_from(&mut self, source: &Self) { ... }
}
```

```rust
use std::clone::Clone;

#[derive(Clone)] // this only works if the types implement the clone trait
struct Appointment {
    doctor: String,
    start_time: String,
    end_time: String,
}

impl Appointment {
    fn new(doctor: &str, start_time: &str, end_time: &str) -> Self {
        Self {
            doctor: doctor.to_string(),
            start_time: start_time.to_string(),
            end_time: end_time.tp_string(),
        }
    }
}

/*
impl Clone for Appointment {
    fn clone(&self) -> Self {
        Self {
            doctor: self.doctor.clone(),
            start_time: self.start_time.clone(),
            end_time: self.end_time.clone(),
        }
    }
}
*/

fn main() {
    let morning_appt = Appointment:::new("Mr Andrews", "09:00 AM", "09:15")
    let replacement_appt = morning_appt.clone();
    println!("{} is seeing the patent from {} to {}",
        replacement_appt.doctor, replacement_appt.start_time, replacement_appt.end_time);
}
```

## copy trait

[copy trait](https://doc.rust-lang.org/std/marker/trait.Copy.html)

```rust
pub trait Copy: Clone { }
```

sub trait of the clone super/parent trait

if a type implement the copy trait, whenever we assign it to another variable it gets copied/duplicated

Note: this does not work if you use String types -> since String does not implement the copy sub trait

```rust
#[derive(Debug, Clone)]
struct Duration {
    hours: u32,
    mins: u32,
    secs: u32,
}

impl Duration {
    fn new(hours: u32, mins: u32, secs: u32) -> Self {
        Self {
            hours,
            mins,
            secs,
        }
    }
}

impl Copy for Duration {}

fn main() {
    let one_hour = Duration::new(1, 0, 0);
    let another_hour = one_hour;

    println!(":?", one_hour);
}
```

## PartialEq trait

[partial Eq trait](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html)

The PartialEq trait establishes equality between two values

```rust
pub trait PartialEq<Rhs = Self>
where
    Rhs: ?Sized,
{
    // Required method
    fn eq(&self, other: &Rhs) -> bool;

    // Provided method
    fn ne(&self, other: &Rhs) -> bool { ... }
}
```

```rust
struct Flight {
    origin: String,
    destination: String,
    time: String,
}

impl Flight {
    fn new(origin: &str, destination: &str, time: &str) -> Self {
        Self {
            origin: origin.to_string(),
            destination: destination.to_string(),
            time: time.to_string(),
        }
    }
}

impl PartialEq for Flight {
     fn eq(&self, other: &Rhs) -> bool {
        self.origin == other.origin && self.destination == other.destination
     }
}

fn main() {
    let a = Flight::new("JFK", "LON", "08:00");
    let b = Flight::new("JFK", "LON", "23:00");
    let c = Flight::new("JFK", "LAS", "08:00");
    println!("{{}}", a == b);
    println!("{{}}", a.eq(&b));
    println!("{{}}", a.ne(&b));
}
```

## defining equality for different types

```rust
struct Bustrip {
    origin: String,
    destination: String,
    time: String,
}

impl Bustrip {
    fn new(origin: &str, destination: &str, time: &str) -> Self {
        Self {
            origin: origin.to_string(),
            destination: destination.to_string(),
            time: time.to_string(),
        }
    }
}

impl PartialEq<Flight> for Bustrip {
     fn eq(&self, other: &Flight) -> bool {
        self.time == other.time
     }
}


struct Flight {
    origin: String,
    destination: String,
    time: String,
}



impl Flight {
    fn new(origin: &str, destination: &str, time: &str) -> Self {
        Self {
            origin: origin.to_string(),
            destination: destination.to_string(),
            time: time.to_string(),
        }
    }
}

impl PartialEq for Flight {
     fn eq(&self, other: &Rhs) -> bool {
        self.origin == other.origin && self.destination == other.destination
     }
}

impl PartialEq<BusTrip> for Flight {
     fn eq(&self, other: &BusTrip) -> bool {
        self.time == other.time
     }
}

fn main() {
    let a = Flight::new("JFK", "LON", "08:00");
    let b = BusTrip::new("LAS", "TOK", "08:00");
    println!("{{}}", a == b);
    println!("{{}}", a.eq(&b));
    println!("{{}}", a.ne(&b));
}
```

## ParialEq Trait for Enums

```rust
enum Muscician {
    SingerSongwriter(String)
    Band(u32)
}

use Muscician::{Band, SingerSongwriter};

impl PartialEq for Muscician {
    fn eq(&self, other: &Muscician) -> bool {
        match self {
            SingerSongwriter(name) => match other {
                SingerSongwriter(other_name) => name == other_name,
                Band(_) => false
            },
            Band(members) => match other {
                SingerSongwriter(_) => false,
                Band(other_members) => members == other_members,
            },
        }
    }
}

fn main() {
    let a = SingerSongwriter("Wim".to_String());
    let b = SingerSongwriter("Wim".to_String());
    let c = SingerSongwriter("Mieke".to_String());

    let b1 = Band(5);
    let b2 = Band(4);
    let b3 = Band(5);

    println!("{}", a == c); // false
    println!("{}", a == b); // true

    println!("{}", b1 == b3); // true

    println!("{}", b1 == a); // false

}
```

## Eq trait

[Eq trait](https://doc.rust-lang.org/std/cmp/trait.Eq.html)

sub trait of the PartialEq trait

3 additional principles
- reflexive a == a; // with itself
- symmetric a == b implies b == a (required by PartialEq as well)
- transitive a== b and b == c implies a ==c (required)

f32, f64 -> they cannot guarantee equality -> they implement NaN (not a number)

```rust
#[derive(PartialEq, Eq)]
struct Flight {
    origin: String,
    destination: String,
    time: String,
}

impl Flight {
    fn new(origin: &str, destination: &str, time: &str) -> Self {
        Self {
            origin: origin.to_string(),
            destination: destination.to_string(),
            time: time.to_string(),
        }
    }
}

fn main() {
    let a = Flight::new("JFK", "LON", "08:00");
    let b = Flight::new("JFK", "LON", "08:00");
    let c = Flight::new("JFK", "LON", "08:00");
    println!("{{}}", a == a);
    println!("{{}}", a == b);
    println!("{{}}", b == a);
    println!("{{}}", b == c);
}
```

## PartialOrd trait

[PartialOrd trait](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html)

trait indicates that a type can be ordered/sorted

```rust
pub trait PartialOrd<Rhs = Self>: PartialEq<Rhs>
where
    Rhs: ?Sized,
{
    // Required method
    fn partial_cmp(&self, other: &Rhs) -> Option<Ordering>; // returns nested enum

    // Provided methods
    fn lt(&self, other: &Rhs) -> bool { ... }
    fn le(&self, other: &Rhs) -> bool { ... }
    fn gt(&self, other: &Rhs) -> bool { ... }
    fn ge(&self, other: &Rhs) -> bool { ... }
}
```

```rust
use std::cmp:Ordering

struct Job {
    stalary: u32
    commute_time: u32
}

impl PartialEq for Job {
    fn eq(&self, other &Self) -> bool {
        self.salary == other.salary
    }
}

impl Eq for Job {}

impl PartialOrd for Job {
    fn partial_cmp(&self, other &Self) -> Option<Ordering> {
        self.salary.partial_cmp(&other.salary) 
        
        /*
        if self.salary == other.salary {
            Some(Ordering::Equal)
        } else if self.salary < other.salary {
            Some(Ordering::Less)
        } else if self.salary > other.salary {
            Some(Ordering::Greater)
        } else {
            None
        }
        */
    }
}

fn main() {
    let long = Job {
        salary: 100000,
        commute_time: 2,
    }

    let long = Job {
        salary: 75000,
        commute_time: 1,
    }

    println!("{}", long > short)
    println!("{}", long < short)
    println!("{}", long == short)
    // lt, le, gt, ge, 
}
```

## associated types

An associated type is a placeholder for a type that is required within a trait

```rust
use std::ops::Add;

#[derive(Debug)]
struct Lunch {
    cost: f64,
}

impl Add for Lunch {
    // associated type
    // we need to provide a concrete type for this trait
    type Output = Lunch
    
    fn add(self, rhs: Self) -> Self::Output {
        Self {
            cost: self.cost + rhs.cost
        }
    }
}

fn main() {
    let one = Lunch { cost: 19.99 };
    let two = Lunch { cost: 29.99 };

    println!("{:?}", one + two)
}
```

## assicated type II

```rust
use std::ops::Add;

fn add_two_numbers<T:Add<Output = T>>(a: T, b: T) -> T {
    a + b
}

fn main() {
    let int_sum = add_two_numbers(1, 2);
    let float_sum = add_two_numbers(1.0, 2.0);
}
```