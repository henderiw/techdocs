# generics

[geenrics](https://doc.rust-lang.org/book/ch10-00-generics.html#removing-duplication-by-extracting-a-function)

is a type argument. its a future for a concrete type
- fn parameter -> placeholder for a value parameter
- generic  -> placeholder for a type
- generic is a type argument

```rust
#[derive(Debug)]
struct Bla {}

// rust will know the type T once invoked
fn identity<T>(value: T) -> T {
    value
}

fn main() {
    println!("{}", identity(5));
    println!("{}", identity(3.2));
    println!("{}", identity("hello"));
    println!("{}", identity(true));
    println!("{}", identity(Bla {}));
}
```

the compiler looks at the invokation and will create an implementation with a specific type
-> as developper you dont see this
-> monomorphization: compile time process

## Turbofish Operation

Turbofish Operation ::<i32>
- allows to customize T and explcitly define the type iso rust interpreting the value as i32

```rust
#[derive(Debug)]
struct Bla {}

// rust will know the type T once invoked
fn identity<T>(value: T) -> T {
    value
}

fn main() {
    println!("{}", identity::<i8>(5));
    println!("{}", identity::<&str>("hello"));
}
```

## multiple generics

```rust
fn make_tuple<T1, T2>(first: T1, second T2) -> (T1, T2) {
    (first, second)
}

fn main() {
    make_tuple("hello", 12);
}
```

## generics in structs

```rust
struct TressureChest<T> {
    captain: String,
    treasure: T,
}

fn main() {
    let gold_chest = TressureChest {
        captain: String::from("firebeard"),
        treasure: "Gold",
    }

    let silver_chest = TressureChest {
        captain: String::from("firebeard"),
        treasure: String::from("Silver"),
    }
    let special_chest = TressureChest {
        captain: String::from("bootyplunder"),
        treasure: ["Gold", "silver", "Platinum"],
    }
}
```

## struct implementation with generics

```rust
struct TressureChest<T> {
    captain: String,
    treasure: T,
}

// option 1: concrete type in impl - TressureChest on which the treassure field is a String these methods exist
impl TressureChest<String> {
    fn clean_treasure(&mut self) {
        self.treasure = self.treasure.trim().to_string()
    }
}

// option 2: concrete type in impl - TressureChest on which the treassure field is a 3 element array of string Slices these methods exist
impl TressureChest<[&str: 3]> {
    fn amount_of_treasure(&self) -> usize {
        self.treasure.len()
    }
}

// optio 3: making it generic
// we cannot use T as T could be a real struct or enum
// can be invoked on any struct, independent on how they implement type T
impl<T> TressureChest<T> {
    fn capital_captain(&self) -> String {
        self.captain.to_uppercase()
    }
}


fn main() {
    let gold_chest = TressureChest {
        captain: String::from("firebeard"),
        treasure: "Gold",
    }

    let silver_chest = TressureChest {
        captain: String::from("firebeard"),
        treasure: String::from("   Silver    "),
    }
    silver_chest.clean_treasure()

    let special_chest = TressureChest {
        captain: String::from("bootyplunder"),
        treasure: ["Gold", "silver", "Platinum"],
    }
    special_chest.amount_of_treasure()
}
```

## enum with generics

```rust
enum CheeseCake<T> {
    Plain,
    Topping(T),
}


fn main() {
    // &str
    let mushroom = CheeseCake::Topping("mushroom");
    let onions = CheeseCake::Topping("onions".to_string());
    let topping = "bacon".to_string();
    let bacon = CheeseCake::Topping(&topping);

    // this is not allowed, type T has to be known, since the enum can be mutable
    let mut plain: CheeseCake<String> = CheeseCake::Plain;
    plain = CheeseCake::Topping(String::from("sausage"));
}
```