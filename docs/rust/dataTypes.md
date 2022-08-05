# data types

- boolean: true, false
- integer
- double
- float
- char
- string

## variables

immutable -> default, faster since the data does not need to change
mutable

variable assignment

```
let two = 2;                // integer
let hello = "hello";        // string
let j = 'j';                // char
let my_half = 0.5;          // float
let mut my_name = "Bill";   // mutable string
let quit_program = false    // bool
```

## enum

data that be one of multiple different possibilities
- each possibility is a variant
- can only be one variant at a time
- more robust when paired with match
- easier to read
provides information to the compiler


```
// Direction is name of the enumeration
enum Direction {
    Left,
    Right
}

fn main() {
    let go = Direction::Left;
    match go {
        Direction::Left => println!("go left"),
        Direction::Right => println!("go right"),
    }
}
```

Additional properties

enum is not limited to just plain variants
- each variant can optionally contain additional data
  - the data can be another enum
- if data is required it has to be there

```
enum Mouse {
    LeftClick,
    RightClick,
    MiddleCloick,
    Scroll(i32),
    Move(i32, i32),
}

enum PromoDiscount {
    NewUser,
    Holiday(String),
}

enum Discount {
    Percent(f64),
    Flat(i32),
    Promo(promoDiscount),
    Custom(String),
}

```

## struct

- a data type that contain multiple pieces of data
  - all or nothing - cannot have some pieces of data and not others
- each piece of data is called a "field"
  - fiels can be accessed using a dot
- makes working with data easier
  - similar data can be grouped together


```
// ShippingBox is name of the struct
struct ShippingBox {
    depth: i32,
    width: i32,
    heighth: i32,
}

let my_box = ShippingBox{
    depth: 3,
    width: 2,
    height: 5,
};

let tall = my_box.height;
println!("the box is {:?} units tall", tall);
```

Exercise a8

## Tuples

a type of record
store data anonymously, iow allow for anonymoud data access
    - no need to name fields
useful when destructuring
can contain any number of fields
    - use struct when more than 2 or 3 fields

```
fn one_two_three -> (i32, i32, i32) {
    (1, 2, 3)
}
let numbers = one_two_three();
// this is destructuring
let (x, y, z) = one_two_three();
println!("{:?}, {:?}", x, numbers.0);

enum Access {
    Full,
}
let (employee, access) = ("Jake", Access::Full);
```

Exercise a9

## Implementation

```
struct Temperature {
    degress_f: f64,
}

impl Temperature {
    // upper case self -> create a new temprature
    fn freezing() -> Self {
        Self { degrees_f: 32.0}
    }

    // lower case self assumes that a Temprature object exists
    fn show_temp(&self) {
        println!("{:?} degrees F", self.degrees_f);
    }
}

fn main() {
    let hot = Temperature { degrees_f: 99.9};
    hot.show_temp();

    let cold = Temperature::freezing();
    cold.show_temp();
}
```

Exercise a12

## Vector

- multiple pieces of data
  - same type
- used for lists of information
- can add, remove and traverse the entries
- The vec! macro can be used to simplify the coode

```
let my_numbers = vec![1,2,3];

let mut my_numbers = Vec::new();
my_numbers.push(1);
my_numbers.push(2);
my_numbers.push(3);
my_numbers.pop();
my_numbers.len();

let two = my_numbers[1];

// for each number in my_number collection
for num in my_numbers {
    println!("{:?}", num);
}
```

exercise a13


###  vector iterators
add one to the vector

```
fn main() {
    let numbers =vec![1.2.3.4.5];

    //let mut plus_one = vec![];
    //for num in numbers {
    //    plus_one.push(num + 1);
    //}

    // use type annotations
    let plus_one: Vec<_> = numbers
        .iter()
        .map(|num| num + 1)
        .collect();
    
    // filter items and keep the once we want
    let new_numbers: Vec<_> = numbers
        .iter()
        .filter(|num| num <= 3)
        .collect();

    // find items and return an option
    let find_me: Option<i32> = numbers
        .iter()
        .find(|num| num == 40)

    // count
    let count = numbers
        .iter()
        .count();
    
    // last
    let last: Option<i32> = numbers
        .iter()
        .last();

    // min
    let min: Option<i32> = numbers
        .iter()
        .min();

    // max
    let min: Option<i32> = numbers
        .iter()
        .max();
    
    // take 3 items
    let min: Vec<i32> = numbers
        .iter()
        .take(3);
        .collect();

}
```

execise a24

## strings

- two commonly used types of strings
  - String - owned
  - &str - borrowed String slice
- Must use an owned String to store in a struct
- Use &str when passing to a function

