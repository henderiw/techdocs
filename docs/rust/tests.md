# testing

```
fn all_caps(...)

fn main() {}

#[cfg(test)]
mod test {
    // collection of code is a crate
    // crate refers to all the code
    use crate::*;

    #[test]
    fn check_all_caps() {
        // rust test ->if program is aborted the test fails, otherwise it succeeds
        // assert_eq args -> 3 variables -> value we want to check, value we expect, msg to display if nok
        let result = all_caps("hello");
        let expected = String::from("HELLO);
        assert_eq!(result, expected, "string should be all uppercase");
    }
}

```

```
cargo test --bin a22
```

exercise a22