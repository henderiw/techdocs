# option result enums

[option enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html#the-option-enum-and-its-advantages-over-null-values)

option and result enum use generics

## option enum

The Option enum models a scenario where a type could be a valid value or nothing at all

example:
- modeling temprature -> how to model an absense of the value

solution: Option enum

Option::None represents an absent value
Option::Some(T) represent a present value

-> Tuple

```rust

fn main() {
    let a: Option<i32> = Option::Some(5); // i32
    let b: Option<&str> = Option::Some("hello");

    let a = Option::<i16>::Some(5); // i32
    let d: Option<&str> = Option::None; // we have to tell the type since reassignment will allow the compiler to know what the type was
}
```

```rust
fn main() {
    let instrument = [
        String::from("Guitar"),
        String::from("Drums"),
        String::from("Bass"),
    ];

    // returns an Option enum
    // Option enum -> possibility None if the position does not exist
    // Option enum -> reference to string
    let bass: Option<&String> = instrument.get(2);
    println!("{?}, bass")

    let invalid: Option<&String> = instrument.get(100);
    println!("{?}, bass")
}
```

## unwrap, expect methods

[unwrap and expect](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#shortcuts-for-panic-on-error-unwrap-and-expect)

How to get the value from the Option

unwrap method attempts to extract the associated data out of the Some variant
-> there is some risk, NOt SAFEST
-> both of these methods are optimistic

```rust
fn main() {
    let instrument = [
        String::from("Guitar"),
        String::from("Drums"),
        String::from("Bass"),
    ];

    // returns an Option enum
    // Option enum -> possibility None if the position does not exist
    // Option enum -> reference to string
    let bass: Option<&String> = instrument.get(2);
    println!("{?}, bass")
    let valid_instrument = bass.unwrap();
    let valid_instrument = bass.expect(mag: "Unable to retrieve element");
    println!("{valid_instrument}");

    let invalid_instrument: Option<&String> = instrument.get(100);
    println!("{:?}, bass", invalid_instrument)
    invalid_instrument.unwrap(); // this panics
    invalid_instrument.expect(mag: "Unable to retrieve element"); // this provides the error message
}
```

match keyword

[match option](https://doc.rust-lang.org/book/ch06-02-match.html#matching-with-optiont)

```rust
fn main() {
    let instrument = [
        String::from("Guitar"),
        String::from("Drums"),
        String::from("Bass"),
    ];


    let bass: Option<&String> = instrument.get(2);
    play(bass)

    let invalid_instrument: Option<&String> = instrument.get(100);
    play(invalid_instrument)
    
}

fn play(instrument_option: Option<&String>) {
    match instrument_option {
        Option::Some(instrument) => println!("Playing {instrument}"),
        Option::None => println!("Singing with my voice"),
    }
}
```

## return option from fn

```rust
fn is_item_in_stock(item_is_in_system: bool, item_is_in_stock: bool) -> Option<bool> {
    if item_is_in_system ** item_is_in_stock {
        Option::Some(true)
    } else if item_is_in_system {
        Option::Some(false)
    } else {
        Option::None
    }
}

fn main() {
    let availability = is_item_in_stock(true, true);
    println!("{availability:?}")

    match availability {
        Option::Some(value) => println!("item is available: {value}")
        Option::None => println!("item is not available")
    }
}
```

## top levle Option variants

The Rust prelude is a collection of named constructs that are available automatically in a rust program
-> Some, None are available since they are very common

```rust
fn is_item_in_stock(item_is_in_system: bool, item_is_in_stock: bool) -> Option<bool> {
    if item_is_in_system ** item_is_in_stock {
        Some(true)
    } else if item_is_in_system {
        Some(false)
    } else {
        None
    }
}

fn main() {
    let availability = is_item_in_stock(true, true);
    println!("{availability:?}")

    match availability {
        Some(value) => println!("item is available: {value}")
        None => println!("item is not available")
    }
}
```

## unwrap_or method

mandates an argument -> falalback argument

```rust
fn main() {
    let present_value = Some(13);
    let missing_value: Option<i32> = None;

    println!("{}", present_value.unwrap_or(0))
}
```

## building option from scratch

```rust
#[derive(Debug, Copy, Clone)]
enum MyOption {
    Some(i32),
    None
}

impl MyOption {
    // we allow ownership since we have the copy trait
    fn unwrap(self) -> i32 {
        match self {
            MyOption::Some(value) => value,
            MyOption::None => panic!("Uh oh"),
        }
    }
    fn unwrap_or(self, fallback i32) -> i32 {
        match self {
            MyOption::Some(value) => value,
            MyOption::None => fallback,
        }
    }
}

fn main() {
    let some_option = MyOption::Some(100);
    println!("{}", some_option.unwrap())
    let none_option = MyOption::None;
    println!("{}", none_option.unwrap())
}
```

## Result enum

return: success versus error
variant:
- OK Variant
- Err Variant
generic types:
- T
- E
implement the debug trait

[result enum](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#recoverable-errors-with-result)

```rust
pub enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

```rust
fn main() {
    // we need to tell the 
    let ok: Result<i32, &str> = Ok(5)
    let nok: Result<i32, &str> = Err("something went wrong")

    println!("{:?}", ok)
    println!("{:?}", nok)
}
```

```rust
fn main() {
    let text = "50";
    // can be ok or nok with turbofish operator
    let text_as_nbr: Result<i32, ParseIntError> = text.parse::<i32>();
    println!("{:?}", text_as_nbr)

    let text = "aaaa";
    // can be ok or nok with turbofish operator
    let text_as_nbr: Result<i32, ParseIntError> = text.parse::<i32>();
    println!("{:?}", text_as_nbr)
}
```

## returning enum result from fn

```rust
fn divide(numerator: f64, denominator: f64) -> Result<f64, String> {
    if denominator == 0.0 {
        Err("devide by 0".to_string()) // heap allocated string
    } else {
        Ok(numerator / denominator)
    }
}

fn main() {
    let result = divide(10.0, 2.0);
    match result {
        Ok(calculation) => println!("result: {}", calculation)
        Err(msg) => println!("error: {}", msg)
    }

}
```

## Result methods

result enum has methods for extraction

```rust
fn divide(numerator: f64, denominator: f64) -> Result<f64, String> {
    if denominator == 0.0 {
        Err("devide by 0".to_string()) // heap allocated string
    } else {
        Ok(numerator / denominator)
    }
}

fn main() {
    let result = divide(10.0, 2.0);
    // unwrap is ok when success
    println!("{}", result.unwrap())
    // expect will panic but with an error
    println!("{}", result.expect("unable to parse divide"))
    // 
    println!("{}", result.unwrap_or(0.0))

    // return a bool
    println!("{}", result.is_ok())
    println!("{}", result.is_err())

}
```

in result the T can implement the copy trait or not

```rust
fn operation(great_success: bool) -> Result<String, String> {
    if great_success {
        Ok("Success".to_string())
    } else {
        Err("Error".to_string())
    }
}

fn main() {
    let my_result = operation(true);
    // content becomes the owner
    let content = match &my_result {
        Ok(message) => message,
        Err(error =>)error,
    }

    // the compiler fails, since the content moved
    println!("{}", my_result.unwrap());
}
```

other option

```rust
fn operation(great_success: bool) -> Result<&'static str, &'static str> {
    if great_success {
        Ok("Success")
    } else {
        Err("Error")
    }
}

fn main() {
    let my_result = operation(true);
    // content becomes the owner
    let content = match &my_result {
        Ok(message) => message,
        Err(error) => error,
    }

    // the compiler fails, since the content moved
    println!("{}", my_result.unwrap());
}
```