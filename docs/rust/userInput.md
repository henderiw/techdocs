# user input

```
// we can access this directly in the code
use std::io

// io::Result provide an error type already, so this is a special Result
fn get_input() -> io::Result<String> {
    let mut buffer = String::new();
    // the buffer is mutable borrowed -> changes the content of the buffer
    // read_line is a chain function
    // returns an error if the function fails
    // returns a buffer that is filled out
    io::stdin().read_line(&mut buffer)?;
    // returns buffer w/o whitespaces
    Ok(buffer.trim().to_owned())
}

fn main() {
    let mut all_input = vec![];
    let mut times_input = 0;
    while tims_input < 2 {
        match get_input() {
            Ok(words) => {
                all_input.push(words);
                times_input += 1;
            }
            Err(e) => println("error: {:?}", e),
        }
    }
    for input in all_input {
        println!(
            "Original: {:?}, capitalized: {:?}",
            input,
            input.to_uppercase()
        );
    }
}
```

Exercise a20