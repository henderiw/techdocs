# control flow

[expressions](https://doc.rust-lang.org/book/ch03-05-control-flow.html#if-expressions)
[expression example](https://doc.rust-lang.org/rust-by-example/flow_control/if_else.html)

- control flow refers to how a program will execute
- conditional code: if condition is met
    - enables different paths in the code


```rust
fn main() {
    // expression - evaluaties truthiness
    let some_condition = true;
    if some_condition {
        println!("This line will be output")
    }

    // this will not execute
    if false {
        println!("This line will NOT output")
    }
}
```

```rust
fn main() {
    let season = "summer";

    // compare equality
    if season == "summer" { // first check this
        println!("school is out");
    } else if season == "winter" { // this gets executed if previous statement did not evaluate to true
        println!("cold brr");
    } else if season == "fall" {
        println!("leaves falling");
    } else if season == "spring" {
        println!("rain");
    }
}
```

## assigning result of if statements to a variable

```rust

fn even_or_odd(number: i32) -> &str {
    let result = if number % 2 == 0 { "even" } else { "odd" };
    return result
}

fn main() {
    even_or_odd(17)
}
```

## match statement

- match -> like switch statement
- a pattern or arm is one possible option to compare the match value
- rocket syntax

```rust
fn main() {
    let evaluation = true;
    match evaluation {
        true => { // block when evaluation is true
            println!("the value is true");
        } 
        false => {
            println!("the value is false");
        }
    }
}
```

optimized syntax if the code

```rust
fn main() {
    let evaluation = true;
    let value = match evaluation {
        true => 20,
        false => 40,
    };
}
```

[catch all](https://doc.rust-lang.org/book/ch06-02-match.html#catch-all-patterns-and-the-_-placeholder)

```rust
fn main() {
    let season = "summer";

    // match statement is matching in sequence
    match season {
        "summer" => println!("school is out"),
        "winter" => println!("cold brr"),
        _ => println!("lots of rain"), // catch all
    }
}
```

```rust
fn main() {
    let number = 8;

    // using multiple values in match
    match number {
        2 | 4 | 6 | 8 => println!("{number} is even"),
        1 | 3 | 5 | 7 => println!("{number} is odd"),
        _ => println!("{number} is unknown"),
    }

    match number {
        value if value % 2 == 0 => println!("{value} is even"),
        value if value % 2 != 0 => println!("{number} is odd"),
        _ => unreachable!(),
    }
}
```

## iterate

[loop](https://doc.rust-lang.org/book/ch03-05-control-flow.html#repeating-code-with-loop)
[loop example](https://doc.rust-lang.org/rust-by-example/flow_control/loop.html)


- to iterate means to repeat
- `loop`
- `break` keyword breaks the loop
- `continue` foces a loop to the next iteration

```rust
fn main() {
    let mut seconds = 10;
    // infinite loop
    loop {
        if seconds == 0 {
            println!("Blastoff!!")
            break;
        }
        println!("{seconds} seconds to blastoff..")
        seconds -= 1;
    }
}
```

keyword: continue

```rust
fn main() {
    let mut seconds = 21;
    // infinite loop
    loop {
        if seconds <= 0 {
            println!("Blastoff!!")
            break;
        }

        if seconds % 2 == 0 {
            println!("{seconds} seconds even number skipping 3 seconds..")
            seconds -= 3;
            continue // gstop the current iteration -> go to the next iteration
        }

        println!("{seconds} seconds to blastoff..")
        seconds -= 1;
    }
}
```

## while loop

[while](https://doc.rust-lang.org/book/ch03-05-control-flow.html#conditional-loops-with-while)
[while example](https://doc.rust-lang.org/rust-by-example/flow_control/while.html)

a while loops continues iterating as long as the condition holds true

```rust
fn main() {
    let mut seconds = 21;
    // infinite loop
    while seconds > 0 {
        if seconds % 2 == 0 {
            println!("{seconds} seconds even number skipping 3 seconds..")
            seconds -= 3;
            continue // gstop the current iteration -> go to the next iteration
        }

        println!("{seconds} seconds to blastoff..")
        seconds -= 1;
    }
    println!("Blastoff!!")
}
```

## recursion

[recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))

- recursion: when a fn calls itself
- base case -> condition to stop the recursion

```rust
fn countdown(seconds: i32) {
    if seconds == 0 {
        // base case -> condition to stop the recursion
        println!("Blastoff!!")
    } else {
        println!("{seconds} seconds to blastoff..");
        countdown(seconds-1);
    }
}

fn main() {
    countdown(5);
}
```