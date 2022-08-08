# javascript loops

## for loop

```
for (let counter = 5; counter <= 10; counter++) {
  console.log(counter);
}
```

```
const vacationSpots = ['Bali', 'Paris', 'Tulum'];

for (let i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}
```

## while

```
const cards = ['diamond', 'spade', 'heart', 'club'];

// Write your code below
let currentCard
while (currentCard != 'spade') {
  currentCard = cards[Math.floor(Math.random() * 4)];
  console.log(currentCard)
}
```

## do..while

```
let cupsOfSugarNeeded = 3;
let cupsAdded = 0;

do {
 cupsAdded++
 console.log(cupsAdded + ' cup was added') 
} while (cupsAdded < cupsOfSugarNeeded);
```

## break

## iterators

run on arrays -> see types-variables.md in array section

- .forEach()
- .map()
- .filter()

