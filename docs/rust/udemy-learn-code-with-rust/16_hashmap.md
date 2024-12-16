# hashmap

[key value](https://doc.rust-lang.org/book/ch08-03-hash-maps.html#storing-keys-with-associated-values-in-hash-maps)

[new hashmap](https://doc.rust-lang.org/book/ch08-03-hash-maps.html#creating-a-new-hash-map)

[hashmap](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.new)

hashmap
- key, value
- association/pairing between key and value
- no order

```rust
use std::collections::HashMap

fn main() {
    let mut menu: HahsMap<String, f64> = HashMap::new();

    menu.insert(String::from("Steak"), 29.99);
    menu.insert(String::from("Tuna"), 29.99);
    menu.insert(String::from("Burger"), 14.99);
    // implements the debug trait, not display trait
    println!("{menu:?}");

    // syntax with turbo fish operator
    let mut country_capitals = HashMap::<&str, &str>::new();
    country_capitals.insert("France", "Paris");
    country_capitals.insert("Germany", "berlin");
    println!("{country_capitals:?}");
}
```

## remove

[remove method](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.remove)


```rust
use std::collections::HashMap

fn main() {
    let data = [
        ("Boby", 7),
        ("Grant", 4),
        ("Ben", 6),
    ];
    
    let mut years_at_company = HashMap::from(data);

    // if ben exists we get the associated value back in an option enum
    let ben = years_at_company.remove("Ben");
}
```

## ownership

- hashmap lives on heap
- hashmap is owner of the data for the key and value store
- if the type does not implmenent copy trait
    - hashmap takes ownership
- if the type implement the copy trait
    - a copy will be made

```rust
use std::collections::HashMap

fn main() {
    let mut coffee_pairrings = HashMap::<&String, &String>::new();

    let drink = String::from("Latte")
    let milk = String::from("Oat Milk")

    coffee_pairrings.insert(&drink, &milk)

}
```

## access a value by a key

[accessing](https://doc.rust-lang.org/book/ch08-03-hash-maps.html#accessing-values-in-a-hash-map)

[get](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.get)

```rust
use std::collections::HashMap

fn main() {
    let mut coffee_pairrings = HashMap::<&str, &str>::new();

    let drink = String::from("Latte")
    let milk = String::from("Oat Milk")

    coffee_pairrings.insert(&drink, &milk)
    coffee_pairrings.insert("Flat White", "Almond Milk")

    // panics if the key does not exist
    let value = coffee_pairrings["Cappuccino"]
    // safer option -> returns an option with a ref
    // ref avoids taking ownership
    let value = coffee_pairrings.get("Cappuccino")

    let value = coffee_pairrings
        .get("Cappuccino")
        .copied()
        .unwrap_or("Unknown Milk")
    println!("{}", value)

}
```

## overwite

[overwrit](https://doc.rust-lang.org/book/ch08-03-hash-maps.html#overwriting-a-value)

```rust
use std::collections::HashMap

fn main() {
    let mut coffee_pairrings = HashMap::<&str, &str>::new();

    let drink = String::from("Latte")
    let milk = String::from("Oat Milk")

    coffee_pairrings.insert(&drink, &milk)
    coffee_pairrings.insert("Flat White", "Almond Milk")

    coffee_pairrings.insert("Latte", "Almond Milk")
}
```

## entry

[entry](https://doc.rust-lang.org/book/ch08-03-hash-maps.html#adding-a-key-and-value-only-if-a-key-isnt-present)

[method entry](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.entry)

- accepts a hasmap key, retrun enum called Entry
    - variants: key exist (occupied) or not exist (vacant)


```rust
use std::collections::HashMap

fn main() {
    let mut coffee_pairrings = HashMap::<&str, &str>::new();

    let drink = String::from("Latte")
    let milk = String::from("Oat Milk")

    coffee_pairrings.insert(&drink, &milk)
    coffee_pairrings.insert("Flat White", "Almond Milk")

    // entry -> Occupied or Vacant
    // or_insert: insert kv pair if the key does not exist
    coffee_pairrings.entry("Latte").or_insert("Pistacho Milk")
}
```

## HashSet

[hashset](https://doc.rust-lang.org/std/collections/struct.HashSet.html)

```rust
use std::collections::HashSet

fn main() {
    let mut concert_queue = HashSet::<&str>::new();

    concert_queue.insert("Molly");    
    concert_queue.insert("Megan");    
    println!("{:?}", concert_queue)

    // already exists -> prevents duplication
    concert_queue.insert("Molly");
    // return a boolean
    concert_queue.remove("Molly");
    // return a boolean
    concert_queue.contains("Megan");

    // Option Some/None -> with the ref of the value (avoids movinf ownership)
    concert_queue.get("Megan");   
}
```

## HashSet operation

[hashset operations](https://doc.rust-lang.org/std/collections/struct.HashSet.html)


```rust
use std::collections::HashSet

fn main() {
    let mut concert_queue = HashSet::<&str>::new();
    let mut movie_queue = HashSet::<&str>::new();

    concert_queue.insert("Boris");   
    concert_queue.insert("Melissa");
    
    movie_queue.insert("Boris");
    movie_queue.insert("Phil");

    // collection of both
    println!("{:?}", concert_queue.union(&movie_queue));
    println!("{:?}", movie_queue.union(&concert_queue));

    // find in concert_queue, but not found in movie_queue
    println!("{:?}", concert_queue.difference(&movie_queue));
    // find in movie_queue, but not found in concert_queue
    println!("{:?}", movie_queue.difference(&concert_queue));

    // not found in both
    println!("{:?}", concert_queue.symmetric_difference(&movie_queue));
    println!("{:?}", concert_queue.symmetric_difference(&movie_queue));

    // if nothing is shared in between them -> false
    println!("{:?}", concert_queue.is_disjoint(&movie_queue));
    println!("{:?}", concert_queue.is_disjoint(&movie_queue));

    // 
    println!("{:?}", concert_queue.is_subset(&movie_queue));
    println!("{:?}", concert_queue.is_subset(&movie_queue));

    println!("{:?}", concert_queue.is_superset(&movie_queue));
    println!("{:?}", concert_queue.is_superset(&movie_queue));
}
```