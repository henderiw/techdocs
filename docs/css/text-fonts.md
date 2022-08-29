# text-fonts

## generic families & font families
  - genric define a attribute
  - generic -> font families inside the generic 
    - serif -> times New Roman, Georgia
    - sans-serif -> Helveticaa, Verdana
    - cursive -> Brush script, Mistral
    - monospace -> courier New, Lucida Bright
    - (fantasy)
  - browser (chrome)
    - standard font: verdana
    - serif font
    - sans-serif font
    - fixed-width font
  - what will be displayed? 3 options
    - default behavior is defined by the browser
      - no font family is defined in css
      - no control on what will be displayed to the user
    - generic family selected in css, but supported by the browser
    - css font family
      - user's computer -> from a user's computer
      - web fonts -> e.g. google server
      - retrieved from a server
      - @import method in shared css files
  - font faces: (google www)
    - light 300 -> font weight
    - italic -> font style
  - font formats:
    - truetype format: .ttf
    - woff: web open fron format -> compressed
    - woff2.0 -> better compressed
    - eot -> embedded opentype formats -> no browser support
  - font properties that effect the letters
    - font-size: 40px;
    - font-variant: small-caps; -> capital
    - font-stretch: ultra-condensed; -> font availability is weak
  - letter spacing
    - letter spacing: 5px; space between the letters
    - white-space: pre | pre-wrap | pre-line
  - line height: space between top and botton of the content box
    - depends on the font family
  - text-decoration:
    - underline;
    - overline;
    - line-though;
    - botted-line
    - dotted | wavy + color
    - none -> to remove the default decoration
  - text-shadow:
    - 5px (x-axis) 5px (y-axis) 2px (blur) gray
  - font shorthand
    - 	/*font-style font-variant font-weight font-size/line-height font-family */
  - font-display:
    - impact loading behavior
      - swap: n/A + fallback + infinite (custom font)
      - block: short + fallback + infinite (custom font)
      - fallback: very short + fallback + short (custom font)
      - optional: very short + custom-font/fallback -> browser decides
      - auto
    - block period: space is reserved with an invisible font face
    - swap period: period to swap to the real fonts
    - uses in @font-face

## local file import

```
@font-face {
	font-family: "AnonymousPro";
	src: url("anonymousPro-Regular.ttf") format)"truetype");
	/*font-display: swap;*/
}
```

[web safe fonts](https://www.cssfontstack.com/)
[google fonts](https://fonts.google.com/)
[line-height](https://developer.mozilla.org/en-US/docs/Web/CSS/line-height)