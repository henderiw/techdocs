# control-flow

## if - else

```
if a > 99 {
    if a > 200 {
        println!("huge number");
    } else {
        println!("big number");
    }
} else {
    println!("small number");
}
```

## match expression

- must be exhuastive -> every option must be accomodated

```
fn main() {
    let some_bool = true;
    match some_bool {
        true => println!("its true"),
        false => println!("its true"),
    }
}
```

```
fn main() {
    let some_int = 3;
    match some_int {
        1 => println!("its 1"),
        2 => println!("its 2"),
        3 => println!("its 3"),
        _ => println!("its something else"),

    }
}
```

match uses comma, since match works on expressions, not statements

match will be checked by the compiler
- new possibilities -> you will be notified
- use _ to match anything else

if/else is not checked by the compilar

## expression

expressions allow nested logic
    - expression values coalesce to a single point
if and match expressions can be used and can be nested
    - best not to use them too deep

assign the result of an expression to a value

```
let my_nu = 3;
// is_lt_5 is a value of an expression
let is_lt_5 = if my_num < 5 {
    true
} else {
    false
};
// short handed
let is_lt_5 = my_num < 5;>

```

Excercise a10

## advanced match

Uses Enumeration data or Struct match information

```
enum Discount {
    Percent(i32),
    Flat(i32),
}

struct Ticket {
    event: String,
    price: i32,
}

fn main() {
    let n= 3;
    match n {
        3 => println("three),
        // iso using _ we assigna variable
        other => println!("number: {:?}", other)
    }

    let flat = Discount::Flat(2);
    match flat {
        Discount::Flat(2) => println!("flat 2"),
        Discount::Flat(amount) => println!("flat discount of {:?}", amount),
        _ => (),   
    }

    let concert = Ticket {
        event: "concert".to_owned(),
        price: 50.0,
    }
    match concert {
        Ticket {price: 50, event} => println!("event @ 50 = {:?}", event),
        Ticket {price, ..} => println!("price = {:?}", price),
    }
}
```

Exercise a15

## if..let

perform action when you have some data and we are only interested in 1 thing

```
enum Color {
    Red,
    Blue,
    Green,
}
fn main() {
    let maybe_user = Some("Jerry");
    match maybe_user {
        Some(user) => println!("user={:?}", user),
        None => println!("no user),
    }

    // optimized code -> whcih does not do anything on None
    if let Some(user) = maybe_user {
        println!("user={:?}", user);
    }

    // same code with if let
    if let Some(user) = maybe_user {
        println!("user={:?}", user);
    } else {
        println!("no user");
    }

    let red = Color::Red;
    if let Color::Red = red {
        println!("red");
    } else {
        println!("not red");
    }
}
```