```
fn print_it(data: &str) {
    println!("{:?}", data);
}

fn main() {
    // automatically borrowed
    print_it("a string slice");
    // owned 
    let owned_string = "owned string.to_owned();
    let anothr_owned = String::from("another");
    print_it(&owned_string);
    print_it(&another_owned);
}
```

```
struct Employee {
    name: String,
}

fn main() {
    let emp_name = "Jayson".to_owned();
    let emp_name = String::from("Jayson");
    let emp Employee{
        name: emp_name,
    }
}
```

Exercise a14

## type annotations

- type annotations are mostly optional within function bodies
  - occasionally required if compilar cannot infer the type
- can be specified when using let bindings

let num: i32 = 15;

generics

let numbers: Vec<i32> = vec![1,2,3];
let letters: Vec<char> = vec!['a', 'b', 'c'];
let clicks: Vec<Mouse> = vec![
    Mouse::LeftClick,
    Mouse::LeftClick,
    Mouse::RightClick,
];

## Option

- a type that may be one of 2 things
  - same data of a specified type
  - nothing
- Used in scenarios where data may not be reqquired or is available
  - unable to find something
  - ran out of items in a list
  - Form field not filled out

```
// <T> option contains some data, the type we dont now
enum Option<T> {
    Some(T), // represents some data, T is whatever type
    None     //
}
```

example

```
struct Customer {
    age: Option<i32>,
    email: String,
}

let mark = Customer {
    age: Some(22), email: "mark@example.com".to_owned(),
};
let becky = Customer {
    age: None, emaul: "becky@example.com".to_owned(),
};
match becky.age {
    Some(age) => println!("Customer is {:?} years", age),
    None => println!("customer age not provided").
}
```

```
for item in proceries {
    if item.name == name {
        return Some(item.qty);
    }
}
None
```

Demo

```
struct Survey {
    q1: Option<i32>,
    q2: Option<bool>,
    q3: Option<string>,
}

fn main() {
    let response = Survey {
        q1: Some(12),
        q2: Some(true),
        q3: Some("A".to_owned()),
    }
    match response.q1 {
        Some(ans) => println!("q1: {:?}", ans),
        None => println!("q1 no response"),
    }
     match response.q2 {
        Some(ans) => println!("q2: {:?}", ans),
        None => println!("q2 no response"),
    }
     match response.q2 {
        Some(ans) => println!("q2: {:?}", ans),
        None => println!("q2 no response"),
    }

}
```

see exercise a16

### Option combinators

```
fn main() {
    let a: Option<i32> = Some(1);
    dbg!(a);

    let a_is_some = a.is_some();
    let a_is_some = a.is_none();
    // only applies if there is data
    let a_mapped = a.map(|num| num + 1)
    // only applies if there is data, if it matches it returns the number, else it returns None
    let a_filered = a.filer(|num| num == &1)

    // used when no data is returned but you want some data
    let a_or_else = a.or_else(|| Some(5));

    // the difference is that the Option wrapper is removed
    let unwrapped = a.unwrap_or_else(|| 0);

}
```

## Result

- a data type that contains one of 2 types of data:
  - successful data: Ok(variable_name)
  - error data: Err(variabale_name)
- used in scenarios where an action needs to be taken, but has the possibility of a failure
  - copying a file
  - connection to a website
- use Result<T, E>

```
// T placeholder for any type
// E placeholder for error
enum Result<T, E> {
    Ok(T),
    Err(E)
}
```

```
fn get_sound(name: &str) -> Result<SoundData, String> {
    if name == "alert" {
        ok(SoundData::new("alert")),
    } else {
        Err("unable to find sound data".to_owned())
    }
}

let sound = get_sound("alert);
match sound {
    Ok(_) => println!("sound data located"),
    Err(e) => println!(""error {:?}", e),
}
```

demo

```
#[derive(Debug)]
enum MenuChoice {
    MainMenu,
    Start,
    Quit,
}

fn get_choice(input: &str) -> result<MenuChoice, String> {
    match input {
        "mainmenu" => Ok(MenuChoice::MainMenu),
        "start" => Ok(MenuChoice::Start),
        "quit" => Ok(MenuChoice::Quit),
        _ => Err("menu choice not found".to_owned()),
    }
}

fn print_choice(choice: &MenuChoice) {
    println!("choice = {:?}", choice);
}

// function is used in the shorted version
fn pick_choice(input: &str) -> Result<(), String> {
    // ? autmatically executes a match
    // if Ok the choice is filled, if Err a return is called with a string
    let choice = get_choice(input)?;
    print_choice(&choice);
    Ok(())
}

fn main() {
    // shorter version
    let choice = pick_choice("end");
    println("choice value = {:?}, choice);

    // longer version
    //let choice: Result<MenuChoice, _> = get_choice("mainmenu");
    //match choice {
    //    Ok(inner_choice) => print_choice(&inner_choice),
    //    Err(e) => println!("error = {:?}", e), 
    //}
}
```

