# error handling

error handling
- process of dealing with potential errors from operations that go wrong
- types
    - recoverable errors
    - unrecoverable errors
- runtime/compile time error
- backtrace

## panic

[panic macro](https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html#unrecoverable-errors-with-panic)

[macro panic](https://doc.rust-lang.org/std/macro.panic.html)

```rust
fn main() {
    // causes a panic
    None.unwrap() 

    let a = 1;
    // safe cleanup
    panic!("something went wrong")
}
```

## process module and the exit function

[exit](https://doc.rust-lang.org/std/process/fn.exit.html)

```rust
// process module
use std::process;

fn main() {
    // 0 if there is no error
    // if there is an error -> 1 or > 0
    process::exit(1)
}
```

## standard error (eprintln!)

[eprintln](https://doc.rust-lang.org/std/macro.eprintln.html)
- print to stderr iso stdout
- 

```rust
fn main() {
    // stdout
    println!("some update");
    // stderr
    eprintln!("some error message");
}
```

cargo run > example.txt

## opening a file

```rust
use std::fs::File; // struct
use std::process;

fn main() {
    // return a Result enum
    let file = match File::open("story.txt") {
        Ok(file) => file,
        Err(error) => {
            eprintln!("some went wrogn reading the file {error:?}");
            process.Exit(1)
        }
    };
    // from here we have a valid file
}
```

## asking for user input

[read_line](https://doc.rust-lang.org/std/io/struct.Stdin.html#method.read_line)

```rust
use std::fs::File; // struct
use std::process;
use std::io::stdin;

fn main() {
    println!("Please provide input file");
    let mut input = String::new();

    let user_requested_file = stdin().read_line(input);
    if let Err(error) = user_requested_file {
        eprintln!("something went wrong collecting user input {error:?}");
            process::exit(1)
    }

    // returns a Result enum
    let file = match File::open(input.trim()) {
        Ok(file) => file,
        Err(error) => {
            eprintln!("some went wrogn reading the file {error}");
            process::exit(1)
        }
    };
    // from here we have a valid file
    println!("{file:?}");
}
```

## reading file content

Each of the operations we get a Result and we provide
a check and in case of error we exit
if not we proceed

```rust
use std::fs::File; // struct
use std::process;
use std::io::{stdin, Read};

fn main() {
    println!("Please provide input file");
    let mut input = String::new();

    let user_requested_file = stdin().read_line(input);
    if let Err(error) = user_requested_file {
        eprintln!("something went wrong collecting user input {error:?}");
            process::exit(1)
    }

    // returns a Result enum
    // file struct becomes mutable
    let mut file = match File::open(input.trim()) {
        Ok(file) => file,
        Err(error) => {
            eprintln!("some went wrogn opening the file {error}");
            process::exit(1)
        }
    };
    // from here we have a valid file
    let mut file_content = String::new();
    let read_operation = file.read_to_string(file_content);

    if let Err(error) = read_operation {
        eprintln!("something went wrong reading file {error}");
        process::exit(1)
    }

    println!("{file_content:?}");
}
```

## propogating errors

[propagating errors](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#propagating-errors)


```rust
use std::fs::File; // struct
use std::io::{self, stdin, Read};

fn main() {
    let file_result = read_file();
    match file_result {
        Ok(content) => println!("{content}"),
        Err(error) => {
            eprintln!("There was an error: {error:?}");
        }
    }
}

fn read_file() -> Result<String, io::Error> {
    println!("Please provide input file");
    let mut input = String::new();

    let user_requested_file = stdin().read_line(input);
    if let Err(error) = user_requested_file {
        return Err(error);
    }

    // returns a Result enum
    // file struct becomes mutable
    let mut file = match File::open(input.trim()) {
        Ok(file) => file,
        Err(error) => return Err(error),
    };
    // from here we have a valid file
    let mut file_content = String::new();
    let read_operation = file.read_to_string(file_content);

    if let Err(error) = read_operation {
        return Err(error)
    }
    Ok(file_content) 
}
```

## understanding error type redeclaration

[alias](https://doc.rust-lang.org/stable/std/io/type.Result.html)

many different type of errors within a category
- meaning that the error is specific to its context
    - io::Error;
    - fmt::Error; 

```rust
pub struct Error {
    repr: Repr,
}


pub struct Error;
```

```rust
io.Result -> where custom type is 
// create a type alias -> nic name for an existing type
// the alias says the T is flexible, the error type is always the Error type from the io module
// This is defined in the io module/package
pub type Result<T> = result::Result<T, Error>
```

## the > operator (the try operator)

[? operataor](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#a-shortcut-for-propagating-errors-the--operator)

```rust
use std::fs::File; // struct
use std::io::{self, stdin, Read};

fn main() {
    let file_result = read_file();
    match file_result {
        Ok(content) => println!("{content}"),
        Err(error) => {
            eprintln!("There was an error: {error:?}");
        }
    }
}

fn read_file() -> Result<String, io::Error> {
    println!("Please provide input file");
    let mut input = String::new();
    stdin().read_line(input)?; // if result is Error the code stops here
   
    let mut file =  File::open(input.trim())?;
 
    let mut file_content = String::new();
    file.read_to_string(file_content)?;
    
    Ok(file_content) 
}
```

refactor file with ? operator


```rust
use std::fs::File; // struct
use std::io::{self, stdin, Read};

fn main() {
    let file_result = read_file();
    match file_result {
        Ok(content) => println!("{content}"),
        Err(error) => {
            eprintln!("There was an error: {error:?}");
        }
    }
}

fn read_file() -> Result<String, io::Error> {
    println!("Please provide input file");
    
    let mut input = String::new();
    stdin().read_line(input)?; // if result is Error the code stops here
   

    let mut file_content = String::new();
    // open 
    // open err -> returns an error, the program returns
    // open ok -> return the associated data
    // read_to_string
    // read_to_string err -> returns an error, the program returns
    // read_to_string ok -> 
    File::open(input.trim())?.read_to_string(file_content)?;
    
    Ok(file_content) 
}
```

## read_to_string associated fn

[read_to_string](https://doc.rust-lang.org/std/fs/fn.read_to_string.html)

```rust
use std::fs;
use std::io::{self, stdin};

fn main() {
    let file_result = read_file();
    match file_result {
        Ok(content) => println!("{content}"),
        Err(error) => {
            eprintln!("There was an error: {error:?}");
        }
    }
}

fn read_file() -> Result<String, io::Error> {
    println!("Please provide input file");
    
    let mut input = String::new();
    stdin().read_line(input)?; // if result is Error the code stops here
   

    fs::read_to_string(input.trim())
}
```

## using the ? option

[? operator can also be applied to option](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#where-the--operator-can-be-used)

```rust
fn main() {
    //
    let mut animals = vec!["Girafe", "Monkey", "Zebra"];
    println!("{:?}", length_of_last_element(&mut animals));
    println!("{:?}", length_of_last_element(&mut animals));
    println!("{:?}", length_of_last_element(&mut animals));
    println!("{:?}", length_of_last_element(&mut animals));
}

fn length_of_last_element(input: &mut Vec<&str>) -> Option<usize> {
    let last_element = input.pop()?; // None return early, Some return string slice
    Some(last_element.len())
}
```