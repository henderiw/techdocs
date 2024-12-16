# enums

[enums](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html#defining-an-enum)


- An enum is a type that represents a set of possible values. Each possible value is called a variant


```rust
#[derive(Debug)]
enum CardSuite { // This is a blueprint
    // variants belonging to the enum
    Hearts,
    Diamonds,
    Spades,
    Clubs,
} 

struct Card {
    rank: String,
    suit: CardSuite,
}

fn main() {
    let first_card = CardSuite::Hearts;
    let mut second_card = CardSuite::Spades; 
    second_card = CardSuite::Clubs;
    println!("{:?}", second_card);

    let card_suits = [CardSuit::Hearts, CardSuit::Clubs]
}
```

## enum with associated values

[enum](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html#enum-values)

How to couple a variant with associated data -> without using a tuple

```rust
#[derive(Debug)]
enum PaymentMethodTypes {
    CreditCard(String),
    DebitCard(String),
    PayPal(String, String),
}

fn main() {
    // it is like a constructor type
    let my_payment = PaymentMethodTypes::CreditCard(String::from("0001"));

    my_payment = aymentMethodTypes::PayPal(String::from("0001"), String::from("bla"));

}
```

advantage of associated values is that different collection of data can belong

## Enum memory

per String 24 bytes on the stack
-> PayPal uses 2x24 bytes -> 48 bytes is stored using the worse case scenario

## Sruct variants

A struct variant stores associated data in fields rather than by position. Each piece of data has an assocated name

```rust
#[derive(Debug)]
struct Credentials {
    username: String,
    password: String,
}

#[derive(Debug)]
enum PaymentMethodTypes {
    CreditCard(String),
    DebitCard(String),
    PayPal(Credentials),
}

fn main() {
    let paypal_credentials = Credentials {
        username: String::from("me@gmail.com"),
        passowrd: String::from("pp"),
    }

    let paypal = PaymentMethodTypes::PayPal(paypal_credentials);
}
```

```rust
#[derive(Debug)]
struct Credentials {
    username: String,
    password: String,
}

#[derive(Debug)]
enum PaymentMethodTypes {
    CreditCard(String),
    DebitCard(Credentials), // struct variant
    PayPal {username: String, password: String}, // struct variant
    Cash,
}

fn main() {
    let paypal_credentials = Credentials {
        username: String::from("me@gmail.com"),
        passowrd: String::from("pp"),
    }

    let mut paypal = PaymentMethodTypes::DebitCard(paypal_credentials);
    paypal PaymentMethodTypes::PayPal {
        username: String::from("me@gmail.com"),
        passowrd: String::from("pp"),
    };
}
```

## nesting enums

```rust
#[derive(Debug)]
enum Beans {
    Pinto,
    Black,
}

#[derive(Debug)]
enum Meat {
    Chicken,
    Steak,
}


#[derive(Debug)]
enum ResourantItem {
    Buritto { meat: Meat, beans: Beans },
    Bowl( meat: Meat, beans: Beans ),
    VeganPlate,
}

fn main() {
    let lunch = ResourantItem::Buritto {
        meat: Meat::Steak, 
        beans: Beans::Black;
    };
    let dinner = ResourantItem::Bowl {
        meat: Meat::Chicken, 
        beans: Beans::Pinto;
    };
    let bla = ResourantItem::VeganPlate;

    println!("lunch was {lunch:?} and dinner was {dinner:?}")
}
```

## match keyword

[match](https://doc.rust-lang.org/book/ch06-02-match.html#the-match-control-flow-construct)
[match examples](https://doc.rust-lang.org/book/ch06-02-match.html#matches-are-exhaustive)

```rust
enum OperatingSystem {
    Windows,
    MacOS,
    Linux
}

fn main() {
    let my_computer = OperatingSystem::MacOS;
    // moves ownership
    let age = years_since_release(my_computer)
    println!("My computer is {age} old")

}

fn years_since_release(os: OperatingSystem) -> u32 {
    match os {
        OperatingSystem::Windows => 39,
        OperatingSystem::MacOS => 23,
        OperatingSystem::Linux => 34,
    }
}
```

[patterns that bind to Values](https://doc.rust-lang.org/book/ch06-02-match.html#patterns-that-bind-to-values)

```rust
enum OperatingSystem {
    Windows,
    MacOS,
    Linux
}

fn main() {
    let my_computer = OperatingSystem::MacOS;
    // moves ownership
    let age = years_since_release(my_computer)
    println!("My computer is {age} old")

}

fn years_since_release(os: OperatingSystem) -> u32 {
    // each arm should produce a consistent output
    match os {
        OperatingSystem::Windows => {
            println!("quite an old os");
            39
        },
        OperatingSystem::MacOS => 23,
        OperatingSystem::Linux => 34,
    }
}
```

## match keyword

```rust

enum LaundryCycle {
    Cold,
    Hot {temp: u32},
    Delicate(String),
}

fn main() {
    wash_laundry(LaundryCycle::Cold);
    wash_laundry(LaundryCycle::Hot {temp: 33});
    wash_laundry(LaundryCycle::Delicate(String::from("Silk")));

}

fn wash_laundry(cycle: LaundryCycle) {
    match cycle {
        LaundryCycle::Cold => {
            println!("Running the laundry with cold temp")
        },
        LaundryCycle::Hot {temp: u32} => {
            println!("Running the laundry with {temp} temp")
        }
        LaundryCycle::Delicate(fabric_type: String) => {
            println!("Running the laundry with {fabric_type}")
        }
    }
}
```

## methods on enum

```rust
enum LaundryCycle {
    Cold,
    Hot {temp: u32},
    Delicate(String),
}

impl LaundryCycle {
    // rust will also use references for its associated values
    fn wash_laundry(&self) {
        // rus takes care of dereferencing
        match self {
            LaundryCycle::Cold => {
                println!("Running the laundry with cold temp")
            },
            LaundryCycle::Hot {temp: &u32} => {
                println!("Running the laundry with {temp} temp")
            }
            LaundryCycle::Delicate(fabric_type: &String) => {
                println!("Running the laundry with {fabric_type}")
            }
        }
    }
}

fn main() {
    LaundryCycle::Cold.wash_laundry()
    let hot_cycle =  LaundryCycle::Hot {temp: 33}
    hot_cycle.wash_laundry()
   
   let delicate_cycle = LaundryCycle::Delicate(String::from("Silk"))
   delicate_cycle.wash_laundry()
}
```

## match against multiple values 

```rust
#[derive(Debug)]
enum OnlineOrderStatus {
    Ordered,
    Packed,
    Shipped,
    Delivered,
}

impl OnlineOrderStatus {
    fn check(&self) {
        match self {
            OnlineOrderStatus::Delivered = {
                println!("Your item has been delivered");
            }
            OnlineOrderStatus::Ordered | OnlineOrderStatus::Packed | OnlineOrderStatus::Shipped = {
                println!("Your item has been preped for shipment");
            }
            other_status => {
                println!("Your item is {other_status:?}");
            }
        }
    }
}

fn main() {
    OnlineOrderStatus::Delivered.check();
}
```

## match against exact values 

-> we can match with a variant with associated data

```rust
#[derive(Debug)]
enum Milk {
    Lowfat(i32),
    Whole,
}

impl Milk {
    // this takes ownership
    fn drink(self) {
        match self {
            Milk::Lowfat(2) => {
                println!("low fat 2%");
            }
            // order matters -> match is sequential
            Milk::Lowfat(percent) => {
                println!("low milk {percent}");
            }
            Milk::Whole => {
                println!("whole milk");
            }
        }
    }
}

fn main() {
    Milk::Delivered.Lowfat(1).drink();
}
```

## the let construct

[let](https://doc.rust-lang.org/book/ch06-03-if-let.html#concise-control-flow-with-if-let)
[if let](https://doc.rust-lang.org/rust-by-example/flow_control/if_let.html)

match keyword can be excessive
match against just 1 scenario

the if let construct combines an if statement with a veriable declaration

```rust
#[derive(Debug)]
enum Milk {
    Lowfat(i32),
    Whole,
    NonDiary {kind: String},
}

fn main() {
    let my_beverage = Milk::Lowfat(2);

    // the specific needs to be first
    // the let is relevant when associated data is present
    if let Milk::Lowfat(percent: i32) = my_beverage {
        println!("you have {precent}% milk")
    }

    let my_beverage = Milk::NonDiary {
        kind: String::from("oat");
    };

    // the specific needs to be first
    // the let is relevant when associated data is present
    if let Milk::Lowfat {kind } = my_beverage {
        println!("you have {kind} milk")
    } else {
        println!("other milk variant")   
    }
}
```

## the let else

if dynamic does not match

```rust
#[derive(Debug)]
enum Milk {
    Lowfat(i32),
    Whole,
    NonDiary {kind: String},
}

fn main() {
    let my_beverage = Milk::Whole;

    
    let Milk::Lowfat(percent: i32) = my_beverage else {
        // Execute if my beverage is NOT equal to my lowfat variant
        println!("you do not have the lowfat milk");

        // you need to terminate
        // option 1
        return;
    }
    println!("{percent} milk is availabel here");
}
```

[enum examples](https://doc.rust-lang.org/rust-by-example/custom_types/enum.html)