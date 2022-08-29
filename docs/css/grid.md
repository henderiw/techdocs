# css grid

[css grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout)
[complete guide](https://css-tricks.com/snippets/css/complete-guide-grid/)

## what

- Header, footer, sidebar, title, text1/text2
- grid of row and columns
- bootstrap workshop -> positioning element

firefox is better for debugging css grid

## how

display: grid

- container becomes a grid
- child element become part of the grid -> creates row automatically
- by default:
  - 1 column
  - direct attached element become children as rows

## container properties

grid-template-columns: 200px 2fr 20% 1fr;
-> creates 4 columns + 1 fr (fraction) -> remaining space split
grid-template-rows: 200px 300px
-> create 2 rows

we can also use auto as value -> fills remaining/empty space

4 equal columns
grid-template-columns: 25% 25% 25% 25%;
grid-template-columns: repeat(4, 25%);

grid-template-rows: 5rem minmax(10px, 200px);

give columns and row names

grid-template-rows: [row-1-start] 5rem [row-1-end row-2-start] minmax(10px, 200px) [row-2-end row-3-start] 100px [row-3-end];

grid-column-gap: 2-0px -> gap between columns
grid-row-gap: 10px
grid-gap: (row-gap) (column-gap)
grid-template-areas: "header heaader header header"
                     "side main main main"
										 "footer footer footer footer"

## container children properties

positioning of an element -> counting starts with 1 (line numbers)
- grid-colum-start: 3
- grid-column-end: 5
- grid-row-start: 1
- grid-row-end: 3

start at 3 and span 2 cells
- grid-colum-start: 3
- grid-column-end: span 2
- grid-row-start: 1
- grid-row-end: 3

take a full row
- grid-column-start: 1;
- grid-column-end: -1;
-> does need to be revisted if the columns grow

ELEMENTS CAN OVERLAP IF YOU EXPLICITLY SET IT

what is the order -> the document flow, but can be changed with z-index

shorthand
- grid-column: 1 / -1; (start) / (end)
- grid-row: 3 / span2; (start) / (end)

- grid-area: (row-start) / (column-start) / (row-end) / (column-end)
- grid-area: header;

## grid areas

container

- grid-template-areas: "header heaader header header"
                     ". . main main"
										 "footer footer footer footer"

child elements

- grid-area: header;

## automating grid areas

container

```
grid-template-columns: [hd-start] repeat(4, [col-start] 25% [col-end]) [hd-end]
grid-template-rows: [hd-start] [row-1-start] 5rem [hd-end row-2-start] minmax(10px, 200px) [hd-end row-3-start] 100px [row-3-end] [hd-end];
```

child element

```
grid-column: col-start 2 / col-end 2
grid-area: hd
```

## practical

backdrop/modal/navigation/header -> position fixed or absolute
they are not part of the grid since they are not part of the document flow

fit-content(8rem)

## positioning elements in a grid

so far they always strecth the full cell

position within row
- justify-items: center | start | end; -> positions the element within the area/cell
-> default is strecth

position within column
- align-items: stretch(default | center | start | end)

## position the entire grid

when the grid does not fill the entire space

position on the x-axis
- justify-content: default (start) | center| end | stretch

position on the y-axis
- align-content: default (start) | center | end

## position element individually

position on the x-axis
- justify-self

position on the y-axis
- align-self

## responsive grids

how to use them with media content
-> we could have a grid that is different based on the media content from 3 rows to 4 rows.

using grid-area makes it easy to position the elements automatically based on the chanage of the grid

## auto-flow

display: grid

how do we control how many rows we create + the sizes

grid-auto-rows: auto | 30 rem | minmax(8 rem, auto)
grid-auto-flow: column
-> where new elements have to be added
grid-auto-columns: 5rem -> controls the width of the columns

## explicit & implicit grid

we can mix implicit and explicit behavior of it
-> new rows can be added automatically

## auto-fill & auto-fit

grid-template-columns: repeat(auto-fill, , 10rem)
grid-template-columns: repeat(auto-fit, , 10rem)

## dense grids

-> be carefull for screen readers

## practial

start hosting

## comparing grid vs flexbox