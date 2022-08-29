# css positioning 

index.html
- navigation bar disaapers
- background positioning of the image
package/index.html
- no background
- plus plan has no recomendation

##  positioning

position= static is the default

where an element is to be positioned in the document flow

other options:
- default position = static
- absolute
- relative
- fixed
- sticky

positioning context:
- where to position based on what context/element
- top/bottom left/right

## fixed navigation bar

position: fixed/absolute;
- positioning is relative to the viewport
- positioning is independent if the lement is block or in-line

```
.parent .child-1 {
	position: fixed;
	width: 100%;
	left: 0px;
	top: 0px;
	margin: 0;
	box-sizing:border-box;
}
```

## z-index

changes the alignment back/front
when elements have a position the order in the html file define who goes above who

## badge

position: absolute

positioning context
- clostest element with a position defined -> html element

position relative fixes this if we apply this to the package class
position relative is the element itself and is not taken out of the document flow

## overflow

overflow: hidden allows to hide the element if it goes 
overflow hidden in body selector is applied at html -. DEFAULT CSS behavior
apply overflow hidden to body and html -> this works
-> also wotks with overflow: auto

## position: sticky

- hybrid of relative and fixed
  - border is reached at the viewport: top is the distance from viewport
  - end is the content of the parent

broweser supprt is limited

## stacking context

position fixed: -> each has a z-index within the element's stacking context

## summary

- [positioning](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Positioning)
  - [position property](https://developer.mozilla.org/en-US/docs/Web/CSS/position)
    - static: default
    - fixed: 
    - absolute
    - relative
    - [sticky](https://caniuse.com/#search=sticky)
  - Document flow
    - the default positioning behavior of html elements
    - can be changed with position
    - elements can remain in the documeent flow or excluded
      - remain within document flow: relative
      - removed from document flow: fixed
    - Moving elements
      - top/bottom, left/right
    - Posiitoning Context
      - anchor point for positioning
      - fixed: viewport
      - absolute: another element: html or ancestor element with position property defined
      - relative: element
      - sticky: viewport and another element
    - [Z-index](https://developer.mozilla.org/en-US/docs/Web/CSS/z-index):
      - changes the default positioning along the z-axis
      - auto (0) is default
      - chnages only when position is applied
      - larger value = element is positioned on top of other elements
    - [stacking context](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context)
      - created when applying fixed/sticky or absolute/relative in combination with z-index
      - defines stacking behavior of child elements