# dimensions

## units

- pixel: px
- percentages: %
- root em: rem -> refers to font size
- em: -> refer to font size
- viewport height: vh
- viewort width: vw

q1: which properties can i use in connection to these units?
- [font-size]( https://developer.mozilla.org/en-US/docs/Web/CSS/font-size)
- box model
  - content
  - padding
  - border
  - margin
  - width
  - height
- position
  - top
  - bottom
  - left
  - right

q2: how is the size calulates -> reference points
categories
- absolute lengths
  - mostly ignore user setting
  - e.g. px, (cm, mm)
- viewport lengths
  - vh, vw, vmin, vmax
  - visible part of the browser
- font-relative length
  - rem, em
- percentages
  - special case -> how is the box sie for % unts calcuated
  - 80% of what?
    - containing block
q3: whats the right unit to choose for which properties

## percentages and the containing block

rule1: element that the % is applied to, position fixed
  - element has property position: fixed
  - containing block is the viewport

rule2: element has % applied, position is absolute
	- containing block is the ancestor content + padding
	- what is the containing block?
  	- closest ancestor which is not position static
  	- iow: has position: absolute, relative, fixed, sticky

rule3: element has %, position static or relative
	- containing block
  	- closest ancestor which is block level element
  	- containing block is the content

use of height with % unit -> closest ancestor which is a block level element?
- backdrop
- margin collapsing -. top0

## min-width & max-width

min or max widt of an image

## rem vs em

calculated based on the fontsize -> when the use changes the fontsize of the browser it will not have effect when using px, but take into account when using em/rem

em -> dynamic but is dependent on INHERITANCE
rem -> fontsize by the browser and multiple by 1.1 -> we always go back to the root element of the browser setting (e.g. 16px)
	-> user controls the settings in the browser

browser support for rem was low, but these days this has changed

## vw and vh

used for backdrop

width: 100vw
height: 100vh

-> 100 is percetage

vmin -> takes the smallest of the height or weight
vmax -> takes the biggest of the height or weight

main.css #product-overview

```
Hiding Scrollbars on Windows machines
After adding vw , you probably saw that the scrollbars appeared in case you are working on Windows. This happens as using vw  on Windows does not include the scrollbars - vw: 100  is  equal to 100% of the viewport width + the scrollbars. On the Mac this is not an issue, but when using Windows it is as the scrollbars are displayed by default.

In case you don't want to display these scrollbars, you can use one of these solutions:

- Use width: 100%  instead of vw: 100

- Add overflow-x: hidden;  to the body selector in the shared.css file to hide the horizontal scrollbar (or overflow-y: hidden  to hide the vertical scrollbar)

Alternatively you could also use the ::-webkit-scrollbar pseudo element. Simply add the following code to the shared.css file:

body: :-webkit-scrollbar {
    width: 0
}
To make sure this works correctly on different browsers, you have to add additional code to it. This blog post nicely summarizes all the code needed right here.

Make sure to follow these approaches in case you don't want to display the scrollbars on Windows machines.
```

## which unit to choose -> guidance

font-size (root element) -> % or nothing (browser setting)
font-size -> rem (em => children only)
padding -> rem
margin -> rem
border -> px
width/height -> % (which containing block), vw/vh (backdrop, background)
top/bottom -> % (which containing block)
left/right -> % (which containing block)

TIP:
-> margin auto -> ONLY WORKS on BLOCK ELEMENTS