[error articale anyhow](https://nick.groenen.me/posts/rust-error-handling/)


### this error

```
use thiserror:Error;

#[Derive(Debug, Error)]
#[error("Error A occured")]
struct ErrorA {
    #[from]
        source: ErrorB
};

#[Derive(Debug, Error)]
#[error("Error B occured")]
struct ErrorB;

fn return_error_a() -> Result<bool, ErrorA> {
    Err(ErrorA {Source: ErrorB})
}

fn return_error_b() -> Result<bool, ErrorB> {
    Err(ErrorB)
}

fn main() -> Result<(), ErrorA> {
    return_error_a();
    return_error_b();
    Ok(())
}
```

### anyhow

deals with dynamic error types

```
use thiserror:Error;
use anyhow::Result;

#[Derive(Debug, Error)]
#[error("Error A occured")]
struct ErrorA {
    #[from]
        source: ErrorB
};

#[Derive(Debug, Error)]
#[error("Error B occured")]
struct ErrorB;

fn return_error_a() -> Result<bool, ErrorA> {
    Err(ErrorA {Source: ErrorB})
}

fn return_error_b() -> Result<bool, ErrorB> {
    Err(ErrorB)
}

fn main() -> Result<()> {
    return_error_a();
    return_error_b();
    Ok(())
}

## HashMaps

- collection that stores data as key-value pair
  - data is located using a key
  - the data is the value
- similar to a definition in a dictionary
- very fast to retrieve data using the ley
- data is stored in random order

```
let mut people = HashMap::new();
// Susan -> key, 21 is Value
people.insert("Susan", 21);
people.remove("Susan");

match people.get("Susan") {
    Some(age) => println!("age = {:?}", age),
    None => println!("not found),
}

for (person, age) in people.iter() {
    println!("person = {:?}, age = {:?}", person, age);
}

for person in people.keys() {
     println!("person = {:?}", person);
}

for age in people.values() {
     println!("age = {:?}", age);
}
```

```
use std::collection:; HashMap;

struct Contents {
    content: String,
}

fn main() {
    let mut lockers = HashMap::new();
    lockers.insert(1, Contents{content: "stuff".to_owned()});
    lockers.insert(2, Contents{content: "shirt".to_owned()});
    lockers.insert(3, Contents{content: "gym charts".to_owned()});

    for (locker_number, content) in lockers.iter() {
        println!("number: {:?}, content: {:?}", locker_number, content);
    }

}
```

## Ranges

easy way to generate numbers for you

```
fn main {
    // includes the 3
    let range = 1..=3;
    // does not include 4
    let range = 1..4;
}
```

## const

create const values in the code

```
const MAX_SPEED: i32 = 9000;

fn clamp_speed(speed: i32) -> i32 {
    if speed > MAX_SPEED {
        MAX_SPEED
    } else {
        speed
    }
}

fn main() {

}
```

## custom error types

allow to use multiple different function that might fail in different ways but seamlessly work together

```
use thisError::Error

// error type -> Error derive 
#[derive{Error, Debug}]
enum LoginError {
    // used for println
    #[error("database error")]
    // convert #[from] SqlError to databaseError/LoginError
    DatabaseError(#[from] SqlError),


    #[error("password expired")]
    PasswordExpired,

    #[error("user not found")]
    UserNotFound,

    #[error("network connection error")]
    NetworkError($[From] std::io::Error),

    #[error("wrong password")]    
    WrongPassword,
}

// Result is a session id
fn login(user: &str, password: &str) -> Result<String, LoginError> {
    let connection: Result<Connection, std::io::Error> = connect()?;
    let user_id = get_user_id(user?);
    if try_password(user_id, password)? {
        let session: Result<String, SqlError> = get_ession(user_id)?;
        Ok(session)
    } else {
        Err(LoginError::WrongPassword)
    }
}

fn main() {
    login("kate", "123);
}
```

exercise a27

## New Types

specific type for a specific piece of data -> less error prone

```
struct NeverZero(i32);

impl NeverZero {
    fn new(i: i32) -> Result<Self, String> {
        if i == 0 {
            Err("cannot be zero".to_owned())
        } else {
            Ok(Self(i))
        }
    }
}

fn divide(a: i32, b: NeverZero) -> i32 {
    let b = b.0
    a / b
}

fn main() {
    match NeverZero::new(0) {
        Ok(nz) => println!("{:?}", divide(10, nz)),
        Err(e) => println!("{:?}", e)
    }
}
```

exercise a28

