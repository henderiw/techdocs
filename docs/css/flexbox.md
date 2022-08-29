# flexbox

modern way the elements are displayed

- flex-container
- main axs vs cross axis
- the flex items

getting rid of display: inline-block

[flexbox background](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)


## display: flex

when we apply display: flex on an element we turn the parent elemnt as flex container

- parent: flex container
- children: flex items
- parent properties
  - flex-flow
  - justify-content
  - align-content
  - align-items
- child properties
  - order
  - flex
  - align-self

## flex container

[flex container](https://developer.mozilla.org/en-US/docs/Glossary/Flex_Container)

add display property with flex value
-> elements displayed in a row
-> all element in the container

display: flex
-> behaves like a block element in a row
display: inline-flex
-> behaves like an in-line element

properties:
- flex-direction: row (default) | column (behaves like a block) | column-reverse | row-reverse
- flex-wrap: no-wrap (default) | wrap | wrap-reverse

### flex container property -> main axis and cross axis

flex-direction: row
- main: top left 
- cross: top left to bottom left -> (starting point is the same as main)
- wrap accross the cross access
- elements adjust to the largest height

flex-direction: row-reverse
- main: top right -> left 
- cross: top right to bottom => (starting point is the same as main)

flex-direction: column
- main: top left to bottom
- cross: top left to top right -> (starting point is the same as main)
- wrap accross the cross access

flex-direction: column-reverse
- main: bottom left to top
- cross: bottom left to bottom right

shorthand:
/* flex-flow: row wrap */

## flex container property -> align-items + justify-content

align-items: stretch, center, flex-start, flex-end, baseline
-> refers to the cross axis

justify-content: center, flex-end
-> refers to the main axis

## flex container property -> align-content

a combination of align-item and kustify-context

space-between, center

align-content -> 

## flex container property -> z-index

Flexbox and the Z-Index
In the position module we learned that adding the z-index  to an element only has an effect, if the position  property with a value different from static  was applied to this element.

One exception from this behaviour is flexbox: Applying the z-index  to flex-items (so the elements inside of the flex-container) will change the order of these items even if no position  property was applied.

You will need the z-index  for flex-items in the following assignment, so keep that special behaviour in mind.

## flex-items properties

order: 
- 4th element should be positioned in the beginning
- order 0: default
- order 1: goes to the end => based on the flex-direction
- order -1: goes to the front => based on the flex-direction

align-self: -> positioned in relation to the cross axis
- flex-start, flex-end

flex-grow: -> focussed on growing
- default value = 0
- 1: element uses the space available and occupies the space
- 4: on another element -> gets 1/5th or 4/5th of the available space

flex-shrink: opposite -> focussed on decreasing
- default value = 1 -> allows to shrink
- 0: it cannot descrease its width

flex-basis:
- size of the element based on the main axis
- flex-direction is row -> width
  - auto -> fallback is width
  - if defined it overrides the weight
- flex-direction is column -> height
  - auto -> fallback is height
  - if defined it overrides the weight

shorthand:

```
flex: 0 1 auto
/* flex-grow flex-shrink flex-basis */
```