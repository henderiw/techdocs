# strings

## strings

[strings](https://doc.rust-lang.org/book/ch08-02-strings.html#what-is-a-string)

string:
- a piece of text
- a sequence of characters
- types
    - &str: 
        - string slice
        - borrow of some text
            - string literal: embedded in the binary
            - can also be some heap
    - String
        - heap
        - can grow, can change
        - new(): associated function
            - constructs an empty instance
        - from(): associated fn from a binary location
        - to_string(): method

```rust
fn main() {
    let pirate: &str = "Bloodhook";

    let sailer: String = String::from(pirate);

    let bad_guy: String = pirate.to_string();

    println!("{pirate} and {sailer} and {bad_guy}");

    // to access the character, you need to use the range operator
    // reason is a slice is not allways a byte, e.g. emoji
    // UTF space can be 4 bytes

   let first_initial = &sailer[0..1];
   println!(first_initial)
}
```

## concatenation

[format](https://doc.rust-lang.org/book/ch08-02-strings.html#concatenation-with-the--operator-or-the-format-macro)

```rust
fn main() {
    let mut full_name = String::from("Sylvester");
    let last_name = String::from("Stallone");
    // push uses single character
    full_name.push(' ')
    full_name.push_str(&last_name); // through deref cooercsion &String -> &str
    println!({full_name})
}
```

alternative using +

```rust
fn main() {
    let first_name = String::from("Sylvester");
    let last_name = String::from("Stallone");
    // first_name ownership moved
    // + sign invokes add method: syntactic sugar
    // first_name.add(last_name)
    let full_name = first_name + &last_name
    println!({full_name})
}
```

add fn that is invoked with the +

```rust
fn add(mut self, other: &str) -> String {
    self.push_str(other);
    self
}
```

## format macro

returns a formatted string

[format](https://doc.rust-lang.org/book/ch08-02-strings.html#concatenation-with-the--operator-or-the-format-macro)

[format](https://doc.rust-lang.org/std/macro.format.html)

```rust
fn main() {
    let first_name = String::from("Sylvester");
    let last_name = String::from("Stallone");
    // does not transfer ownership
    let full_name = format!("{first_name} {&last_name}")
    println!({full_name})
}
```

## methods

[trim](https://doc.rust-lang.org/std/string/struct.String.html#method.trim)

[to_lowercase](https://doc.rust-lang.org/std/string/struct.String.html#method.to_lowercase)

[to_uppercase](https://doc.rust-lang.org/std/string/struct.String.html#method.to_uppercase)

[split](https://doc.rust-lang.org/std/string/struct.String.html#method.split)


```rust
fn main() {
    let mut music_genres = "       Rock, Metal, Rap     ";
    println!("{}", music_genres.trim());
    println!("{}", music_genres.trim_start());
    println!("{}", music_genres.trim_end());

    music_genres = music_genres.trim();
    // returns a new heap allocated string
    println!("{}", music_genres.to_uppercase());
    // returns a new heap allocated string
    println!("{}", music_genres.to_lowercase());
    // returns a new heap allocated string
    println("{}", music_genres.replace("a", "@"))

    let genres: Vec<&str> = music_genres.split(", ").collect();
    println!("{:?}", genres);
}
```

## user input with read_line

[user input](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html#receiving-user-input)

[read_line](https://doc.rust-lang.org/std/io/struct.Stdin.html#method.read_line)

```rust
use std::io;

fn main() {
    let mut name = String::new();
    // stdin -> return Stdin struct
    // read_line -> mut ref of a heap string
    println!("What is your name?");
    io.stdin().read_line(&mut name).expect("Failed to collect input from the user");
    println!("Hello, {name}");   
}
```

```rust
use std::io;

fn main() {
    let mut name = String::new();
    println!("What is your name?");
    match io.stdin().read_line(&mut name) {
        Ok(_) => println!("Hello, {}", name.trim());
        Err(msg) => println!("There was an error: {msg}");
    }
}
```