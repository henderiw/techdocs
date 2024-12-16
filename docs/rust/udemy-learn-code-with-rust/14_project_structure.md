# project structure 

## package and crates

[package, crates, modules](https://doc.rust-lang.org/book/ch07-00-managing-growing-projects-with-packages-crates-and-modules.html)

[packages, crates](https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html#packages-and-crates)

cargo new -> creates a package 

package:
- folder with a cargo.toml files
- cargo.toml holds metadata about the package:
    - name
    - version
- a collection of one or more crates

crate:
- collection of rust code that produces an executable or a library
- smallest amount of code that the rust compiler considers at the a time
- a binary crate
    - has a main fn -> compiles to an executable
- a lib crate (crate is referred to a library crate)
    - does not have a main fn -> exports functionality, that can be used by binary crates
- you need 1 crate in a package

cargo new 
- create a cargo.toml
    - name: warehouse
- src directory with main.rs file
    - main.rs in src -> binary create with name of the toml.cargo
    - lib.rs in src -> cargo assumes the package contains a library with the name of the cargo.toml field

## modules

[module cheat sheet](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html#modules-cheat-sheet)

[grouping code in modules](https://doc.rust-lang.org/book/ch07-02-defining-modules-to-control-scope-and-privacy.html#grouping-related-code-in-modules)

[expose](https://doc.rust-lang.org/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html#exposing-paths-with-the-pub-keyword)

[visibility](https://doc.rust-lang.org/rust-by-example/mod/visibility.html)

module: organizational container that encapsulates related code

scope resolution operator -> ::
private/public



```rust
// mod -> organizational container
mod inventory {
    const FLOOR_SPACE: i32 = 10000;
    pub const MANAGER: &str = "Ivan Inventory";

    #[derive(Debug)]
    enum ProductCategory {
        Ladder,
        Hammer,
    }

    #[derive(Debug)]
    struct Item {
        name: String,
        category: ProductCategory,
        quantity: u32,
    }

    fn talk_to_manager() {
        println!("Hey, {MANAGER}, how's your day")
    }
}

mod orders {
    pub const MANAGER: &str = "oiler orderson";
}

fn main() {
    println!("the manager of our inventory is {}", inventory::MANAGER)
    println!("the manager of our order is {}", orders::MANAGER)
}
```

namespace allows for duplicate names

## seperating modules in files

[modules in files](https://doc.rust-lang.org/book/ch07-05-separating-modules-into-different-files.html#separating-modules-into-different-files)


crate root:
- main.rs
- is the base/foundation of a crate

how rust looks for modules
- look in the crate root -. sees mod inventory; -> look for 2nd file with the <module_name>.rs
- look for a file with the name = <module_name>.rs


main.rs
```rust
mod inventory;

mod orders {
    pub const MANAGER: &str = "oiler orderson";
}

fn main() {
    println!("the manager of our inventory is {}", inventory::MANAGER)
    println!("the manager of our order is {}", orders::MANAGER)
}
```

inventory.rs
```rust
const FLOOR_SPACE: i32 = 10000;
pub const MANAGER: &str = "Ivan Inventory";

#[derive(Debug)]
enum ProductCategory {
    Ladder,
    Hammer,
}

#[derive(Debug)]
struct Item {
    name: String,
    category: ProductCategory,
    quantity: u32,
}

fn talk_to_manager() {
    println!("Hey, {MANAGER}, how's your day")
}
```

## modules in directory/folder

folder has the module name -> filename mod.rs


inventory/mod.rs
```rust
const FLOOR_SPACE: i32 = 10000;
pub const MANAGER: &str = "Ivan Inventory";

#[derive(Debug)]
enum ProductCategory {
    Ladder,
    Hammer,
}

#[derive(Debug)]
struct Item {
    name: String,
    category: ProductCategory,
    quantity: u32,
}

fn talk_to_manager() {
    println!("Hey, {MANAGER}, how's your day")
}
```

orders/mod.rs
```rust
pub const MANAGER: &str = "oiler orderson";
```

main.rs
```rust
mod inventory;
mod orders;

fn main() {
    println!("the manager of our inventory is {}", inventory::MANAGER)
    println!("the manager of our order is {}", orders::MANAGER)
}
```

## module ambiguity

module files and folder can not coexist

## makeing enum, structs pub

[pub](https://doc.rust-lang.org/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html#making-structs-and-enums-public)

[struct visibility](https://doc.rust-lang.org/rust-by-example/mod/struct_visibility.html)


inventory/mod.rs
```rust
pub const FLOOR_SPACE: i32 = 10000;
pub const MANAGER: &str = "Ivan Inventory";

#[derive(Debug)]
pub enum ProductCategory {
    Ladder,
    Hammer,
}

#[derive(Debug)]
pub struct Item {
    pub name: String,
    pub category: ProductCategory,
    pub quantity: u32,
}

pub fn talk_to_manager() {
    println!("Hey, {MANAGER}, how's your day")
}
```

a struct field remain private
- we can expose them all public
- we can use an associate fn to access and define the private fields
- fn on an impl, we need to declare them pub to use them externally

```rust
mod inventory;
mod orders;

fn main() {
    println!("the inventory mgr {}, order mangere {}. we have square foor {}", inventory::MANAGER, orders::MANAGER, inventory::FLOORSPACE)

    inventory.talk_to_manager();

    let favorite_category = inventory::ProductCategory::Hammer;
    println!("My favorite category")

    // struct fields remain private
    let tall_ladder = inventory::Item{
        name: String::from("ladder"),
        category: favorite_category,
        quantaty: 100,
    }
}
```

## submodules

we can nest mdoules in modules

options:
// inline
// inventory/product.rs
// inventory/product/mod.rs

need to expose products as pub

```rust
let favorite_category = inventory::products::ProductCategory::Hammer;
```

## the crate prefix

[crate prefix](https://doc.rust-lang.org/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html#paths-for-referring-to-an-item-in-the-module-tree)

path:
- absolute path: complete path to a name
    - crate::inventory::MANAGER
- reletive path: we start relative from the current module
    - MANAGER
    - products::ProductCategory::Ladder

## the use keyword

[use keyword](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#bringing-paths-into-scope-with-the-use-keyword)

[nested paths](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#using-nested-paths-to-clean-up-large-use-lists)

[use example](https://doc.rust-lang.org/rust-by-example/mod/use.html)

use:
- brings names in the current path
- shortcut

```rust
mod inventory;
mod orders;

// we bring a given name in the file scope
use inventory::{FLOORSPACE, talk_to_manager};
use inventory::product::{Item, ProductCategory};
use orders::{MANAGER};


fn main() {
    println!("the inventory mgr {}, order mangere {}. we have square foor {}", 
        inventory::MANAGER, 
        orders::MANAGER, 
        FLOORSPACE
    );

    talk_to_manager();

    let favorite_category = ProductCategory::Hammer;
    println!("My favorite category {favorite_category:?}")

    // struct fields remain private
    let tall_ladder = Item{
        name: String::from("ladder"),
        category: favorite_category,
        quantaty: 100,
    }
    println!("{:#?}", tall_ladder)
}
```

## self keyword

```rust
mod inventory;
mod orders;

// we bring a given name in the file scope
use inventory::product::{self, ProductCategory}
use inventory::{FLOORSPACE, talk_to_manager};

fn main() {
    println!("the inventory mgr {}, order mangere {}. we have square foor {}", 
        inventory::MANAGER, 
        orders::MANAGER, 
        FLOORSPACE
    );

    talk_to_manager();

    let favorite_category = ProductCategory::Hammer;
    println!("My favorite category {favorite_category:?}")

    // struct fields remain private
    let tall_ladder = product::Item{
        name: String::from("ladder"),
        category: favorite_category,
        quantaty: 100,
    }
    println!("{:#?}", tall_ladder)
}
```

## super keyword

[super](https://doc.rust-lang.org/book/ch07-03-paths-for-referring-to-an-item-in-the-module-tree.html#starting-relative-paths-with-super)

[super and self](https://doc.rust-lang.org/rust-by-example/mod/super.html)

modules
- submodule is a child module
super -> parent
- a child can access the parent

products.rs
```rust
#[derive(Debug)]
pub enum ProductCategory {
    Ladder,
    Hammer,
}

#[derive(Debug)]
pub struct Item {
    pub name: String,
    pub category: ProductCategory,
    pub quantity: u32,
}

impl Item {
    pub fn new(name: String, category: ProductCategory, quality: u32) -> Self {
        super::talk_to_manager(); // we can access this w/o pub keyword, since this is a parent
        Self {
            name,
            category,
            quality,
        }
    }
}
```

## alias

[alias](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#providing-new-names-with-the-as-keyword)

nicname for the import

```rust
mod inventory;
mod orders;

// we bring a given name in the file scope
use inventory::product::{self, ProductCategory}
use inventory::{MANAGER as INVENTORYMANAGER, FLOORSPACE, talk_to_manager};
use orders::MANAGER as ORDERSMANAGER

fn main() {
    println!("the inventory mgr {}, order mangere {}. we have square foor {}", 
        INVENTORYMANAGER, 
        ORDERSMANAGER, 
        FLOORSPACE
    );

    talk_to_manager();

    let favorite_category = ProductCategory::Hammer;
    println!("My favorite category {favorite_category:?}")

    // struct fields remain private
    let tall_ladder = product::Item{
        name: String::from("ladder"),
        category: favorite_category,
        quantaty: 100,
    }
    println!("{:#?}", tall_ladder)
}
```

## reexporting

[use export](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#re-exporting-names-with-pub-use)

## external crates

[using creates](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html#using-a-crate-to-get-more-functionality)

[using external packages](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#using-external-packages)

A dependency is an external crate that we pull in
- cargo build
- cargo run
-> download the dependencies listed in the corgo.toml file

```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2021"

[dependencies]
fake = { version = "2.9.2", features = ["derive] }
```

products.rs
```rust
use fake::Dummy;

#[derive(Debug, Dummy)]
pub enum ProductCategory {
    Ladder,
    Hammer,
}

#[derive(Debug, Dummy)]
pub struct Item {
    pub name: String,
    pub category: ProductCategory,
    pub quantity: u32,
}

impl Item {
    pub fn new(name: String, category: ProductCategory, quality: u32) -> Self {
        super::talk_to_manager(); // we can access this w/o pub keyword, since this is a parent
        Self {
            name,
            category,
            quality,
        }
    }
}

```rust
mod inventory;
mod orders;

use fake::{Fake, Faker}

use inventory::product::{self, ProductCategory}
use inventory::{MANAGER as INVENTORYMANAGER, FLOORSPACE, talk_to_manager};
use orders::MANAGER as ORDERSMANAGER

fn main() {

    let fake_item Item = Faker.fake();
    println!("{:?}, fake_item")
}
```

## the rust standard library

[standard library](https://doc.rust-lang.org/std/)

a collection of modules built into rust

```rust
mod inventory;
mod orders;

use std::{fmt, io::{self, stdin, stdout}};

fn main() {

}
```

## the glob operator

[glob operator](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#the-glob-operator)

automatically import all names from that collections

NOT RECOMMENDED
- name collisions are possible

```rust

use std::collections::*

```

## create library crate

a package has to contain 1 library and/or 1 binary cratw

lib.rs
```rust
pub mod inventory;
pub mod orders;

pub use inventory::{Item, ProductCategory, FLOORSPACE, MANAGER AS INVENTORY_MANAGER}
pub use orders::MANAGER as ORDERS_MANAGER
```

main.rs
```rust
use fake::{Fake, Faker};

use warehouse::inventory::{Item, ProductCategory, FLOORSPACE, INVENTORY_MANAGER}

fn main() {

}
```

## multiple binary crates

in src create a bin folder
-> each .rs file is perceived as a binary crate

lib.rs stores the library

bin/summary.rs
```rust
use warehouse::{FLOORSPACE, INVENTORY_MANAGER, ORDERS_MANAGER};

fn main() {
    println!("Our managers are {} {}", INVENTORY_MANAGER,ORDERS_MANAGER )
}
```

run a specific executable

```shell
cargo run --bin warehouse
cargo run --bin summary
```

## documentation

```rust
/// Primary entrypoint into our warehouse program
fn main() {
    println!("This")
}
```

cargo docs 

## project structure

crates.io

